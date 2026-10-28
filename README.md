# Ledger: categorising UAE bank SMS expenses

MAAI902 Natural Language Processing & LLMs, Assessment 2 (NLP solution design).
Danish Ali (5584978), Master of Applied Artificial Intelligence, University of Wollongong in Dubai.

Ledger reads the SMS alerts UAE banks send after every card payment, puts each expense into one of 12 spending categories with a calibrated confidence score, asks the user about the uncertain ones, and answers plain-English questions such as *"How much did I spend on food in May 2025?"* through guarded, read-only SQL written by a small local LLM.

Site and results dashboard: **https://ledger.danishali.dev**

## Results

Macro-F1 of the TF-IDF (character 2–5 and word 1–2 grams, plus log amount) + logistic regression model, on 9,592 personal expenses and 1,776 external ones:

| Test set-up | Accuracy | Macro-F1 | Exact-lookup baseline |
|---|---|---|---|
| Random 5-fold | 97.7% | 94.9% | 90.0% |
| Future (train before 2025, test on 2025) | 93.6% | 89.2% | 79.6% |
| Unseen person (leave one out, average of 5) | 89.2% | 80.3% | 60.6% |
| External bank (Khalifa University ADIB set) | 71.3% | 59.4% | 19.1% |
| Unseen merchants (merchant-grouped 5-fold) | 55.5% | **51.2%** | 4.1% |

- **Calibration:** on unseen merchants, a confidence of 0.7–0.8 was right 95% of the time. At a 0.60 review threshold, 31% of brand-new-merchant purchases are filed automatically at 91% accuracy.
- **Error propagation:** 30 gold questions were answered on true and predicted categories. Questions without categories were always right. Category questions were right 55% of the time with known-merchant predictions (median error 5%) and 5% with brand-new-merchant predictions (median error 89%).
- **Text-to-SQL:** Qwen2.5-1.5B-Instruct, run locally on a Colab T4, wrote correct SQL for 20 of the 30 questions (67%): 75% of category questions and 50% of controls. The guard rejected none, and most errors were column confusions (bank instead of merchant).

## Repository layout

```
sms_transactions_pipeline.ipynb        parse 5 bank SMS templates, clean, convert to AED, privacy tests
expense_categoriser_train_test.ipynb   5 test set-ups, error analysis, calibration, confidence cascade
spending_assistant.ipynb               text-to-SQL assistant with guard rails, error propagation
scripts/rules.py                       12-category definitions, brand and keyword rules
scripts/categoriser_lib.py             shared loading and model code
scripts/censor.py                      masking used on the raw SMS exports before any analysis
export_web_model.ipynb                 privacy-pruned, calibrated export of the categoriser for the browser
site/                                  static site deployed to ledger.danishali.dev (Vercel root directory)
site/try/                              public prototype: the SMS pipeline + categoriser ported to JavaScript
```

## Public prototype (`site/try/`, ledger.danishali.dev/try/)

Visitors upload their own bank SMS export (Excel/CSV with Date and Message columns, or an SMS Backup & Restore .xml) or any transaction CSV. Everything runs in the browser; nothing is uploaded, and the page's Content-Security-Policy only allows it to download code and model files.

- `ledger-rules.js` is **generated** from `sms_transactions_pipeline.ipynb` (parser, merchant cleaning, brand table) and `scripts/rules.py` (keyword rules, category descriptions), so the browser uses the same patterns as the notebooks.
- `sms.js` ports `parse_message`, `split_merchant`, `clean_name`, the expense flags, `make_text`, the TF-IDF + logistic-regression model with sigmoid calibration, and the confidence cascade. On 2,426 test messages and 5,163 merchant strings the browser output is identical to the notebooks; model scores match scikit-learn to within 1e-5.
- `ledger_web_model.json` comes from `export_web_model.ipynb`: a character or word n-gram is kept only if it occurs in at least two people's expenses, the merchant lookup table is not exported (tier 1 becomes the visitor's own corrections), and calibration uses one model fitted on grouped out-of-fold scores (`CalibratedClassifierCV(ensemble=False)`), with the review threshold re-chosen by the same 90% rule (0.60). Pruning left unseen-merchant macro-F1 unchanged (47.9% vs 47.3%, pooled folds) and cost about a point on Khalifa (58.1% vs 59.4%).
- The text-to-SQL step uses the `spending_assistant.ipynb` prompt and runs Qwen2.5-1.5B-Instruct in the browser through WebLLM (WebGPU); the browser runs the SQL under the same read-only guard.

## Running the notebooks

The notebooks run in Google Colab from a Google Drive folder that contains this repository's files plus a `data/` folder and `merchant_labels.xlsx`. The first cell mounts Drive and changes into that folder; edit the path there if yours differs.

1. `sms_transactions_pipeline.ipynb` writes `outputs/personal_*` and `outputs/khalifa_*`.
2. `expense_categoriser_train_test.ipynb` trains and evaluates the categoriser and writes `models/`.
3. `spending_assistant.ipynb` needs a T4 GPU runtime for the LLM section; sections 1–4 run on CPU.

Requirements: pandas, scikit-learn, openpyxl, matplotlib, and for the assistant `transformers` and `torch` (both preinstalled on Colab).

## Data

**No data is included in this repository.** The SMS exports belong to the author and four volunteers, who are referred to as Contributors A–D; they were censored before analysis (names, IBANs, card numbers, account and reference numbers, OTPs and emails masked) and are available to the marker on request. The external test set is the public Kaggle dataset *Bank Transactions SMS* from Khalifa University (https://www.kaggle.com/datasets/engreemali/bank-transactions-sms-datasetss), which must be downloaded separately.

Private settings stay out of the repo: `private/config.py` can redefine `FILES` (the original export file names) and `BANNED_TERMS` (names the privacy tests must never find), and `scripts/censor.py` reads the employer pattern from the `LEDGER_EMPLOYER_RE` environment variable. `.gitignore` excludes `data/`, `outputs/`, `models/`, `private/` and all spreadsheets.

## Generative AI

Claude (Anthropic) was used, under the author's direction, to draft and debug code, suggest initial labels (checked through a blind audit of 150 merchants, 94.0% agreement, Cohen's κ = 0.93), produce figures and draft documentation. See the report's acknowledgement section for details.
