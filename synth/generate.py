"""Reproducible public-only synthetic SMS; private templates require an explicit local path."""
import argparse
from datetime import datetime, timedelta
import hashlib
import json
from pathlib import Path
import random
import re
import sys
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.rules import CATS

VERSION = '1.0.0'
# Independently authored illustrative text. No claim of authentic bank-specific wording.
TEMPLATES = [
 ('purchase_en_1','purchase','en','Card {last4}: payment {currency} {amount} at {merchant} on {date}. Balance {currency} {bal}.'),
 ('purchase_en_2','purchase','en','{bank} purchase alert. Merchant: {merchant}. Amount: {currency} {amount}. Card: ****{last4}. Date: {date}.'),
 ('purchase_en_3','purchase','en','You paid {currency} {amount} to {merchant} using card {last4}. Remaining balance {bal}.'),
 ('purchase_ar_1','purchase','ar','عملية شراء بمبلغ {amount} {currency} لدى {merchant} بالبطاقة المنتهية بـ {last4}. الرصيد {bal}. التاريخ {date}'),
 ('purchase_mixed_1','purchase','mixed','شراء Card {last4}: {currency} {amount} at {merchant}. الرصيد المتاح {bal}'),
 ('bill_en_1','bill_payment','en','Bill paid to {merchant}: {currency} {amount} from account ****{last4} on {date}. Balance {bal}.'),
 ('refund_en_1','refund','en','Refund from {merchant}: {currency} {amount} returned to card {last4} on {date}. Balance {bal}.'),
 ('decline_en_1','declined','en','Payment attempt of {currency} {amount} at {merchant} declined. Card {last4}. No funds debited.'),
 ('atm_en_1','ATM','en','ATM cash withdrawal {currency} {amount}, card {last4}, {date}. Balance {bal}.'),
 ('transfer_out_en_1','transfer_out','en','Transfer sent: {currency} {amount} to beneficiary {person}. Ref {reference}. Account ****{last4}. Balance {bal}.'),
 ('transfer_in_en_1','transfer_in','en','Incoming transfer: {currency} {amount} from {person}. Ref {reference}. Balance {bal}.'),
 ('salary_en_1','salary','en','Salary credited: {currency} {amount}. Employer {person}. Account ****{last4}. Available {bal}.'),
 ('otp_en_1','OTP','en','Verification code {otp} for card {last4}. Never share this code.'),
 ('promo_en_1','promo','en','Discover this month offers from {bank}. Visit your banking app for details.'),
 ('statement_en_1','statement','en','Your {bank} statement for {date} is ready in your banking app.'),
 ('balance_en_1','balance','en','Balance enquiry for account ****{last4}: {currency} {bal} on {date}.'),
 ('standing_en_1','standing_order','en','Standing order processed: {currency} {amount} to {person}. Reference {reference}.')
]

# Engineering priors, not empirical transaction quantiles. Public tariff anchors are in the report.
RANGES = dict(zip(CATS, [(8,500),(10,1200),(2,2500),(5,8000),(20,3000),(10,10000),
                        (100,15000),(10,1500),(10,10000),(50,50000),(5,600),(5,5000)]))
BANKS = ['ADCB','Liv','Emirates NBD','Mashreq','FAB','DIB','Emirates Islamic','ADIB','RAKBANK','CBD','HSBC UAE','Wio',
         'Al Rajhi','SNB','QNB','NBK','BBK','Bank Muscat']

def descriptor_variant(value, rng, level):
    if level == 0:
        return value
    options = [value, value.lower(),value.upper(),value[:rng.choice([14,18,22])],
               value+' '+rng.choice(['DUBAI','ABU DHABI','SHARJAH','DOHA','RIYADH']),
               value+' '+str(rng.randint(1,399)),rng.choice(['PAYPAL *','CHECKOUT.COM*','SQ *'])+value]
    return rng.choice(options)

