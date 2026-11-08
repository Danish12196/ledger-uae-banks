"""Resource-bounded multilingual transformer baseline with a frozen encoder.

CPU fallback avoids Windows host-commit/CUDA allocation failures. No messages leave this process.
"""
import argparse
import gc
import hashlib
import json
import os
from pathlib import Path
import sys
os.environ['HF_HUB_DISABLE_TELEMETRY']='1'
os.environ['TOKENIZERS_PARALLELISM']='false'
os.environ['OPENBLAS_NUM_THREADS']='4'
import numpy as np
import pandas as pd
import onnxruntime as ort
from tokenizers import Tokenizer
from sklearn.linear_model import LogisticRegression
from threadpoolctl import threadpool_limits
ROOT=Path(__file__).resolve().parents[1]
LOCAL=ROOT/'synth/local'
sys.path.insert(0,str(ROOT/'synth'))
from benchmark import load_real, score, DEADLINE
from scripts.rules import CATS
from datetime import datetime, timezone

def rows_for_round(number):
    syn=pd.read_json(LOCAL/f'round_{number}_synthetic.jsonl',lines=True)
    syn=syn[syn.label.isin(CATS) & syn.bank.ne('ADIB')]
    return syn.sample(n=min(12000,len(syn)),random_state=902)

def public_rows():
    frame=pd.read_csv(ROOT/'synth/out/synthetic_public.csv')
    frame=frame[frame.label.isin(CATS) & frame.bank.ne('ADIB')]
    return frame.sample(n=min(12000,len(frame)),random_state=902)

def extract():
    real=load_real()
    corpora=[real[['message']],public_rows()[['message']]]+[rows_for_round(n)[['message']] for n in (2,3)]
    text=pd.concat(corpora,ignore_index=True).drop_duplicates('message').reset_index(drop=True)
    ids=[hashlib.sha256(m.encode()).hexdigest() for m in text.message]
    features_path=LOCAL/'encoder_features.npy'
    # The cache contains private-derived embeddings and is never public.
    features=np.lib.format.open_memmap(features_path,mode='w+',dtype='float32',shape=(len(text),384))
    tokenizer=Tokenizer.from_file(str(LOCAL/'public_minilm/tokenizer.json'))
    tokenizer.enable_truncation(max_length=96)
    tokenizer.enable_padding()
    options=ort.SessionOptions()
    options.intra_op_num_threads=4
    options.inter_op_num_threads=1
    options.enable_mem_pattern=False
    session=ort.InferenceSession(str(LOCAL/'public_minilm/model.onnx'),sess_options=options,providers=['CPUExecutionProvider'])
    names={x.name for x in session.get_inputs()}
    print('Multilingual MiniLM encoder ready; local examples:',len(text),flush=True)
    if True:
        for start in range(0,len(text),8):
            if datetime.now(timezone.utc)>=DEADLINE:
                raise TimeoutError('Dubai deadline reached')
            batch=tokenizer.encode_batch(text.message.iloc[start:start+8].tolist())
            inputs={'input_ids':np.array([b.ids for b in batch],dtype=np.int64),
                    'attention_mask':np.array([b.attention_mask for b in batch],dtype=np.int64),
                    'token_type_ids':np.array([b.type_ids for b in batch],dtype=np.int64)}
            hidden=session.run(None,{k:v for k,v in inputs.items() if k in names})[0]
            mask=inputs['attention_mask'][:,:,None]
            vector=(hidden*mask).sum(axis=1)/mask.sum(axis=1).clip(min=1)
            vector=vector/np.linalg.norm(vector,axis=1,keepdims=True).clip(min=1e-12)
            features[start:start+len(vector)]=vector
            if start%2000==0:
                features.flush()
                print('Embedded local examples:',start,'/',len(text),flush=True)
    features.flush()
    (LOCAL/'encoder_index.json').write_text(json.dumps(dict(zip(ids,range(len(ids))))))
    (LOCAL/'encoder_complete.json').write_text(json.dumps({'n':len(ids),'encoder':'multilingual MiniLM L12 v2; quint8 avx2 ONNX','pooling':'attention masked mean; L2 normalization','device':'CPU','training':'encoder frozen; logistic classifier trained locally','max_length':96}))

def run(final=False):
    if not (LOCAL/'encoder_complete.json').exists():
        extract()
    real=load_real()
    lookup=json.loads((LOCAL/'encoder_index.json').read_text())
    embedded=np.load(LOCAL/'encoder_features.npy',mmap_mode='r')
    def x(frame):
        return embedded[[lookup[hashlib.sha256(m.encode()).hexdigest()] for m in frame.message]]
    training=real[(real.partition=='train') & real.bank.ne('ADIB')]
    validation=real[real.partition=='validation']
    results=[]
    for number in (2,3):
        synthetic=rows_for_round(number)
        for setup in ('real_only','real_plus_synthetic','synthetic_only'):
            data=training if setup=='real_only' else synthetic if setup=='synthetic_only' else pd.concat([training,synthetic],ignore_index=True)
            model=LogisticRegression(C=10,class_weight='balanced',max_iter=1000,random_state=902)
            with threadpool_limits(limits=4):
                model.fit(x(data),data.label)
            prediction=model.predict(x(validation))
            results.append({'round':number,'setup':setup,'model':'minilm_frozen_encoder_int8','train_n':len(data),'metrics':score(validation.label,prediction)})
            print('Frozen-encoder validation:',number,setup,round(results[-1]['metrics']['macro_f1'],4),flush=True)
    (LOCAL/'encoder_results.json').write_text(json.dumps(results,indent=2))
    if final:
        path=LOCAL/'encoder_final.json'
        if path.exists():
            print('Frozen-encoder final evaluation already exists')
            return
        out=[]
        test=real[real.partition=='test']
        development=real[(real.partition!='test') & real.bank.ne('ADIB')]
        for setup in ('real_only','real_plus_synthetic','synthetic_only'):
            chosen=max((r for r in results if r['setup']==setup),key=lambda r:r['metrics']['macro_f1'])
            synthetic=rows_for_round(chosen['round'])
            data=development if setup=='real_only' else synthetic if setup=='synthetic_only' else pd.concat([development,synthetic],ignore_index=True)
            model=LogisticRegression(C=10,class_weight='balanced',max_iter=1000,random_state=902)
            with threadpool_limits(limits=4):
                model.fit(x(data),data.label)
            prediction=model.predict(x(test))
            row={'setup':setup,'model':'minilm_frozen_encoder_int8','selected_round':chosen['round'],'test':score(test.label,prediction),'leave_one_bank_out':{}}
            for bank in sorted(real.bank.unique()):
                # Frozen encoder has no corpus fitting. Fixed round-2 public rows only,
                # no target-bank template mining or validation feedback in LOBO.
                fixed=public_rows()
                fixed=fixed[fixed.bank.ne(bank)]
                other=real[real.bank.ne(bank) & real.bank.ne('ADIB')]
                bank_test=real[real.bank.eq(bank)]
                other=other[~other.template_group.isin(bank_test.template_group)]
                data=other if setup=='real_only' else fixed if setup=='synthetic_only' else pd.concat([other,fixed],ignore_index=True)
                with threadpool_limits(limits=4):
                    model.fit(x(data),data.label)
                row['leave_one_bank_out'][bank]=score(bank_test.label,model.predict(x(bank_test)))
            out.append(row)
        path.write_text(json.dumps(out,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--final',action='store_true')
    args=parser.parse_args()
    run(args.final)
