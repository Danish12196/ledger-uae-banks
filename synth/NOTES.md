# Decisions and open questions

- Target stop: 2026-11-09 07:00 Asia/Dubai (03:00 UTC). Stop earlier if the stopping criterion is met.
- User authorized pushing `synth-dataset`; never merge or change main.
- A separate validation partition drives iteration. Frozen real test partitions are opened only for final reporting.
- All private inputs and derived tables/templates/model weights/errors/split membership now live in local app storage outside the repository. `python synth/paths.py` shows that location. Initial work copies were placed in ignored workspace directories before recognizing that the workspace was inside OneDrive; they were subsequently moved out. OneDrive's prior synchronization state was not inspected, so this project does not claim those copies could never have synced.
- Existing 12-category `merchant_labels.xlsx` was found in the newer project bundle and copied into ignored storage. The older 10-category file was rejected. No new rule predictions are inferred as gold.
- Public availability alone is insufficient permission for training. Unknown-rights sources are reference-only. Independently authored formats are explicitly marked illustrative, not verified bank wording.
- NON_TXN is a separate filtering task; ATM, salary, transfers and declined transactions are not forced into spending categories.
- Strict masked-template groups, including removal of merchant identity, remain disjoint across train/validation/test. This produces uneven bank representation; report that rather than relaxing grouping to inflate scores.
- Kaggle API metadata reports its license as Unknown. Supplied ADIB records are used only for private evaluation, not training or template mining. No external SMS dataset is downloaded for training.
- The newer 12-category workbook has zero nonempty row overrides. Merchant labels can be used without reconstructing historical transaction IDs.
- Classical iterations stopped after round 4: rounds 3 and 4 both improved by less than 0.005 compared with their preceding round. The best augmented validation setup was round 2. No generator edits follow final-test evaluation.
- Windows host committed-memory pressure caused allocation failures in large classical fits and PyTorch/CUDA loading, despite free GPU memory. Classical fits now run in isolated processes. A lower-memory SAGA retry preserves the char-SMS logistic objective and C when LBFGS allocation fails. The initial LOBO implementation did not preserve per-bank convergence-warning metadata; future fits record it.
- Full DistilBERT fine-tuning was attempted but did not complete. The successful resource-bounded alternative uses a pinned Apache-2.0 multilingual MiniLM quantized ONNX encoder on CPU, with frozen features and a trained logistic classifier. This is not full transformer fine-tuning or a GPU benchmark.
- The public amount draws are nominal local-currency engineering priors followed by illustrative fixed conversions; the AED-equivalent foreign tail can exceed the nominal range. No historical FX accuracy is claimed.

## Open questions

- Confirm representativeness and independent audit quality of the existing merchant labels. Automated label provenance checks do not establish manual accuracy.
- Public descriptor spelling often cannot be verified; generated uppercase variants must never be described as observed bank descriptors.
- The target of 1,500 merchants is a research target, not permission to invent businesses or count branch variants as separate businesses.
