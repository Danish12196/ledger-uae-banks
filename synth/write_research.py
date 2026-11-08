"""Append the public gazetteer and emit a source register without accessing private files."""
import csv
import io
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

REFERENCES=[
 ('wikidata_license','Wikidata structured data licensing','https://www.wikidata.org/wiki/Wikidata:Licensing','CC0-1.0','structured_facts_training','Structured entity facts only; surrounding wiki prose is not CC0.'),
 ('adcb','ADCB SMS alerts','https://www.adcb.com/en/ways-to-bank/sms-banking/sms-alerts.aspx','not_verified','reference_only','No page wording copied into generator.'),
 ('adcb_faq','ADCB SMS FAQ','https://www.adcb.com/en/get-in-touch/faqs/services/adcb-sms-banking','not_verified','reference_only','Service description only.'),
 ('liv','Liv support','https://www.liv.me/en/ways-of-banking/get-support','not_verified','reference_only','SMS/app transition; no template extraction.'),
 ('enbd','Emirates NBD glossary','https://finwell.emiratesnbd.com/-/media/enbd/files/pdf/our-glossary.pdf','not_verified','reference_only','Alert types only.'),
 ('enbd_supplementary','Emirates NBD card activation','https://www.emiratesnbd.com/en/help-and-support/activate-your-credit-or-debit-card','not_verified','reference_only','Supplementary alert balance behavior.'),
 ('mashreq','Mashreq UAE security','https://www.mashreq.com/uae/neo/security/online-security/','not_verified','reference_only','No use of Egypt templates as UAE evidence.'),
 ('fab','FAB debit card','https://www.bankfab.com/en-ae/private/fab-world-elite-debit-card','not_verified','reference_only','Purchase and withdrawal notification support.'),
 ('fab_security','FAB security','https://www.bankfab.com/en-ae/about-fab/security-and-certifications/online-and-offline-security','not_verified','reference_only','Alert coverage only.'),
 ('dib','DIB banking agreement','https://www.dib.ae/docs/default-source/terms-conditions/terms-conditions-banking-services-agreement-english.pdf?sfvrsn=95cf1f50_6','not_verified','reference_only','No authenticated wording established.'),
 ('ei','Emirates Islamic SMS banking','https://www.emiratesislamic.ae/en/ways-to-bank/sms-banking','not_verified','reference_only','Published examples excluded from training.'),
 ('adib','ADIB SMS banking','https://www.adib.ae/en/personal/services/sms-banking','not_verified','reference_only','Language commands and types only.'),
 ('rakbank','RAKBANK SMS alerts','https://www.rakbank.ae/en/cards/card-safety/sms-alerts','not_verified','reference_only','Coverage description only.'),
 ('cbd','CBD transaction alerts','https://www.cbd.ae/personal/more/cbd-rewards/transaction-alerts','not_verified','reference_only','Channel threshold; exact boundary unverified.'),
 ('hsbc','HSBC push notifications','https://www.hsbc.ae/help/push-notifications/','not_verified','reference_only','Channel differences only.'),
 ('hsbc_balance','HSBC balance guide','https://www.hsbc.ae/current-accounts/how-to-check-your-bank-balance/','not_verified','reference_only','Fields only.'),
 ('nbk_uae','NBK UAE SMS','https://www.nbk.com/fallback/ar/uae/services-and-support/sms-service-and-mobile-banking.html','not_verified','reference_only','Arabic page; exact alert wording unverified.'),
 ('snb','SNB e-services terms','https://www.alahli.com/en/pages/personal-banking/digital-banking/e-services-usage-terms-and-conditions','not_verified','reference_only','Not an SMS corpus.'),
 ('alrajhi','Al Rajhi 2023 report','https://www.alrajhibank.com.sa/-/media/Project/AlRajhi/ARBRevamp/Investor-Relation/Annual-Reports/Annual-Report-EN-2023.pdf','not_verified','reference_only','Broad communication evidence only.'),
 ('qnb','QNB Qatar SMS','https://qnb.com/sites/qnb/qnbqatar/page/en/ensmsbanking.html','not_verified','reference_only','Qatar-specific service description.'),
 ('nbk_kw','NBK Kuwait messaging','https://www.nbk.com/ar/kuwait/services-and-support/messaging-service.html','not_verified','reference_only','Language/types only.'),
 ('nbk_bh','NBK Bahrain SMS','https://www.nbk.com/bahrain/services-and-support/sms-service.html','not_verified','reference_only','Types only.'),
 ('muscat','Bank Muscat terms','https://www.bankmuscat.com/en/about/Documents/bmforms/IND_TC_EN.pdf','not_verified','reference_only','SMS alert acknowledgment only.'),
 ('fab_oman','FAB Oman debit card','https://www.bankfab.com/en-om/personal/debit-cards/visa-classic-debit-card','not_verified','reference_only','Card alerts only.'),
 ('rta','RTA nol fares','https://rta.ae/wps/portal/rta/ae/public-transport/Nol-Fares','not_verified','reference_only','Numeric tariff facts; no prose training.'),
 ('dewa','DEWA slab tariff','https://www.dewa.gov.ae/en/consumer/billing/slab-tariff?bck=1','not_verified','reference_only','Does not establish household bill distribution.'),
 ('carrefour','Carrefour rice prices','https://www.carrefouruae.com/mafuae/en//c/F1701240','not_verified','reference_only','Time-sensitive numeric price anchors only.'),
 ('vox','VOX offers','https://uae.voxcinemas.com/ticket-offer/summary','not_verified','reference_only','Offer-specific; not typical-ticket distribution.'),
 ('starbucks','Starbucks products','https://www.starbucks.ae/en/espresso-drinks','not_verified','reference_only','No supported price range inferred.'),
 ('kaggle','Bank Transactions SMS datasetss','https://www.kaggle.com/datasets/engreemali/bank-transactions-sms-datasetss','Unknown','supplied_private_evaluation_only','Kaggle API licenseName Unknown; never train or redistribute.'),
 ('sme_paper','SME categorisation with synthetic data','https://arxiv.org/abs/2508.05425','not_verified','citation_only','Reported accuracy is not directly comparable to SMS macro-F1.'),
 ('finance_survey','Synthetic Data Applications in Finance','https://arxiv.org/abs/2401.00081','not_verified','citation_only','No training text/data copied.'),
 ('aml','Realistic synthetic AML transactions','https://arxiv.org/abs/2306.16424','not_verified','citation_only','Different task.'),
 ('distilmbert','Multilingual DistilBERT','https://huggingface.co/distilbert/distilbert-base-multilingual-cased','Apache-2.0','pretrained_model','Revision 45c032ab32cc946ad88a166f7cb282f58c753c2e; downstream private checkpoints never committed.')
 ,('minilm','Multilingual MiniLM ONNX','https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2','Apache-2.0','pretrained_model','Revision e8f8c211226b894fcb81acc59f3b34ba3efd5f42; license verified through public model metadata API. Frozen quint8 AVX2 encoder; private features stay local.')
]

if __name__=='__main__':
    records=[dict(zip(['id','title','url','license','allowed_use','notes'],r),accessed='2026-11-08',retrieval='public_web_research') for r in REFERENCES]
    (ROOT/'research/sources.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
    path=ROOT/'research/merchants_and_formats.md'
    text=path.read_text(encoding='utf-8').split('\n```csv\n')[0]
    gaz=list(csv.DictReader((ROOT/'synth/gazetteer/merchants.csv').open(encoding='utf-8')))
    stream=io.StringIO(newline='')
    writer=csv.DictWriter(stream,fieldnames=['descriptor','brand','category','country','emirate','confidence','source'],extrasaction='ignore')
    writer.writeheader()
    writer.writerows(gaz)
    path.write_text(text+'\n```csv\n'+stream.getvalue()+'```\n',encoding='utf-8')
    print('Source register entries:',len(records),'; gazetteer identities:',len(gaz))
