"""Benchmark iteration on validation only, then one final frozen real-test evaluation."""
import argparse
import gc
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import warnings
os.environ.setdefault('OMP_NUM_THREADS','8')
os.environ.setdefault('MKL_NUM_THREADS','8')
os.environ['OPENBLAS_NUM_THREADS']='4'
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, f1_score, classification_report
from sklearn.pipeline import Pipeline
from threadpoolctl import threadpool_limits

ROOT=Path(__file__).resolve().parents[1]
LOCAL=ROOT/'synth/local'
sys.path.insert(0,str(ROOT))
sys.path.insert(0,str(ROOT/'synth'))
from scripts.categoriser_lib import add_features, tfidf_logreg
from scripts.rules import CATS
from generate import generate, TEMPLATES

DEADLINE=datetime(2026,11,9,3,0,tzinfo=timezone.utc)

def load_real():
    manifest=json.loads((LOCAL/'frozen.json').read_text(encoding='utf-8'))
    path=LOCAL/'real.jsonl'
    if hashlib.sha256(path.read_bytes()).hexdigest()!=manifest['table_hash']:
        raise ValueError('Frozen real table changed')
    real=pd.read_json(path,lines=True)
    assert dict(zip(real.row_id,real.partition))==manifest['members']
    return real

def features(frame, family):
    return add_features(frame) if family=='ledger' else frame.message.fillna('')

def _fit_predict(train, evaluation, family):
    gc.collect()
    # ADIB's dataset license is unresolved; prevent its use in training in every setup.
    train=train[train.bank.ne('ADIB')].copy()
    if train.label.nunique()<2:
        raise ValueError('Insufficient classes in training')
    model=tfidf_logreg() if family=='ledger' else Pipeline([
        ('tfidf',TfidfVectorizer(analyzer='char',ngram_range=(2,5),sublinear_tf=True,min_df=2,max_features=80000)),
        ('classifier',LogisticRegression(C=2,class_weight='balanced',max_iter=1500))])
    with threadpool_limits(limits=8), warnings.catch_warnings(record=True) as caught:
        model.fit(features(train,family),train.label)
        prediction=model.predict(features(evaluation,family))
    convergence=[type(item.message).__name__ for item in caught]
    del model
    gc.collect()
    return prediction, convergence

def fit_predict(train, evaluation, family):
    # Isolate each fit so Windows releases all vectorizer/optimizer allocations.
    work=LOCAL/'worker'
    work.mkdir(exist_ok=True)
    train.to_pickle(work/'train.pkl')
    evaluation.to_pickle(work/'evaluation.pkl')
    subprocess.run([sys.executable,str(Path(__file__).resolve()),'--worker',family],cwd=ROOT,check=True)
    response=json.loads((work/'response.json').read_text())
    return np.asarray(response['prediction']),response['warnings']

def score(truth,prediction):
    report=classification_report(truth,prediction,labels=CATS,output_dict=True,zero_division=0)
    return {'macro_f1':f1_score(truth,prediction,labels=CATS,average='macro',zero_division=0),
            'accuracy':float(np.mean(np.asarray(truth)==prediction)),
            'per_class':{c:report[c] for c in CATS},
            'confusion_matrix':confusion_matrix(truth,prediction,labels=CATS).tolist(),
            'class_order':CATS,'n':len(truth)}

def mine_templates(train):
    import re
    allowed=set(re.findall(r'[A-Za-z]+',' '.join(x[3] for x in TEMPLATES).lower()))
    allowed.update('purchase debit credit ending available avl bal balance is with at on card no amount account used for was cr limit bill payment has been debited from acc approved trx transaction thank you using debitcard creditcard'.split())
    templates={}
    for record in train[train.bank.ne('ADIB')].itertuples():
        text=record.message
        raw=record.merchant_raw
        if not isinstance(raw,str) or not raw:
            continue
        text=text.replace(raw,'{merchant}')
        # Remove every digit-bearing token before allowing only generic public grammar words.
        text=re.sub(r'\S*\d\S*','{reference}',text)
        text=re.sub(r'\b[A-Za-z]+\b',lambda m:m.group(0) if m.group(0).lower() in allowed or m.group(0) in ('merchant','reference') else '{person}',text)
        text=re.sub(r'[^\x00-\x7f]',' ',text)
        text=re.sub(r'(?:\{person\}\s*){2,}','{person} ',text)
        text=re.sub(r'\s+',' ',text).strip()
        # Add amount/card/balance fields with synthetic values, never values mined from messages.
        text += ' Amount {currency} {amount}. Card {last4}. Balance {bal}.'
        if text not in templates:
            templates[text]=(f'private_train_{len(templates):04}','purchase','en',text)
    path=LOCAL/'private_templates.json'
    path.write_text(json.dumps(list(templates.values()),indent=2),encoding='utf-8')
    return path

