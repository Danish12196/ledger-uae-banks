"""Retrieve CC0 structured business facts without reading private data."""
from pathlib import Path
import json
import requests

ROOT = Path(__file__).resolve().parents[1]
QUERY = '''SELECT DISTINCT ?item ?itemLabel ?countryLabel ?typeLabel WHERE {
 VALUES ?country { wd:Q878 wd:Q851 wd:Q846 wd:Q817 wd:Q398 wd:Q842 }
 ?item wdt:P17 ?country; wdt:P31 ?type.
 VALUES ?type { wd:Q4830453 wd:Q507619 wd:Q3918 wd:Q16917 wd:Q177054 wd:Q259059 wd:Q11707 wd:Q3914 wd:Q27686 wd:Q11315 wd:Q46970 wd:Q11755880 wd:Q875538 wd:Q55488 wd:Q35509 wd:QSR }
 SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
} LIMIT 5000'''.replace(' wd:QSR', '')

if __name__ == '__main__':
    response = requests.get('https://query.wikidata.org/sparql', params={'query': QUERY, 'format': 'json'},
                            headers={'User-Agent': 'LedgerResearch/1.0 academic synthetic benchmark'}, timeout=55)
    response.raise_for_status()
    target = ROOT / 'research/wikidata_businesses.json'
    target.write_text(json.dumps(response.json(), ensure_ascii=False, indent=2), encoding='utf-8')
    print('CC0 structured business records:', len(response.json()['results']['bindings']))
