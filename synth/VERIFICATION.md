# Verification

- Public generation completed for 20,000 rows and reproduced the existing CSV byte for byte with seed 902.
- The documented `python synth/run.py --rounds 8 --encoder` command completed using the frozen experiment artifacts. It resumed four completed rounds and refused to reopen completed final tests.
- Round 0 plus four iteration rounds were committed separately. The stop rule triggered after two successive validation gains below 0.005.
- Both classical models completed real-only, augmented, synthetic-only and public-synthetic-only final comparisons, plus leave-one-bank-out results.
- The multilingual frozen MiniLM baseline completed the three training setups and leave-one-bank-out comparisons. Full GPU fine-tuning did not complete; its failure and CPU alternative are disclosed.
- Eight masked validation error replays (four rounds, two models) reproduced their original macro-F1 exactly. They did not alter the generator or use test errors for tuning.
- Private inputs and working artifacts were moved into local app storage outside the OneDrive workspace. Initial work copies were inside the workspace; prior OneDrive synchronization was not audited.
- Privacy checks verified disjoint template groups, frozen hashes/IDs, all 12 test classes, deterministic generation, public-only provenance, denial of private-template public export, ignored legacy private paths, separate-branch authorship, and no exact real-message lines/cells in new commit history or the public CSV.
- Source and data boundaries are the primary protection. These checks cannot establish the absence of every possible private substring, semantic disclosure, or prior cloud synchronization.

Detailed private checks and frozen input hashes remain outside the repository. Aggregate class/bank metrics are in `metrics.json`. Main is not merged or modified by this work.