def error_summary(evaluation,prediction):
    wrong=evaluation[evaluation.label.to_numpy()!=prediction].copy()
    wrong['predicted']=np.asarray(prediction)[evaluation.label.to_numpy()!=prediction]
    pairs=wrong.groupby(['label','predicted']).size().sort_values(ascending=False).head(20)
    # Only class names/counts may be published. Private merchant hashes are local-only.
    return [{'truth':a,'prediction':b,'count':int(n)} for (a,b),n in pairs.items()]

def commit_round(round_number):
    # Explicit allowlist: no private-derived artifacts can be staged by this command.
    subprocess.run(['git','status','--short'],cwd=ROOT,check=True)
    subprocess.run(['git','add','synth/ROUNDS.md','synth/benchmark.py'],cwd=ROOT,check=True)
    staged=subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT,text=True).splitlines()
    if any(p.startswith(('data/','synth/local/','synth/out/private')) for p in staged):
        raise ValueError('Private path staged')
    subprocess.run(['git','commit','-m',f'Benchmark round {round_number}: validation metrics and generator decisions'],cwd=ROOT,check=True)

def append_round(number,rows,results,notes):
    path=ROOT/'synth/ROUNDS.md'
    if not path.exists():
        path.write_text('# Synthetic SMS benchmark rounds\n\nAll iteration metrics below use validation, never the frozen test set. Macro-F1 averages all 12 classes with zero for absent classes. Real-only estimates are cached when training data is unchanged.\n\n',encoding='utf-8')
    with path.open('a',encoding='utf-8') as out:
        out.write(f'## Round {number}\n\nSynthetic rows generated: {rows:,}. {notes}\n\n')
        out.write('| Model | Training | Validation macro-F1 | Accuracy | Train rows |\n|---|---|---:|---:|---:|\n')
        for item in results:
            out.write(f"| {item['model']} | {item['setup']} | {item['metrics']['macro_f1']:.4f} | {item['metrics']['accuracy']:.4f} | {item['train_n']} |\n")
        out.write('\nPer-class scores, confusion matrices, class-pair errors and split membership are in ignored `synth/local/`.\n\n')

