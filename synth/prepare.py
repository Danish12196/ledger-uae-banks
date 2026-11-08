"""Local-only ingestion using the existing notebook parser, never displaying SMS."""
import ast
import hashlib
import json
from pathlib import Path
import re
import sys
import warnings
import numpy as np
import pandas as pd
from sklearn.model_selection import GroupShuffleSplit

from paths import ROOT, LOCAL, PRIVATE
sys.path.insert(0, str(ROOT))
from scripts.rules import CATS

def notebook_helpers():
    notebook = json.loads((ROOT / 'sms_transactions_pipeline.ipynb').read_text(encoding='utf-8'))
    env = {'np': np, 'pd': pd, 're': re}
    # Only declarations in parser/merchant-cleaning cells; never execute notebook I/O or displays.
    for cell_index in (8, 14):
        tree = ast.parse(''.join(notebook['cells'][cell_index]['source']))
        keep = []
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.Assign, ast.AnnAssign)):
                targets = [t.id for t in getattr(node, 'targets', []) if isinstance(t, ast.Name)]
                if any(t in {'df', 'split', 'no_name', 'is_xfer', 'before'} for t in targets):
                    break
                keep.append(node)
        exec(compile(ast.Module(body=keep, type_ignores=[]), '<ledger-public-helpers>', 'exec'), env)
    return env

def digest(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def fingerprint(message, merchant_raw=None):
    text = str(message).lower()
    if merchant_raw:
        text = text.replace(str(merchant_raw).lower(), ' {merchant} ')
    text = re.sub(r'\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b', '{email}', text)
    text = re.sub(r'https?://\S+', '{url}', text)
    text = re.sub(r'\d[\d,.:/\-]*', '{number}', text)
    text = re.sub(r'[^a-z{}\u0600-\u06ff]+', ' ', text)
    return digest(re.sub(r'\s+', ' ', text).strip())

def run():
    LOCAL.mkdir(parents=True, exist_ok=True)
    if (LOCAL / 'frozen.json').exists():
        print('Frozen manifest already exists; refusing to replace splits.')
        return
    env = notebook_helpers()
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        labels = pd.read_excel(PRIVATE / 'merchant_labels.xlsx', sheet_name='Merchants')
    if not set(labels.final_category.dropna()).issubset(CATS):
        raise ValueError('Gold label workbook must use the 12-class scheme; no automatic remapping.')
    label_map = dict(zip(labels.merchant, labels.final_category))
    rows = []
    for source in sorted(PRIVATE.glob('*.xlsx')):
        if source.name == 'merchant_labels.xlsx':
            continue
        name = source.name.lower()
        bank = next((b for token, b in [('adcb','ADCB'), ('adib','ADIB'), ('fab','FAB'), ('liv','Liv')] if token in name), 'Mashreq')
        for sheet, frame in pd.read_excel(source, sheet_name=None).items():
            message_col = next((c for c in frame if str(c).lower() in ('message','sms')), None)
            if not message_col:
                continue
            date_col = next(c for c in frame if str(c).lower().startswith('date'))
            sender_col = next((c for c in frame if str(c).lower() in ('sender','bank')), None)
            for index, record in frame.iterrows():
                message = str(record[message_col]).strip()
                if message.lower() in ('nan','none',''):
                    continue
                parsed = env['parse_message'](message, bank)
                merchant = env['split_merchant'](parsed['merchant_raw'], bank)[0]
                canonical = env['clean_name'](merchant)
                row = {'row_id': digest(f'{source.name}|{sheet}|{index}'), 'bank': bank,
                       'sender': str(record[sender_col]) if sender_col else bank,
                       'date': str(record[date_col]), 'message': message, 'merchant': merchant or '',
                       'merchant_clean': canonical or '', 'label': label_map.get(canonical),
                       'source_file': source.name, 'source_sheet': sheet, 'source_row': index + 2,
                       'label_provenance': 'existing_12_class_merchant_workbook', **parsed}
                row['amount_aed'] = parsed['amount'] * {'AED':1,'USD':3.6725,'SAR':0.9793,'QAR':1.009,'BHD':9.767,'OMR':9.551}.get(parsed['currency'], np.nan)
                row['template_group'] = fingerprint(message, parsed['merchant_raw'])
                row['exact_hash'] = digest(message)
                row['near_hash'] = digest(row['template_group'] + '|' + str(canonical).lower())
                row['expense'] = parsed['txn_type'] in ('purchase','bill_payment') and not env['TRANSFER_MERCHANTS'].search(parsed['merchant_raw'] or '')
                rows.append(row)
    full = pd.DataFrame(rows)
    # Exact duplicated messages and masked duplicates of the same merchant are one observation.
    dedup = full.drop_duplicates('exact_hash').drop_duplicates('near_hash').reset_index(drop=True)
    labelled = dedup[dedup.expense & dedup.label.isin(CATS)].copy().reset_index(drop=True)
    if len(labelled) < 100:
        raise ValueError('Insufficient labelled real expenses')
    # Use strict bank-message template groups, with the merchant fully removed. Whole groups stay together.
    candidates = GroupShuffleSplit(n_splits=100, test_size=0.2, random_state=902)
    train_index, test_index = min(candidates.split(labelled, groups=labelled.template_group),
                                key=lambda pair: (12-labelled.iloc[pair[0]].label.nunique()) * 100 + abs(len(pair[1])/len(labelled)-0.2))
    development = labelled.iloc[train_index]
    inner = GroupShuffleSplit(n_splits=100, test_size=0.2, random_state=903)
    a, b = min(inner.split(development, groups=development.template_group),
               key=lambda pair: (12-development.iloc[pair[0]].label.nunique()) * 100 + abs(len(pair[1])/len(development)-0.2))
    labelled['partition'] = 'test'
    labelled.loc[development.iloc[a].index, 'partition'] = 'train'
    labelled.loc[development.iloc[b].index, 'partition'] = 'validation'
    assert not set(labelled[labelled.partition=='train'].template_group) & set(labelled[labelled.partition!='train'].template_group)
    assert not set(labelled[labelled.partition=='test'].template_group) & set(labelled[labelled.partition!='test'].template_group)
    full.to_json(LOCAL / 'all_messages.jsonl', orient='records', lines=True, force_ascii=False)
    labelled.to_json(LOCAL / 'real.jsonl', orient='records', lines=True, force_ascii=False)
    manifest = {'seed':902, 'split_method':'strict_masked_template_group_holdout',
                'input_hashes': {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in PRIVATE.glob('*.xlsx')},
                'members':dict(zip(labelled.row_id,labelled.partition)),
                'table_hash':hashlib.sha256((LOCAL/'real.jsonl').read_bytes()).hexdigest()}
    (LOCAL/'frozen.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    summary = {'messages':len(full),'exact_unique':full.exact_hash.nunique(),'near_unique':len(dedup),
               'labelled_expenses':len(labelled),'unlabelled_expenses':int((dedup.expense & dedup.label.isna()).sum()),
               'template_groups':labelled.template_group.nunique(),
               'partitions':labelled.partition.value_counts().to_dict(),
               'class_counts':pd.crosstab(labelled.label,labelled.partition).to_dict(),
               'bank_counts':pd.crosstab(labelled.bank,labelled.partition).to_dict(),
               'row_overrides':'The supplied newer workbook has zero explicit row overrides; merchant-level annotations are used.'}
    (LOCAL/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps(summary,indent=2))

if __name__ == '__main__':
    run()
