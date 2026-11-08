# Synthetic SMS benchmark rounds

All iteration metrics below use validation, never the frozen test set. Macro-F1 averages all 12 classes with zero for absent classes. Real-only estimates are cached when training data is unchanged.

## Round 0

Synthetic rows generated: 0. Real train 1,954; validation 559; frozen test 704. Strict template groups; unresolved-license ADIB excluded from training. Labels are inherited merchant-level project annotations; historical row overrides are not reapplied.

| Model | Training | Validation macro-F1 | Accuracy | Train rows |
|---|---|---:|---:|---:|
| ledger | real_only | 0.8932 | 0.9320 | 1954 |
| char_sms | real_only | 0.7346 | 0.8533 | 1954 |

Per-class scores, confusion matrices, class-pair errors and split membership are in external local private working storage (`python synth/paths.py`).

## Round 1

Synthetic rows generated: 20,000. Public authored formats; baseline descriptor variation.

| Model | Training | Validation macro-F1 | Accuracy | Train rows |
|---|---|---:|---:|---:|
| ledger | real_only | 0.8932 | 0.9320 | 1954 |
| char_sms | real_only | 0.7346 | 0.8533 | 1954 |
| ledger | real_plus_synthetic | 0.9072 | 0.9428 | 17806 |
| ledger | synthetic_only | 0.5916 | 0.6798 | 15852 |
| char_sms | real_plus_synthetic | 0.6960 | 0.8265 | 17806 |
| char_sms | synthetic_only | 0.4105 | 0.4150 | 15852 |

Per-class scores, confusion matrices, class-pair errors and split membership are in external local private working storage (`python synth/paths.py`).

## Round 2

Synthetic rows generated: 30,000. Adds conservative train-only masked private formats, class reweighting, typos and odd spacing.

| Model | Training | Validation macro-F1 | Accuracy | Train rows |
|---|---|---:|---:|---:|
| ledger | real_only | 0.8932 | 0.9320 | 1954 |
| char_sms | real_only | 0.7346 | 0.8533 | 1954 |
| ledger | real_plus_synthetic | 0.9163 | 0.9481 | 25539 |
| ledger | synthetic_only | 0.5708 | 0.6655 | 23585 |
| char_sms | real_plus_synthetic | 0.7048 | 0.8372 | 25539 |
| char_sms | synthetic_only | 0.4411 | 0.4830 | 23585 |

Per-class scores, confusion matrices, class-pair errors and split membership are in external local private working storage (`python synth/paths.py`).

## Round 3

Synthetic rows generated: 40,000. Adds truncated messages and updated validation-class reweighting.

| Model | Training | Validation macro-F1 | Accuracy | Train rows |
|---|---|---:|---:|---:|
| ledger | real_only | 0.8932 | 0.9320 | 1954 |
| char_sms | real_only | 0.7346 | 0.8533 | 1954 |
| ledger | real_plus_synthetic | 0.8992 | 0.9410 | 33445 |
| ledger | synthetic_only | 0.5915 | 0.6816 | 31491 |
| char_sms | real_plus_synthetic | 0.6950 | 0.8283 | 33445 |
| char_sms | synthetic_only | 0.4778 | 0.4794 | 31491 |

Per-class scores, confusion matrices, class-pair errors and split membership are in external local private working storage (`python synth/paths.py`).

## Round 4

Synthetic rows generated: 40,000. Adds truncated messages and updated validation-class reweighting.

| Model | Training | Validation macro-F1 | Accuracy | Train rows |
|---|---|---:|---:|---:|
| ledger | real_only | 0.8932 | 0.9320 | 1954 |
| char_sms | real_only | 0.7346 | 0.8533 | 1954 |
| ledger | real_plus_synthetic | 0.8991 | 0.9428 | 33428 |
| ledger | synthetic_only | 0.5607 | 0.6583 | 31474 |
| char_sms | real_plus_synthetic | 0.7072 | 0.8265 | 33428 |
| char_sms | synthetic_only | 0.4753 | 0.4902 | 31474 |

Per-class scores, confusion matrices, class-pair errors and split membership are in external local private working storage (`python synth/paths.py`).


## Frozen multilingual encoder validation

Quantized pretrained MiniLM encoder on CPU; logistic classifier; at most 12,000 synthetic expenses, 96 tokens. Full GPU fine-tuning failed under host-memory pressure.

| Round | Training | Macro-F1 |
|---|---|---:|
| 2 | real_only | 0.4945 |
| 2 | real_plus_synthetic | 0.4054 |
| 2 | synthetic_only | 0.1572 |
| 3 | real_only | 0.4945 |
| 3 | real_plus_synthetic | 0.4078 |
| 3 | synthetic_only | 0.1922 |
