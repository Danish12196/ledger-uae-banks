# Synthetic UAE/GCC SMS benchmark

This extends Ledger without changing its categoriser. Public synthetic data comes only from independently authored illustrative templates, a public business gazetteer, and synthetic numeric values. Actual bank wording and observed statement descriptors are not claimed. Read `research/merchants_and_formats.md` and `research/sources.json` before reusing external material.

## Public dataset: one command

From the repository root, install `python -m pip install -r synth/requirements.txt`, then run:

```powershell
python synth/generate.py --rows 20000 --seed 902 --level 1 --output synth/out/synthetic_public.csv
```

`synth/out/synthetic_public.csv` is committed. The gazetteer has per-row source/license/confidence and an explicit training-eligibility flag. Descriptor spelling is generated and unverified. CC0 applies to Wikidata structured facts; the project-authored rows/templates have no third-party page text. Unknown categories are excluded. Public rows retain template ID, bank scenario, brand, merchant variant, generator version, source and seed.

Spending labels use the 12 existing categories. `NON_TXN` and `TXN_OTHER` are separate event/filter labels and are excluded from the 12-class categoriser score. Refunds, transfers, ATM, salary and declines must not be counted as purchases. Auxiliary examples are not independently validated real-data ground truth.

## Private benchmark: one command

Place the seven authorized redacted SMS exports and the **12-category** `merchant_labels.xlsx` in ignored `data/private/`. The older 10-category workbook is rejected. Then run:

```powershell
python synth/run.py --rounds 8
```

This prepares a frozen group split if none exists, runs/resumes validation rounds, produces the final held-out test and leave-one-bank-out comparisons, writes aggregate reports, and audits the privacy boundaries. Existing frozen files are never silently regenerated. Changed inputs require a new explicitly named experiment directory/version rather than replacing an evaluation split. The default deadline is 7 am Dubai time on 9 November 2026; use `--deadline` for a later independent experiment.

The full benchmark requires local private inputs and is not reproducible from public data alone. Source hashes and private split membership remain in `synth/local/frozen.json`; dependency versions and seeds are recorded. Personal raw messages are never printed. Every script reading private messages writes only to ignored storage, except safe aggregate metrics/report summaries.

The existing notebook's parser/merchant-cleaning declarations are loaded without executing its data-loading, display or export cells. The shared `scripts/categoriser_lib.py` model is reused unchanged: character/word TF-IDF and log-amount with balanced logistic regression. The additional baseline uses full-SMS character 2–5-gram TF-IDF and balanced logistic regression. They measure different interfaces; the Ledger model receives parsed merchant text while the SMS baseline receives the whole alert.

Exact SMS duplicates and numeric-masked repetitions of a merchant/template are deduplicated. Strict masked-template groups, with merchant identity removed, stay entirely within one partition. Consequently the test/validation bank distribution is uneven; this is not an ordinary row-random 80/20 experiment. The final test is about 20% of unique labelled expenses. Merchant-level categories are inherited project annotations, not a new independent gold-label audit. The reviewed workbook has no nonempty row overrides.

Kaggle metadata reports an unknown license. Supplied ADIB rows are retained only for private evaluation, excluded from training and private-template mining. No Kaggle data, private template, learned weights, private source file name, or private row-level error is committed.

## Evaluation protocol

Round 0 is real-only. Rounds 1 onward compare real-only, augmented and synthetic-only on real validation messages. Round 1 uses original public formats; later rounds add conservative masked templates from training messages, noise and validation-driven class weights. Real-only fits are cached while data/configuration are unchanged. Size grows only while validation improvement supports it. Stop at eight rounds, two consecutive gains below 0.005 macro-F1, or the deadline. A decline counts as a non-improving round.

Each selected classical setup is refitted on train+validation before the single final test. The test is not used to edit the generator. Leave-one-bank-out is a separate fixed-public-generator experiment: all real examples from the held-out bank are excluded, as are shared real masked-template groups; private templates and globally validation-selected synthetic weights are not used. This avoids leaking held-out-bank feedback through generator tuning. Banks with rare classes have macro-F1 averaged over all 12 labels; support is reported.

All per-class scores and confusion matrices are stored locally and exported only as aggregate summaries. Merchant/template diagnostics remain local. `synth/ROUNDS.md` records each completed round, and `synth/REPORT.md` describes the final comparison. No score should be compared directly with the README's earlier random-fold experiment.

## Optional GPU baseline

`synth/transformer.py` fine-tunes multilingual DistilBERT locally. It pins the Apache-2.0 checkpoint, caps synthetic training at 12,000 expenses, uses two epochs, maximum length 96, batch size 16 and seed 902. Round 2/3 real-only, augmented and synthetic-only checkpoints are compared on validation. Downloads contain only public model weights; no private SMS is sent to Hugging Face. Disable telemetry and keep learned checkpoints in ignored `synth/local/transformer_models/`.

```powershell
synth/local/venv/Scripts/python.exe synth/transformer.py
synth/local/venv/Scripts/python.exe synth/transformer.py --final
```

Model/environment failures are documented, never replaced with invented metrics. GPU scores and training budgets must be distinguished from full-corpus classical fits. The transformer is optional for reproducibility on a CPU-only machine.

## Research refresh and verification

```powershell
python synth/research_sources.py
python synth/build_gazetteer.py
python synth/write_research.py
python synth/audit.py
```

Refreshing research changes the public dataset version. Keep a dated source snapshot for a paper. The audit verifies frozen hashes, disjoint groups, public provenance, generation determinism, no exact real SMS in the public CSV/new commit lines/cells, ignored private paths and branch authorship. It cannot prove absence of every private substring; explicit output provenance remains the primary protection.

`--private-templates` is accepted only for paths in `synth/local/` and forces generated outputs into that same ignored directory. Never publish those outputs. Keep the checked-in synthetic CSV's provenance independent of private data.
