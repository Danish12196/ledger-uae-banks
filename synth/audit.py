"""Verify frozen splits, provenance, authorship and newly committed privacy boundaries."""
import csv
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'synth'))

def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT,text=True,encoding='utf-8')

def audit():
    import pandas as pd
    from benchmark import load_real
    from generate import generate
    real=load_real()
    checks={}
    groups={p:set(real[real.partition==p].template_group) for p in ('train','validation','test')}
    checks['disjoint_template_groups']=all(not groups[a]&groups[b] for a,b in [('train','test'),('train','validation'),('test','validation')])
    checks['all_12_test_classes']=real[real.partition=='test'].label.nunique()==12
    checks['frozen_row_ids_unique']=real.row_id.is_unique
    checks['private_paths_ignored']=subprocess.run(['git','check-ignore','data/private/merchant_labels.xlsx','synth/local/frozen.json','synth/out/private_test.csv'],cwd=ROOT,capture_output=True).returncode==0
    checks['deterministic_generator']=generate(100,seed=42).equals(generate(100,seed=42))
    public=pd.read_csv(ROOT/'synth/out/synthetic_public.csv')
    checks['public_provenance']=bool(public.public_eligible.all() and public.template_provenance.eq('independently_authored_illustrative').all())
    checks['public_no_real_messages']=not set(public.message)&set(pd.read_json(ROOT/'synth/local/all_messages.jsonl',lines=True).message)
    checks['every_public_row_traceable']=bool(public[['template_id','merchant','bank','generator_version','source']].notna().all().all())
    base=git('merge-base','HEAD','origin/main').strip()
    added=git('diff','--name-only',base,'HEAD').splitlines()
    checks['no_committed_private_paths']=not any(p.startswith(('data/','synth/local/','private/','models/','outputs/','synth/out/private')) or p.endswith(('.xlsx','.pkl','.joblib','.pt','.safetensors')) for p in added)
    authors=git('log',f'{base}..HEAD','--format=%an').splitlines()
    checks['branch_authorship']=bool(authors) and set(authors)=={'Danish12196'}
    bodies=git('log',f'{base}..HEAD','--format=%B').lower()
    checks['no_coauthor_trailers']='co-authored-by:' not in bodies
    checks['separate_branch']=git('branch','--show-current').strip()=='synth-dataset'
    # Scan every newly introduced text blob across every branch commit for full real SMS.
    # Start with long line/cell hashes; public CSV message cells receive a separate exact check.
    raw=pd.read_json(ROOT/'synth/local/all_messages.jsonl',lines=True)
    real_hashes={hashlib.sha256(m.strip().encode()).hexdigest() for m in raw.message if isinstance(m,str) and len(m.strip())>=25}
    matched=0
    for commit in git('rev-list',f'{base}..HEAD').splitlines():
        paths=git('diff-tree','--no-commit-id','--name-only','-r',commit).splitlines()
        for name in paths:
            if not name.endswith(('.py','.md','.json','.csv','.txt')):
                continue
            content=git('show',f'{commit}:{name}')
            cells=list(content.splitlines())
            if name.endswith('.csv'):
                import io
                cells.extend(value for row in csv.reader(io.StringIO(content)) for value in row)
            matched+=sum(hashlib.sha256(value.strip().encode()).hexdigest() in real_hashes for value in cells if len(value.strip())>=25)
    checks['no_real_message_lines_or_cells_in_new_history']=matched==0
    output={'checks':checks,'all_passed':all(checks.values()),'new_commits':len(authors),'real_message_matches':matched,
            'limits':'Checks cover new branch history, exact full message lines/cells and explicit provenance. Not a proof against every possible personal-data substring or semantic disclosure.'}
    (ROOT/'synth/local/audit.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
    print(json.dumps(output,indent=2))
    if not output['all_passed']:
        raise SystemExit(1)

if __name__=='__main__':
    audit()