def generate(count=20000, seed=902, level=1, private_templates=None, weights=None):
    rng, nrng = random.Random(seed), np.random.default_rng(seed)
    gaz = pd.read_csv(ROOT/'synth/gazetteer/merchants.csv',keep_default_na=False)
    gaz = gaz[gaz.training_eligible.astype(str).str.lower()=='true']
    by_class = {c:g.to_dict('records') for c,g in gaz.groupby('category')}
    templates = list(TEMPLATES)
    private_ids = set()
    if private_templates:
        path = Path(private_templates).resolve()
        if ROOT.joinpath('synth/local').resolve() not in path.parents:
            raise ValueError('Private template path must be under ignored synth/local')
        for item in json.loads(path.read_text(encoding='utf-8')):
            templates.append(tuple(item))
            private_ids.add(item[0])
    purchases = [x for x in templates if x[1]=='purchase']
    auxiliary = [x for x in templates if x[1]!='purchase']
    results = []
    for index in range(count):
        category = rng.choices(CATS,weights=[(weights or {}).get(c,1) for c in CATS])[0]
        business = rng.choice(by_class[category])
        template = rng.choice(purchases) if rng.random()<0.82 else rng.choice(auxiliary)
        tid, kind, language, pattern = template
        if kind=='bill_payment' and category!='Utilities_Telecom':
            category='Utilities_Telecom'
            business=rng.choice(by_class[category])
        low, high = RANGES[category]
        amount = float(np.clip(nrng.lognormal(np.log(np.sqrt(low*high)),0.85),low,high))
        bank = rng.choice(BANKS)
        currency = rng.choices(['AED','USD','EUR','SAR','GBP'],weights=[92,3,1,3,1])[0]
        merchant = descriptor_variant(business['descriptor'],rng,level)
        if level>=2 and rng.random()<0.1 and len(merchant)>5:
            position = rng.randint(1,len(merchant)-2)
            merchant = merchant[:position]+merchant[position+1:]
        values = dict(bank=bank,last4=f'{rng.randint(0,9999):04}',currency=currency,amount=f'{amount:.2f}',
                      merchant=merchant,date=(datetime(2025,1,1)+timedelta(days=rng.randint(0,364))).strftime('%d/%m/%Y'),
                      bal=f'{rng.uniform(100,90000):.2f}',person='SYNTHETIC BENEFICIARY',reference=f'SYNTH{index:08}',otp=f'{rng.randint(0,999999):06}')
        message = pattern.format(**values)
        if currency!='AED' and kind=='purchase' and rng.random()<0.5:
            message += f' FX conversion applies; billed in AED.'
        if level>=2 and rng.random()<0.08:
            message = message.replace(' ','  ') if rng.random()<0.5 else message.replace(' ','',1)
        if level>=3 and rng.random()<0.05:
            message=message[:rng.randint(max(20,len(message)//2),len(message))]
        is_expense = kind in ('purchase','bill_payment')
        label=category if is_expense else ('NON_TXN' if kind in ('OTP','promo','statement','balance') else 'TXN_OTHER')
        amount_aed=amount*{'AED':1,'USD':3.6725,'EUR':4.0,'SAR':0.9793,'GBP':4.7}[currency]
        results.append(dict(row_id=f'synthetic-{seed}-{index}',message=message,label=label,category=category,
                    message_type=kind,is_expense=is_expense,merchant=merchant,brand=business['brand'],
                    bank=bank,template_id=tid,language=language,amount=amount,amount_aed=amount_aed,
                    generator_version=VERSION,seed=seed,source=business['source'],
                    template_provenance='private_derived' if tid in private_ids else 'independently_authored_illustrative',
                    public_eligible=tid not in private_ids))
    return pd.DataFrame(results)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--rows',type=int,default=20000)
    parser.add_argument('--seed',type=int,default=902)
    parser.add_argument('--level',type=int,default=1,choices=[0,1,2,3])
    parser.add_argument('--output',default='synth/out/synthetic_public.csv')
    parser.add_argument('--private-templates')
    args=parser.parse_args()
    target=(ROOT/args.output).resolve()
    if ROOT not in target.parents:
        raise ValueError('Output must be inside project')
    if args.private_templates and ROOT.joinpath('synth/local').resolve() not in target.parents:
        raise ValueError('Private-derived output must remain in synth/local')
    frame=generate(args.rows,args.seed,args.level,args.private_templates)
    target.parent.mkdir(parents=True,exist_ok=True)
    frame.to_csv(target,index=False)
    print('Generated rows:',len(frame),'; public eligible:',bool(frame.public_eligible.all()))

if __name__=='__main__':
    main()
