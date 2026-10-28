// Where the categoriser model is loaded from (first one that loads and passes its self-check wins).
// The model lives in the GitHub repo and is served by jsDelivr, pinned to the commit that added it.
window.LEDGER_CONFIG = { modelUrls: [
  'https://cdn.jsdelivr.net/gh/Danish12196/ledger-uae-banks@cf8329ecce5848eff89a969ed6eeab8290c88dc5/site/try/ledger_web_model.json',
  'ledger_web_model.json'
] };
