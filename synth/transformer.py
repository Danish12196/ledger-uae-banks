"""Optional local GPU fine-tuning; all private text and model weights remain local."""
import argparse
from datetime import datetime, timezone
import gc
import json
import os
from pathlib import Path
import random
import sys
os.environ['HF_HUB_DISABLE_TELEMETRY']='1'
os.environ['HF_HUB_DISABLE_XET']='1'
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING']='1'
os.environ['OPENBLAS_NUM_THREADS']='4'
os.environ['TOKENIZERS_PARALLELISM']='false'
os.environ['WANDB_DISABLED']='true'
import numpy as np
import pandas as pd
import torch
from torch.utils.data import DataLoader, TensorDataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers.utils import logging
logging.set_verbosity_error()

from paths import ROOT, LOCAL
sys.path.insert(0,str(ROOT/'synth'))
from benchmark import load_real, score, DEADLINE
from scripts.rules import CATS

def evaluate(model, tokenizer, frame):
    model.eval()
    output=[]
    with torch.inference_mode(), torch.autocast('cuda',dtype=torch.float16):
        for start in range(0,len(frame),32):
            batch=tokenizer(frame.message.iloc[start:start+32].astype(str).tolist(),truncation=True,padding=True,max_length=96,return_tensors='pt').to('cuda')
            output.extend(model(**batch).logits.argmax(-1).cpu().tolist())
    return np.asarray([CATS[i] for i in output])

def fit(training,validation,tag,epochs=2):
    random.seed(902)
    np.random.seed(902)
    torch.manual_seed(902)
    torch.cuda.manual_seed_all(902)
    torch.set_num_threads(6)
    meta=json.loads((LOCAL/'transformer_source.json').read_text())
    pretrained=LOCAL/'public_pretrained'
    tokenizer=AutoTokenizer.from_pretrained(pretrained,local_files_only=True)
    model=AutoModelForSequenceClassification.from_pretrained(pretrained,local_files_only=True,num_labels=len(CATS),id2label=dict(enumerate(CATS)),label2id={c:i for i,c in enumerate(CATS)}).to('cuda')
    training=training[training.bank.ne('ADIB')].sample(frac=1,random_state=902)
    encoded=tokenizer(training.message.astype(str).tolist(),truncation=True,padding='max_length',max_length=96,return_tensors='pt')
    labels=torch.tensor([CATS.index(c) for c in training.label])
    dataset=TensorDataset(encoded['input_ids'],encoded['attention_mask'],labels)
    loader=DataLoader(dataset,batch_size=16,shuffle=True,generator=torch.Generator().manual_seed(902))
    optimizer=torch.optim.AdamW(model.parameters(),lr=2e-5,weight_decay=0.01)
    scaler=torch.amp.GradScaler('cuda')
    best=-1
    checkpoint=LOCAL/'transformer_models'/tag
    checkpoint.mkdir(parents=True,exist_ok=True)
    for epoch in range(epochs):
        model.train()
        total=0
        for input_ids,mask,gold in loader:
            if datetime.now(timezone.utc)>=DEADLINE:
                raise TimeoutError('Dubai deadline reached; checkpoints remain local')
            optimizer.zero_grad(set_to_none=True)
            with torch.autocast('cuda',dtype=torch.float16):
                loss=model(input_ids=input_ids.to('cuda'),attention_mask=mask.to('cuda'),labels=gold.to('cuda')).loss
            scaler.scale(loss).backward()
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(),1.0)
            scaler.step(optimizer)
            scaler.update()
            total+=loss.item()
        predicted=evaluate(model,tokenizer,validation)
        metric=score(validation.label,predicted)
        print(json.dumps({'tag':tag,'epoch':epoch+1,'loss':total/len(loader),'validation_macro_f1':metric['macro_f1']}),flush=True)
        if metric['macro_f1']>best:
            best=metric['macro_f1']
            model.save_pretrained(checkpoint)
            tokenizer.save_pretrained(checkpoint)
            (checkpoint/'validation.json').write_text(json.dumps(metric,indent=2))
    del model, optimizer, scaler
    gc.collect()
    torch.cuda.empty_cache()
    return json.loads((checkpoint/'validation.json').read_text())

def validation_run():
    if not torch.cuda.is_available():
        print('No CUDA GPU; optional transformer skipped')
        return
    real=load_real()
    training=real[(real.partition=='train') & real.bank.ne('ADIB')]
    validation=real[real.partition=='validation']
    results=[]
    for round_number in (2,3):
        synthetic=pd.read_json(LOCAL/f'round_{round_number}_synthetic.jsonl',lines=True)
        synthetic=synthetic[synthetic.label.isin(CATS)].sample(n=min(12000,sum(synthetic.label.isin(CATS))),random_state=902)
        for setup in ('real_only','real_plus_synthetic','synthetic_only'):
            tag=f'round{round_number}_{setup}'
            if round_number==3 and setup=='real_only':
                item=dict(results[0],round=3,cached=True)
                results.append(item)
                continue
            data=training if setup=='real_only' else synthetic if setup=='synthetic_only' else pd.concat([training,synthetic],ignore_index=True)
            metrics=fit(data,validation,tag)
            results.append({'round':round_number,'setup':setup,'tag':tag,'model':'distilmbert_sms','train_n':len(data),'metrics':metrics})
            (LOCAL/'transformer_results.json').write_text(json.dumps(results,indent=2))

def final_run():
    path=LOCAL/'transformer_final.json'
    if path.exists():
        print('Transformer final evaluation already exists')
        return
    results=json.loads((LOCAL/'transformer_results.json').read_text())
    real=load_real()
    test=real[real.partition=='test']
    output=[]
    for setup in ('real_only','real_plus_synthetic','synthetic_only'):
        item=max((r for r in results if r['setup']==setup),key=lambda r:r['metrics']['macro_f1'])
        checkpoint=LOCAL/'transformer_models'/item['tag']
        tokenizer=AutoTokenizer.from_pretrained(checkpoint,local_files_only=True)
        model=AutoModelForSequenceClassification.from_pretrained(checkpoint,local_files_only=True).to('cuda')
        prediction=evaluate(model,tokenizer,test)
        output.append({'setup':setup,'model':'distilmbert_sms','selected_round':item['round'],'test':score(test.label,prediction),
                       'note':'Checkpoint trained on train partition only; validation selects epoch/configuration; no refit on validation.'})
        del model
        gc.collect()
        torch.cuda.empty_cache()
    path.write_text(json.dumps(output,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--final',action='store_true')
    args=parser.parse_args()
    if args.final: final_run()
    else: validation_run()
