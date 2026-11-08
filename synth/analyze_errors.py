"""Local validation error diagnostics, public-name allowlist, no raw SMS output."""
import hashlib
import json
from pathlib import Path
import sys
import pandas as pd
from paths import ROOT, LOCAL
sys.path.insert(0,str(ROOT/'synth'))
from benchmark import load_real, fit_predict, score
from scripts.rules import CATS

def run():
    real=load_real()
    train=real[(real.partition=='train') & real.bank.ne('ADIB')]
    validation=real[real.partition=='validation']
    gaz=pd.read_csv(ROOT/'synth/gazetteer/merchants.csv',keep_default_na=False)
    allowed={v.casefold() for c in ('brand','descriptor') for v in gaz[c]}
    completed=json.loads((LOCAL/'results.json').read_text())
    target=LOCAL/'validation_errors'
    target.mkdir(exist_ok=True)
    for number in sorted({r['round'] for r in completed if r['round']>0}):
        synthetic=pd.read_json(LOCAL/f'round_{number}_synthetic.jsonl',lines=True)
        synthetic=synthetic[synthetic.label.isin(CATS)]
        for family in ('ledger','char_sms'):
            path=target/f'round_{number}_{family}.json'
            if path.exists():continue
            training=pd.concat([train,synthetic],ignore_index=True)
            prediction,warnings=fit_predict(training,validation,family)
            rows=[]
            for record,pred in zip(validation.itertuples(),prediction):
                if record.label==pred:continue
                merchant=record.merchant_clean if record.merchant_clean.casefold() in allowed else '{merchant}'
                rows.append({'truth':record.label,'prediction':pred,'merchant':merchant,
                             'merchant_id':hashlib.sha256(record.merchant_clean.encode()).hexdigest(),
                             'template_id':record.template_group,'bank':record.bank})
            pairs=pd.DataFrame(rows).groupby(['truth','prediction']).size().sort_values(ascending=False).head(20)
            expected=next(r for r in completed if r['round']==number and r['model']==family and r['setup']=='real_plus_synthetic')['metrics']['macro_f1']
            measured=score(validation.label,prediction)['macro_f1']
            path.write_text(json.dumps({'round':number,'family':family,'class_pairs':[{'truth':a,'prediction':b,'count':int(n)} for (a,b),n in pairs.items()],
                'masked_merchant_template_errors':rows,'warnings':warnings,'original_validation_macro_f1':expected,'replayed_validation_macro_f1':measured,
                'generator_changed':False,'note':'Post-run diagnostic replay; final test never inspected for generator changes. Public-name allowlist; raw SMS and numeric values omitted.'},indent=2))
            print('Saved masked validation error diagnostics:',number,family,flush=True)

if __name__=='__main__':run()
