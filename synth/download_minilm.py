"""Download a pinned Apache-2.0 multilingual MiniLM ONNX checkpoint."""
import hashlib
import json
from pathlib import Path
import requests
ROOT=Path(__file__).resolve().parents[1]
LOCAL=ROOT/'synth/local'
MODEL='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'
REVISION='e8f8c211226b894fcb81acc59f3b34ba3efd5f42'
if __name__=='__main__':
    metadata=requests.get(f'https://huggingface.co/api/models/{MODEL}/revision/{REVISION}',timeout=25).json()
    assert metadata.get('cardData',{}).get('license')=='apache-2.0','Model license must be explicit'
    target=LOCAL/'public_minilm'
    target.mkdir(exist_ok=True)
    hashes={}
    for remote,name in [('tokenizer.json','tokenizer.json'),('tokenizer_config.json','tokenizer_config.json'),('onnx/model_quint8_avx2.onnx','model.onnx')]:
        path=target/name
        if not path.exists():
            response=requests.get(f'https://huggingface.co/{MODEL}/resolve/{REVISION}/{remote}',stream=True,timeout=(20,90))
            response.raise_for_status()
            with (target/(name+'.part')).open('wb') as out:
                for chunk in response.iter_content(65536):out.write(chunk)
            (target/(name+'.part')).replace(path)
            print('Downloaded public MiniLM file:',name,flush=True)
        h=hashlib.sha256()
        with path.open('rb') as stream:
            for chunk in iter(lambda:stream.read(1024*1024),b''):h.update(chunk)
        hashes[name]=h.hexdigest()
    (LOCAL/'minilm_source.json').write_text(json.dumps({'model':MODEL,'revision':REVISION,'license':'Apache-2.0','sha256':hashes},indent=2))
