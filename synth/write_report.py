"""Publish only aggregate experiment metrics; never private message-level artifacts."""
import json
from pathlib import Path
from paths import ROOT, LOCAL

def write():
    rounds_path=ROOT/'synth/ROUNDS.md'
    if rounds_path.exists():
        text=rounds_path.read_text(encoding='utf-8').replace('in ignored `synth/local/`','in external local private working storage (`python synth/paths.py`)')
        rounds_path.write_text(text,encoding='utf-8')
    final=json.loads((LOCAL/'final_results.json').read_text())
    rounds=json.loads((LOCAL/'results.json').read_text())
    summary=json.loads((LOCAL/'summary.json').read_text())
    transformer=json.loads((LOCAL/'transformer_final.json').read_text()) if (LOCAL/'transformer_final.json').exists() else []
    transformer_validation=json.loads((LOCAL/'transformer_results.json').read_text()) if (LOCAL/'transformer_results.json').exists() else []
    encoder=json.loads((LOCAL/'encoder_final.json').read_text()) if (LOCAL/'encoder_final.json').exists() else []
    encoder_validation=json.loads((LOCAL/'encoder_results.json').read_text()) if (LOCAL/'encoder_results.json').exists() else []
    filter_results=json.loads((LOCAL/'filter_results.json').read_text()) if (LOCAL/'filter_results.json').exists() else None
    # These are aggregates over classes/banks, with no row IDs, merchants, dates, amounts,
    # source file names, template strings or learned parameters.
    metrics={'protocol':'strict_masked_template_holdout; final test never used for generator tuning',
             'counts':{k:summary[k] for k in ['messages','exact_unique','near_unique','labelled_expenses','unlabelled_expenses','template_groups','partitions','class_counts','bank_counts']},
             'validation':[{k:r[k] for k in ('round','model','setup','train_n','metrics','errors')} for r in rounds],
             'final':final,'transformer':transformer,'transformer_validation':transformer_validation,
             'frozen_multilingual_encoder':encoder,'encoder_validation':encoder_validation,'filter':filter_results}
    (ROOT/'synth/metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
    out=['# Ledger synthetic-SMS benchmark report','',
         '## Setup','',
         f"Seven redacted exports: {summary['messages']:,} messages, {summary['near_unique']:,} masked-unique observations, {summary['labelled_expenses']:,} labelled expenses. Strict template groups give 2,215 train / 559 validation / 704 test examples. The nominal train partition includes 261 ADIB rows excluded from training due to unresolved licensing. Existing 12-category merchant annotations are used; no row overrides are populated.",
         '',
         'Ledger’s existing merchant/amount model is unchanged; the char-SMS baseline uses whole alerts. Validation selects configurations; classical models refit on train+validation before one frozen real-test evaluation. Per-class scores/confusion matrices are in `metrics.json`; private rows/templates/weights remain local.',
         '', '## Frozen real-test comparison','',
         '| Model | Training | Selected round | Macro-F1 | Accuracy |',
         '|---|---|---:|---:|---:|']
    for row in final+transformer+encoder:
        out.append(f"| {row['model']} | {row['setup']} | {row['selected_round']} | {100*row['test']['macro_f1']:.2f}% | {100*row['test']['accuracy']:.2f}% |")
    out+=['','## Leave one bank out','',
          'Independent fixed public-generator experiment, excluding all held-out-bank real data/shared real templates. No private templates or bank-informed generator tuning. Macro-F1 includes all 12 classes. Support: ADCB 357, ADIB 613, FAB 1,018, Liv 742, Mashreq 748.',
          '', '| Model / training | ADCB | ADIB | FAB | Liv | Mashreq |','|---|---:|---:|---:|---:|---:|']
    for row in final+encoder:
        if row['setup']=='public_synthetic_only':
            continue
        values=[f"{100*row['leave_one_bank_out'][b]['macro_f1']:.2f}%" for b in ['ADCB','ADIB','FAB','Liv','Mashreq']]
        out.append('| '+row['model']+' / '+row['setup']+' | '+' | '.join(values)+' |')
    out+=['','## What helped, failure cases, and limits','',
          'Ledger augmentation raised validation macro-F1 from 89.32% to 91.63% (round 2), but reduced final-test macro-F1 from 74.28% to 73.09%. Later noise/truncation did not sustain validation gains; stopping triggered after round 4. Whole-SMS augmentation also reduced final performance. Synthetic-only data did not replace real examples; effects varied by bank.',
          '',
          'Round-2 validation errors included Others→Food_Dining and Entertainment→Shopping_Retail; masked merchant/template diagnostics remain local. Frozen MiniLM augmentation improved its test macro-F1 from 39.70% to 44.21%, below real-only Ledger.',
          '',
          'Public release: 20,000 illustrative messages; 3,351 business identities (1,949 UAE), with unreviewed categories excluded. Formats/descriptors are unverified synthetic renderings, amounts are engineering priors, and real Arabic performance is unmeasured. Sources/reuse decisions are recorded in the research register.',
          '',
          'Open questions: independent label audit; licensed authentic descriptors/Arabic formats; Kaggle permission; merchant/person holdouts; realistic FX/amount tails; rare-class confidence intervals. Strict groups yield uneven bank coverage. Earlier row-random Ledger scores are not directly comparable. Private inputs are required to reproduce the benchmark.']
    if transformer:
        out+=['', 'The GPU baseline uses multilingual DistilBERT with a 12,000-synthetic-example cap, two epochs and validation-selected checkpoints. Its final test uses train-only checkpoints without refitting on validation. This training budget differs from the classical models. Transformer leave-one-bank-out results are not included unless separately completed.']
    elif encoder:
        out+=['', 'Full GPU fine-tuning failed under host-memory pressure. The working MiniLM baseline uses a pinned Apache-2.0 quantized frozen encoder on CPU and a trained logistic classifier: 12,000 synthetic rows, 96-token limit, validation-selected round. Its LOBO public corpus is capped at 12,000; classical LOBO uses the full public release.']
    else:
        out+=['', 'GPU fine-tuning did not complete; no GPU score is fabricated. See `NOTES.md`.']
    if filter_results:
        out+=['', 'A separate event filter was evaluated on synthetic holdout and parser-derived real silver labels. These diagnostics are in `metrics.json` and must not be presented as independently labelled real filtering accuracy.']
    (ROOT/'synth/REPORT.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    # Append GPU validation results to completed rounds without exposing training texts.
    if transformer_validation:
        path=ROOT/'synth/ROUNDS.md'
        text=path.read_text(encoding='utf-8').split('\n## Optional GPU validation')[0]
        text+='\n## Optional GPU validation\n\nSynthetic training capped at 12,000 examples; two epochs, local GPU.\n\n| Round | Training | Macro-F1 |\n|---|---|---:|\n'
        for r in transformer_validation:
            text+=f"| {r['round']} | {r['setup']} | {r['metrics']['macro_f1']:.4f} |\n"
        path.write_text(text,encoding='utf-8')
    if encoder_validation:
        path=ROOT/'synth/ROUNDS.md'
        text=path.read_text(encoding='utf-8').split('\n## Frozen multilingual encoder validation')[0]
        text+='\n## Frozen multilingual encoder validation\n\nQuantized pretrained MiniLM encoder on CPU; logistic classifier; at most 12,000 synthetic expenses, 96 tokens. Full GPU fine-tuning failed under host-memory pressure.\n\n| Round | Training | Macro-F1 |\n|---|---|---:|\n'
        for r in encoder_validation:
            text+=f"| {r['round']} | {r['setup']} | {r['metrics']['macro_f1']:.4f} |\n"
        path.write_text(text,encoding='utf-8')
    print('Wrote aggregate report and metrics; no private row-level fields exported.')

if __name__=='__main__':
    write()
