"""Separate event filter diagnostic; real labels are parser-derived silver, not gold."""
import json
from pathlib import Path
import re
import sys
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from threadpoolctl import threadpool_limits
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'synth'))
from generate import generate

def run():
    synthetic=generate(20000,seed=1902,level=1)
    synthetic['event_label']=np.where(synthetic.is_expense,'EXPENSE',synthetic.label)
    train,test=train_test_split(synthetic,test_size=.2,stratify=synthetic.event_label,random_state=902)
    model=make_pipeline(TfidfVectorizer(analyzer='char',ngram_range=(2,5),max_features=40000,min_df=2),LogisticRegression(max_iter=1000,class_weight='balanced'))
    with threadpool_limits(limits=4):
        model.fit(train.message,train.event_label)
        output={'synthetic_holdout':classification_report(test.event_label,model.predict(test.message),output_dict=True,zero_division=0)}
        real=pd.read_json(ROOT/'synth/local/all_messages.jsonl',lines=True).drop_duplicates('exact_hash')
        real['event_label']=real.txn_type.map({'otp':'NON_TXN','purchase':'EXPENSE','bill_payment':'EXPENSE','refund':'TXN_OTHER','cash_withdrawal':'TXN_OTHER','income':'TXN_OTHER','transfer_in':'TXN_OTHER','transfer_out':'TXN_OTHER','declined':'TXN_OTHER'})
        real=real[real.event_label.notna()]
        output['real_silver_diagnostic']=classification_report(real.event_label,model.predict(real.message),output_dict=True,zero_division=0)
    output['warning']='Real event labels are inherited from the existing parser and are not independently annotated. This is a silver-label diagnostic, not a gold benchmark or evidence of production filtering accuracy.'
    (ROOT/'synth/local/filter_results.json').write_text(json.dumps(output,indent=2))
    print('Separate filter diagnostic saved; real labels explicitly marked silver.')

if __name__=='__main__':
    run()
