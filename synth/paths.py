"""Private work defaults outside the repository and cloud-synced workspace."""
import hashlib
import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
base=Path(os.environ.get('LOCALAPPDATA',str(Path.home()/'.local/share')))/'LedgerBenchmarks'
key=hashlib.sha256(str(ROOT).encode('utf-8')).hexdigest()[:12]
LOCAL=Path(os.environ.get('LEDGER_RUN_DIR',str(base/key))).resolve()
PRIVATE=Path(os.environ.get('LEDGER_PRIVATE_DIR',str(LOCAL/'inputs'))).resolve()
if LOCAL==ROOT or ROOT in LOCAL.parents:
    raise ValueError('Private working storage must be outside the source workspace')
if __name__=='__main__':
    print('Private working directory:',LOCAL)
    print('Private input directory:',PRIVATE)
