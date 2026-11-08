# Ledger synthetic-SMS benchmark report

## Setup

Seven redacted exports: 19,641 messages, 4,545 masked-unique observations, 3,478 labelled expenses. Strict template groups give 2,215 train / 559 validation / 704 test examples. The nominal train partition includes 261 ADIB rows excluded from training due to unresolved licensing. Existing 12-category merchant annotations are used; no row overrides are populated.

Ledger’s existing merchant/amount model is unchanged; the char-SMS baseline uses whole alerts. Validation selects configurations; classical models refit on train+validation before one frozen real-test evaluation. Per-class scores/confusion matrices are in `metrics.json`; private rows/templates/weights remain local.

## Frozen real-test comparison

| Model | Training | Selected round | Macro-F1 | Accuracy |
|---|---|---:|---:|---:|
| ledger | real_only | 0 | 74.28% | 79.97% |
| ledger | real_plus_synthetic | 2 | 73.09% | 79.83% |
| ledger | synthetic_only | 1 | 53.68% | 60.65% |
| ledger | public_synthetic_only | public | 50.35% | 59.66% |
| char_sms | real_only | 0 | 65.10% | 69.46% |
| char_sms | real_plus_synthetic | 4 | 62.87% | 69.32% |
| char_sms | synthetic_only | 3 | 43.89% | 37.36% |
| char_sms | public_synthetic_only | public | 37.43% | 26.85% |
| minilm_frozen_encoder_int8 | real_only | 2 | 39.70% | 44.32% |
| minilm_frozen_encoder_int8 | real_plus_synthetic | 3 | 44.21% | 51.14% |
| minilm_frozen_encoder_int8 | synthetic_only | 3 | 25.15% | 22.02% |

## Leave one bank out

Independent fixed public-generator experiment, excluding all held-out-bank real data/shared real templates. No private templates or bank-informed generator tuning. Macro-F1 includes all 12 classes. Support: ADCB 357, ADIB 613, FAB 1,018, Liv 742, Mashreq 748.

| Model / training | ADCB | ADIB | FAB | Liv | Mashreq |
|---|---:|---:|---:|---:|---:|
| ledger / real_only | 75.36% | 60.30% | 68.56% | 72.61% | 78.70% |
| ledger / real_plus_synthetic | 74.28% | 59.27% | 71.44% | 72.54% | 75.71% |
| ledger / synthetic_only | 44.54% | 44.77% | 56.57% | 51.09% | 51.50% |
| char_sms / real_only | 64.97% | 36.67% | 46.05% | 63.51% | 53.04% |
| char_sms / real_plus_synthetic | 58.01% | 47.08% | 46.01% | 60.41% | 60.35% |
| char_sms / synthetic_only | 32.86% | 23.03% | 32.80% | 40.30% | 34.63% |
| minilm_frozen_encoder_int8 / real_only | 31.88% | 14.32% | 28.11% | 32.09% | 14.32% |
| minilm_frozen_encoder_int8 / real_plus_synthetic | 28.01% | 23.61% | 22.40% | 23.38% | 23.28% |
| minilm_frozen_encoder_int8 / synthetic_only | 19.67% | 18.03% | 16.29% | 18.24% | 25.01% |

## What helped, failure cases, and limits

Ledger augmentation raised validation macro-F1 from 89.32% to 91.63% (round 2), but reduced final-test macro-F1 from 74.28% to 73.09%. Later noise/truncation did not sustain validation gains; stopping triggered after round 4. Whole-SMS augmentation also reduced final performance. Synthetic-only data did not replace real examples; effects varied by bank.

Round-2 validation errors included Others→Food_Dining and Entertainment→Shopping_Retail; masked merchant/template diagnostics remain local. Frozen MiniLM augmentation improved its test macro-F1 from 39.70% to 44.21%, below real-only Ledger.

Public release: 20,000 illustrative messages; 3,351 business identities (1,949 UAE), with unreviewed categories excluded. Formats/descriptors are unverified synthetic renderings, amounts are engineering priors, and real Arabic performance is unmeasured. Sources/reuse decisions are recorded in the research register.

Open questions: independent label audit; licensed authentic descriptors/Arabic formats; Kaggle permission; merchant/person holdouts; realistic FX/amount tails; rare-class confidence intervals. Strict groups yield uneven bank coverage. Earlier row-random Ledger scores are not directly comparable. Private inputs are required to reproduce the benchmark.

Full GPU fine-tuning failed under host-memory pressure. The working MiniLM baseline uses a pinned Apache-2.0 quantized frozen encoder on CPU and a trained logistic classifier: 12,000 synthetic rows, 96-token limit, validation-selected round. Its LOBO public corpus is capped at 12,000; classical LOBO uses the full public release.

A separate event filter was evaluated on synthetic holdout and parser-derived real silver labels. These diagnostics are in `metrics.json` and must not be presented as independently labelled real filtering accuracy.
