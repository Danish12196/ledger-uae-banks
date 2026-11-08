"""Stream explicitly licensed public checkpoint files with bounded memory."""
import hashlib
import json
from pathlib import Path
import requests
from paths import ROOT, LOCAL

if __name__=='__main__':
    meta=json.loads((LOCAL/'transformer_source.json').read_text())
    target=LOCAL/'public_pretrained'
    target.mkdir(exist_ok=True)
    base=f"https://huggingface.co/{meta['model']}/resolve/{meta['revision']}/"
    hashes={}
    for name in ('config.json','tokenizer_config.json','tokenizer.json','vocab.txt','model.safetensors'):
        path=target/name
        if not path.exists():
            response=requests.get(base+name,stream=True,timeout=(20,90))
            response.raise_for_status()
            size=0
            temporary=target/(name+'.part')
            with temporary.open('wb') as out:
                for chunk in response.iter_content(chunk_size=65536):
                    out.write(chunk)
                    size+=len(chunk)
            temporary.replace(path)
            print('Downloaded public model file:',name,'bytes:',size,flush=True)
        h=hashlib.sha256()
        with path.open('rb') as stream:
            for chunk in iter(lambda:stream.read(1024*1024),b''):
                h.update(chunk)
        hashes[name]=h.hexdigest()
    (LOCAL/'pretrained_hashes.json').write_text(json.dumps(dict(source=meta,sha256=hashes),indent=2))
