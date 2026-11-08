"""One-command local benchmark orchestration, with no push/merge side effects."""
import argparse
import os
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]

def execute(script,*args):
    subprocess.run([sys.executable,str(ROOT/'synth'/script),*args],cwd=ROOT,check=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--rounds',type=int,default=8,choices=range(1,9))
    parser.add_argument('--deadline',default='2026-11-09T03:00:00+00:00',help='Timezone-aware ISO deadline; default 7 am Dubai, 9 Nov 2026')
    parser.add_argument('--commit-rounds',action='store_true')
    parser.add_argument('--encoder',action='store_true',help='Download and evaluate the optional frozen multilingual MiniLM baseline')
    args=parser.parse_args()
    os.environ['LEDGER_DEADLINE']=args.deadline
    execute('prepare.py')
    flags=['--rounds',str(args.rounds)]
    if args.commit_rounds: flags.append('--commit-rounds')
    execute('benchmark.py',*flags)
    execute('benchmark.py','--final-only')
    execute('filter_benchmark.py')
    if args.encoder:
        execute('download_minilm.py')
        execute('encoder_benchmark.py','--final')
    execute('write_report.py')
    execute('audit.py')
