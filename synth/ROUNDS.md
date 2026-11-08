# Synthetic SMS benchmark rounds

All iteration metrics below use validation, never the frozen test set. Macro-F1 averages all 12 classes with zero for absent classes. Real-only estimates are cached when training data is unchanged.

## Round 0

Synthetic rows generated: 0. Real train 1,954; validation 559; frozen test 704. Strict template groups; unresolved-license ADIB excluded from training. Labels are inherited merchant-level project annotations; historical row overrides are not reapplied.

| Model | Training | Validation macro-F1 | Accuracy | Train rows |
|---|---|---:|---:|---:|
| ledger | real_only | 0.8932 | 0.9320 | 1954 |
| char_sms | real_only | 0.7346 | 0.8533 | 1954 |

Per-class scores, confusion matrices, class-pair errors and split membership are in ignored `synth/local/`.