def run(rounds=3,commit=False,final=False):
    real=load_real()
    train=real[(real.partition=='train') & real.bank.ne('ADIB')]
    validation=real[real.partition=='validation']
    templates=mine_templates(train)
    if (LOCAL/'results.json').exists():
        all_results=json.loads((LOCAL/'results.json').read_text(encoding='utf-8'))
        base=[r for r in all_results if r['round']==0]
    else:
        all_results=[]
        base=[]
        for family in ('ledger','char_sms'):
            prediction,notes=fit_predict(train,validation,family)
            item={'round':0,'model':family,'setup':'real_only','train_n':len(train),'metrics':score(validation.label,prediction),'warnings':notes,'errors':error_summary(validation,prediction)}
            base.append(item)
        all_results.extend(base)
        append_round(0,0,base,f'Real train {len(train):,}; validation {len(validation):,}; frozen test {sum(real.partition=="test"):,}. Strict template groups; unresolved-license ADIB excluded from training. Labels are inherited merchant-level project annotations; historical row overrides are not reapplied.')
        (LOCAL/'results.json').write_text(json.dumps(all_results,indent=2),encoding='utf-8')
        if commit: commit_round(0)
    weights=None
    best_scores=[]
    for number in range(1,rounds+1):
        if any(r['round']==number for r in all_results):
            chosen=max((r for r in all_results if r['round']==number and r['setup']=='real_plus_synthetic'),key=lambda x:x['metrics']['macro_f1'])
            best_scores.append(chosen['metrics']['macro_f1'])
            weights=json.loads((LOCAL/f'round_{number}_weights.json').read_text())
            continue
        if datetime.now(timezone.utc)>=DEADLINE:
            break
        size=[20000,30000,40000,60000,80000,100000,150000,200000][number-1]
        generated=generate(size,seed=902+number,level=min(number,3),private_templates=templates if number>=2 else None,weights=weights)
        generated.to_json(LOCAL/f'round_{number}_synthetic.jsonl',orient='records',lines=True,force_ascii=False)
        synthetic=generated[generated.label.isin(CATS)]
        progress=LOCAL/f'round_{number}_progress.json'
        result=json.loads(progress.read_text()) if progress.exists() else [dict(baseline,round=number,cached=True) for baseline in base]
        for family in ('ledger','char_sms'):
            for setup,training in [('real_plus_synthetic',pd.concat([train,synthetic],ignore_index=True)),('synthetic_only',synthetic)]:
                if any(item['model']==family and item['setup']==setup for item in result):
                    continue
                prediction,notes=fit_predict(training,validation,family)
                result.append({'round':number,'model':family,'setup':setup,'train_n':int(sum(training.bank!='ADIB')),'metrics':score(validation.label,prediction),'warnings':notes,'errors':error_summary(validation,prediction)})
                (LOCAL/f'round_{number}_progress.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
                print(f'Round {number}: {family}/{setup} complete',flush=True)
        all_results.extend(result)
        chosen=max((x for x in result if x['setup']=='real_plus_synthetic'),key=lambda x:x['metrics']['macro_f1'])
        # Class-level validation feedback only; never inspect real test merchant/template errors.
        weights={c:1+2*(1-chosen['metrics']['per_class'][c]['f1-score']) for c in CATS}
        (LOCAL/f'round_{number}_weights.json').write_text(json.dumps(weights),encoding='utf-8')
        best_scores.append(chosen['metrics']['macro_f1'])
        notes=['Public authored formats; baseline descriptor variation.',
               'Adds conservative train-only masked private formats, class reweighting, typos and odd spacing.',
               'Adds truncated messages and updated validation-class reweighting.'][min(number-1,2)]
        append_round(number,size,result,notes)
        (LOCAL/'results.json').write_text(json.dumps(all_results,indent=2),encoding='utf-8')
        if commit: commit_round(number)
        if len(best_scores)>=3 and best_scores[-1]-best_scores[-2]<0.005 and best_scores[-2]-best_scores[-3]<0.005:
            break
    if final:
        finalize(all_results)
    print('Validation rounds complete:',max(x['round'] for x in all_results),flush=True)

def finalize(results=None):
    if (LOCAL/'final_results.json').exists():
        print('Final results already exist; refusing to reopen test set.')
        return
    results=results or json.loads((LOCAL/'results.json').read_text(encoding='utf-8'))
    real=load_real()
    development=real[real.partition!='test']
    test=real[real.partition=='test']
    output=[]
    for family in ('ledger','char_sms'):
        for setup in ('real_only','real_plus_synthetic','synthetic_only','public_synthetic_only'):
            if setup=='real_only':
                chosen=0
                synthetic=None
            elif setup=='public_synthetic_only':
                chosen='public'
                synthetic=pd.read_csv(ROOT/'synth/out/synthetic_public.csv')
                synthetic=synthetic[synthetic.label.isin(CATS)]
            else:
                chosen=max((x for x in results if x['model']==family and x['setup']==setup),key=lambda x:x['metrics']['macro_f1'])['round']
                synthetic=pd.read_json(LOCAL/f'round_{chosen}_synthetic.jsonl',lines=True)
                synthetic=synthetic[synthetic.label.isin(CATS)]
            training=development if setup=='real_only' else synthetic if setup in ('synthetic_only','public_synthetic_only') else pd.concat([development,synthetic],ignore_index=True)
            prediction,notes=fit_predict(training,test,family)
            row={'model':family,'setup':setup,'selected_round':chosen,'test':score(test.label,prediction),'warnings':notes,'leave_one_bank_out':{}}
            for bank in sorted(real.bank.unique()):
                bank_test=real[real.bank==bank]
                # LOBO is an independent fixed-generator experiment, not a test of the
                # globally selected validation configuration (which has seen this bank).
                public=pd.read_csv(ROOT/'synth/out/synthetic_public.csv')
                public=public[public.label.isin(CATS) & public.bank.ne(bank)]
                other_real=real[(real.bank!=bank) & real.bank.ne('ADIB')]
                bank_train=other_real if setup=='real_only' else public if setup in ('synthetic_only','public_synthetic_only') else pd.concat([other_real,public],ignore_index=True)
                bank_train=bank_train[~bank_train.get('template_group',pd.Series(index=bank_train.index,dtype=str)).isin(bank_test.template_group)]
                pred,warn=fit_predict(bank_train,bank_test,family)
                row['leave_one_bank_out'][bank]=score(bank_test.label,pred)
            output.append(row)
            (LOCAL/'final_progress.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
    (LOCAL/'final_results.json').write_text(json.dumps(output,indent=2),encoding='utf-8')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--rounds',type=int,default=3,choices=range(1,9))
    parser.add_argument('--commit-rounds',action='store_true')
    parser.add_argument('--final',action='store_true')
    parser.add_argument('--final-only',action='store_true')
    parser.add_argument('--worker',choices=['ledger','char_sms'])
    args=parser.parse_args()
    if args.worker:
        train=pd.read_pickle(LOCAL/'worker/train.pkl')
        evaluation=pd.read_pickle(LOCAL/'worker/evaluation.pkl')
        prediction,notes=_fit_predict(train,evaluation,args.worker)
        (LOCAL/'worker/response.json').write_text(json.dumps({'prediction':prediction.tolist(),'warnings':notes}))
    elif args.final_only:
        finalize()
    else:
        run(args.rounds,args.commit_rounds,args.final)
