"""Publish only aggregate experiment metrics; never private message-level artifacts."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LOCAL=ROOT/'synth/local'

def write():
    final=json.loads((LOCAL/'final_results.json').read_text())
    rounds=json.loads((LOCAL/'results.json').read_text())
    summary=json.loads((LOCAL/'summary.json').read_text())
    transformer=json.loads((LOCAL/'transformer_final.json').read_text()) if (LOCAL/'transformer_final.json').exists() else []
    transformer_validation=json.loads((LOCAL/'transformer_results.json').read_text()) if (LOCAL/'transformer_results.json').exists() else []
    filter_results=json.loads((LOCAL/'filter_results.json').read_text()) if (LOCAL/'filter_results.json').exists() else None
    # These are aggregates over classes/banks, with no row IDs, merchants, dates, amounts,
    # source file names, template strings or learned parameters.
    metrics={'protocol':'strict_masked_template_holdout; final test never used for generator tuning',
             'counts':{k:summary[k] for k in ['messages','exact_unique','near_unique','labelled_expenses','unlabelled_expenses','template_groups','partitions','class_counts','bank_counts']},
             'validation':[{k:r[k] for k in ('round','model','setup','train_n','metrics','errors')} for r in rounds],
             'final':final,'transformer':transformer,'transformer_validation':transformer_validation,'filter':filter_results}
    (ROOT/'synth/metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
    out=['# Ledger synthetic-SMS benchmark report','',
         '## Setup','',
         f"Seven local redacted exports contained {summary['messages']:,} messages. Exact and numeric-masked merchant/template deduplication left {summary['near_unique']:,} unique observations and {summary['labelled_expenses']:,} labelled expenses. The frozen strict-template split has 2,215 train, 559 validation and 704 test examples; 261 ADIB examples in the nominal train partition are excluded from training because source licensing is unresolved. The 12-category project workbook supplies merchant-level labels; its row-override column is empty. This is not an independently relabelled gold corpus.",
         '',
         'The existing Ledger merchant/amount model is reused unchanged. The second baseline uses whole-SMS character TF-IDF and logistic regression. All tuning uses validation. Selected classical configurations are refitted on train+validation, excluding ADIB, then tested once on frozen real messages. Per-class F1, support and confusion matrices are in `metrics.json`. Raw messages, private templates, row membership and model weights remain local.',
         '', '## Frozen real-test comparison','',
         '| Model | Training | Selected round | Macro-F1 | Accuracy |',
         '|---|---|---:|---:|---:|']
    for row in final+transformer:
        out.append(f"| {row['model']} | {row['setup']} | {row['selected_round']} | {100*row['test']['macro_f1']:.2f}% | {100*row['test']['accuracy']:.2f}% |")
    out+=['','## Leave one bank out','',
          'Independent fixed public-generator comparison; no validation-adapted class weights or private templates. All held-out-bank real examples and shared real template groups are removed from training. Each column averages all 12 classes, including absent ones; read support before comparing banks.',
          '', '| Model / training | ADCB | ADIB | FAB | Liv | Mashreq |','|---|---:|---:|---:|---:|---:|']
    for row in final:
        if row['setup']=='public_synthetic_only':
            continue
        values=[f"{100*row['leave_one_bank_out'][b]['macro_f1']:.2f}% (n={row['leave_one_bank_out'][b]['n']})" for b in ['ADCB','ADIB','FAB','Liv','Mashreq']]
        out.append('| '+row['model']+' / '+row['setup']+' | '+' | '.join(values)+' |')
    out+=['','## What helped, failure cases, and limits','',
          'Validation favored moderate augmentation of Ledger: its baseline macro-F1 was 89.32%, rising to 91.63% in round 2. Increasing noise and truncation in later rounds did not sustain that gain, so corpus growth stopped. Whole-SMS augmentation underperformed its real-only validation baseline. Synthetic-only performance remains substantially weaker, showing a format/merchant distribution gap rather than a replacement for real labels.',
          '',
          'The public release has 20,000 independently generated rows, including non-expense events. Its business gazetteer contains 3,351 identities (1,949 assigned to UAE); unreviewed generic business categories are excluded from generation. Names and categories are public facts/engineering annotations, while uppercase descriptors and formats are illustrative and unverified. The geographic field is not proof of current operation. Amounts are broad engineering priors with sparse public tariff anchors. Arabic examples are synthetic; real Arabic quality is unmeasured.',
          '',
          'Open questions: independent annotation audit; authentic licensed descriptors and Arabic formats; unresolved Kaggle permission; stronger merchant-held-out and person-held-out evaluation; realistic category-specific currencies/amount tails; confidence intervals for rare classes. Strict grouping leaves uneven bank coverage in validation/test. These scores are not directly comparable with earlier row-random Ledger results. Full benchmark reproduction requires the local authorized inputs; the public release can be regenerated without them.']
    if transformer:
        out+=['', 'The GPU baseline uses multilingual DistilBERT with a 12,000-synthetic-example cap, two epochs and validation-selected checkpoints. Its final test uses train-only checkpoints without refitting on validation. This training budget differs from the classical models. Transformer leave-one-bank-out results are not included unless separately completed.']
    else:
        out+=['', 'GPU baseline status: attempted, but no completed held-out score is available at report generation. See `NOTES.md`; no GPU result is inferred or fabricated.']
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
    print('Wrote aggregate report and metrics; no private row-level fields exported.')

if __name__=='__main__':
    write()
