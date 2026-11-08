# UAE/GCC bank-SMS research for Ledger

Research date: 8 November 2026. This report was researched with public web search and official pages in Codex; it is not a ChatGPT Deep Research product export. No private messages were used to prepare this report or the public gazetteer. Sources and reuse decisions are recorded in `sources.json`; business-level source identifiers are in `../synth/gazetteer/merchants.csv`.

## Evidence and reuse policy

Public access does not establish a right to train on page text. Bank pages below are reference-only: they document services and format fields, not a licensed SMS corpus. Their wording is not copied into the generator. Generator patterns are independently authored illustrations and must not be described as observed bank alerts. All actual sender IDs remain unverified unless explicitly stated; a bank name in the synthetic `bank` column is a scenario label, not proof of an authentic format or sender. Arabic website availability is not evidence of Arabic transaction-message wording.

Wikidata structured facts are CC0, as documented by its [licensing policy](https://www.wikidata.org/wiki/Wikidata:Licensing). Each retrieved business carries its entity URL. Independently curated names retain a separate `project:` source and confidence flag; these are not externally verified statement descriptors. Unknown business categories are excluded from training. No Reddit posts, screenshots, GitHub SMS corpora or bank-page bodies are included in the training set.

## 1. UAE bank SMS formats

The following matrix deliberately records missing evidence instead of inventing bank-specific templates. A service confirmation supports only the fields/types stated. Sender IDs can change and may be spoofed, so neither brand names nor banking shortcodes should be assumed to be sender IDs.

| Bank | Verified public evidence and supported alerts | Sender ID / Arabic / exact wording | Source |
|---|---|---|---|
| ADCB | SMS service and alert offerings; account/card and bill-related services | Actual sender and exact alert wording unverified here; Arabic transaction format unverified | [SMS alerts](https://www.adcb.com/en/ways-to-bank/sms-banking/sms-alerts.aspx), [FAQ](https://www.adcb.com/en/get-in-touch/faqs/services/adcb-sms-banking) |
| Liv | Support page confirms SMS notification troubleshooting; e-commerce authentication has moved toward app approval | Sender and exact wording unverified; no authenticated Arabic template located | [Liv support](https://www.liv.me/en/ways-of-banking/get-support) |
| Emirates NBD | Official material describes purchase, ATM, salary and balance notifications; supplementary-card alerts may omit remaining balance | Exact sender and Arabic wording unverified; optional balance is an evidenced field distinction | [Glossary](https://finwell.emiratesnbd.com/-/media/enbd/files/pdf/our-glossary.pdf), [card support](https://www.emiratesnbd.com/en/help-and-support/activate-your-credit-or-debit-card) |
| Mashreq | Official UAE security page describes near-real-time financial-transaction alerts | Exact text and sender unverified; Egyptian examples must not be silently treated as UAE templates | [UAE security](https://www.mashreq.com/uae/neo/security/online-security/) |
| FAB | Official card pages confirm purchase and withdrawal SMS; security page covers success and decline notifications | Sender and Arabic text unverified | [Debit card](https://www.bankfab.com/en-ae/private/fab-world-elite-debit-card), [security](https://www.bankfab.com/en-ae/about-fab/security-and-certifications/online-and-offline-security) |
| DIB | Banking-services agreement acknowledges SMS banking services | Exact transaction formats, sender, and language coverage not established | [Agreement](https://www.dib.ae/docs/default-source/terms-conditions/terms-conditions-banking-services-agreement-english.pdf?sfvrsn=95cf1f50_6) |
| Emirates Islamic | Official SMS page publishes illustrative POS, ATM and account-alert examples | Public POS example establishes a deducted amount and POS type; no merchant in that example. Sender unverified. Examples reference-only, not training inputs | [SMS banking](https://www.emiratesislamic.ae/en/ways-to-bank/sms-banking) |
| ADIB | PUSH debit/credit alerts, balance requests and promotional messages; SLA/SLE language commands | Arabic and English service documented. 2400 is a request shortcode, **not a verified originating sender ID**. Exact Arabic purchase text unverified | [SMS banking](https://www.adib.ae/en/personal/services/sms-banking) |
| RAKBANK | Retail, online, cash withdrawal, digital/IVR, balance-transfer and cheque notifications | Sender and exact text unverified; Arabic transaction wording unverified | [SMS alerts](https://www.rakbank.ae/en/cards/card-safety/sms-alerts) |
| CBD | Current transaction page distinguishes app notifications below AED 300 and continuing SMS above AED 300 | Boundary behavior at exactly AED 300 is not established by the page. Sender/text/Arabic unverified | [Transaction alerts](https://www.cbd.ae/personal/more/cbd-rewards/transaction-alerts) |
| HSBC UAE | Account debit/credit and card approval/decline notifications; reversals/payment reminders may remain SMS when push is enabled | Channel depends on preferences. Sender, exact wording and Arabic unverified | [Push notifications](https://www.hsbc.ae/help/push-notifications/), [balance guide](https://www.hsbc.ae/current-accounts/how-to-check-your-bank-balance/) |
| Wio | No sufficiently specific official SMS-format evidence established in this research pass | Entire bank-specific format/sender/language matrix unverified; generic scenarios only | No verified template source |
| NBK UAE | Official service page describes POS, internet purchase, withdrawal/deposit, salary, transfer and account notifications | Arabic/English preference documented; sender and exact transaction text unverified | [Arabic service page](https://www.nbk.com/fallback/ar/uae/services-and-support/sms-service-and-mobile-banking.html) |

### Independently authored format inventory

These patterns are original engineering examples. They are not quotations, reconstructed private templates, or claims about a bank's real wording. The public generator uses this inventory, including separate Arabic and mixed-language examples.

| Type | Illustrative pattern |
|---|---|
| Purchase | `Card {last4}: payment {currency} {amount} at {merchant} on {date}. Balance {currency} {bal}.` |
| ATM | `ATM cash withdrawal {currency} {amount}, card {last4}, {date}. Balance {bal}.` |
| Transfer out | `Transfer sent: {currency} {amount} to beneficiary {person}. Ref {reference}. Account ****{last4}. Balance {bal}.` |
| Transfer in | `Incoming transfer: {currency} {amount} from {person}. Ref {reference}. Balance {bal}.` |
| Salary | `Salary credited: {currency} {amount}. Employer {person}. Account ****{last4}. Available {bal}.` |
| Refund | `Refund from {merchant}: {currency} {amount} returned to card {last4} on {date}. Balance {bal}.` |
| Decline | `Payment attempt of {currency} {amount} at {merchant} declined. Card {last4}. No funds debited.` |
| Bill | `Bill paid to {merchant}: {currency} {amount} from account ****{last4} on {date}. Balance {bal}.` |
| Standing order | `Standing order processed: {currency} {amount} to {person}. Reference {reference}.` |
| Balance | `Balance enquiry for account ****{last4}: {currency} {bal} on {date}.` |
| Arabic purchase | `عملية شراء بمبلغ {amount} {currency} لدى {merchant} بالبطاقة المنتهية بـ {last4}. الرصيد {bal}. التاريخ {date}` |

OTP, promotion and statement-ready examples are generated separately. Declines and transfers are transaction events but are not expenses; the dataset records `TXN_OTHER` rather than assigning them a fabricated spending class. Balance enquiries and notices are `NON_TXN`.

## 2. GCC extension

| Country | Bank | Evidence and remaining gap | Source |
|---|---|---|---|
| Saudi Arabia | SNB | Official e-services terms describe transaction/account services and notifications, but do not establish exact consumer purchase-SMS wording | [E-services terms](https://www.alahli.com/en/pages/personal-banking/digital-banking/e-services-usage-terms-and-conditions) |
| Saudi Arabia | Al Rajhi | Annual-report communication evidence is too broad to verify transaction templates; actual sender/Arabic alert text unverified | [Annual report](https://www.alrajhibank.com.sa/-/media/Project/AlRajhi/ARBRevamp/Investor-Relation/Annual-Reports/Annual-Report-EN-2023.pdf) |
| Qatar | QNB | Qatar-specific SMS banking page documents alert/request functions; avoid substituting QNB India/Tunisia wording | [Qatar SMS banking](https://qnb.com/sites/qnb/qnbqatar/page/en/ensmsbanking.html) |
| Kuwait | NBK | Official Arabic page documents POS, withdrawal/deposit, salary, transfer and bill notifications; Arabic/English preference available | [Messaging service](https://www.nbk.com/ar/kuwait/services-and-support/messaging-service.html) |
| Bahrain | NBK Bahrain | POS, online purchases, deposits/withdrawals, salary/transfer and account notifications; Arabic/English preference documented | [SMS service](https://www.nbk.com/bahrain/services-and-support/sms-service.html), [Arabic FAQ](https://nbk.com/ar/bahrain/services-and-support/sms-service.html) |
| Oman | Bank Muscat | Account terms and registration form acknowledge transaction alerts; exact purchase template and sender unverified | [Terms](https://www.bankmuscat.com/en/about/Documents/bmforms/IND_TC_EN.pdf), [registration](https://www.bankmuscat.com/en/about/Documents/bmforms/Indemnity%20Form.pdf) |
| Oman | FAB Oman | Debit card page documents SMS for card use/bill due; exact wording and sender unverified | [Debit card](https://www.bankfab.com/en-om/personal/debit-cards/visa-classic-debit-card) |

These countries have separate country codes in the gazetteer. The generator's mostly-AED currency mixture is a UAE stress-test scenario, not a realistic domestic currency model for every GCC bank. Unsupported bank labels do not create evidence of coverage.

## 3. Merchant gazetteer

The machine-readable gazetteer contains public business identities, plain brand names, category, country, optional emirate, confidence, source, license, descriptor status and training eligibility. The Wikidata query and raw structured response are saved for reproduction. Country is Wikidata's country-of-entity fact, not proof that a brand operates every branch in that country. City/emirate is left empty when not verified.

The broad retrieval includes hotels, airlines, universities, schools, hospitals, restaurants, retail chains, shopping centers and generic businesses. Cave, station and residential-building records are filtered out. Unreviewed generic businesses are retained for source review but excluded from training. Type-to-category mapping is an annotation heuristic, not a manual gold label; mixed-use shopping centers are particularly ambiguous.

The descriptor column is an uppercase synthetic rendering of the business name. No row in this version claims a verified observed bank descriptor. Branch suffixes are generated at runtime and never counted as additional merchants. Target coverage of 1,500+ **verified UAE descriptors** therefore remains unmet, even if the number of UAE business identities exceeds that target. Manual descriptor verification requires suitably licensed statement examples.

Curated coverage includes delivery, fuel, utilities, telcos, government, pharmacies, hospitals, travel, cinemas, gyms, schools, digital subscriptions and ecommerce. Aggregators such as Amazon, Noon, Careem, PayPal, Tabby, Apple and Google can span categories. Their synthetic category represents a scenario convention; the underlying purchase may require a user correction. Curated identities whose country/location has not been externally checked should not be used to assert current operational presence.

## 4. Descriptor quirks and stress tests

Generated variations include uppercase/lowercase, truncation to 14/18/22 characters, synthetic branch numbers, city suffixes, and selected payment-gateway prefixes. These are engineered stress tests. A gateway does not identify what was purchased; a fuel-station address may belong to a restaurant tenant; an app-store payment can conceal the actual service. Do not automatically label all strings containing a gateway, airport, school, mall or bank name by that token alone.

Noise levels add missing characters, double spaces, removed spaces and whole-message truncation. Public rows preserve the clean brand and category for traceability. Truncation can remove the merchant entirely: those rows have inherited latent labels and should be treated as robustness tests, not necessarily answerable classification examples. The benchmark should disclose this ceiling.

Arabic/mixed purchase illustrations use Arabic grammar with Latin business names. This does not cover Arabic business aliases, dialects, bidirectional display defects, Arabic-Indic digits or authentic bank-specific Arabic phrasing. Arabic coverage is a synthetic stress test until evaluated on independently labelled Arabic messages.

FX lines in this version state that conversion applies. Non-AED amounts use fixed illustrative conversions for model features; EUR/GBP conversions are scenario constants, not historical rates. Contactless wallet wording is not used as evidence that a transaction is a subscription or a separate merchant category.

## 5. Amount ranges

Amounts use clipped log-normal draws, with log-mean at the geometric midpoint and sigma 0.85. The following ranges are **engineering priors**, not empirically measured percentiles or claims about household spending. They are nominal amounts in the selected currency; foreign examples converted to AED may exceed the nominal bounds. Broad categories contain many transaction types and cannot be grounded in one menu item.

| Category | Nominal synthetic range (mostly AED) | Evidence status |
|---|---:|---|
| Food_Dining | 8–500 | Broad assumption; official Starbucks page confirms products but does not establish a complete price distribution |
| Groceries | 10–1,200 | Public Carrefour examples include 1 kg rice around AED 10–18; basket totals are an explicit assumption |
| Transport_Auto | 2–2,500 | RTA regular fares include AED 3/5/7.5; fuel, repair and rental tails are assumptions |
| Shopping_Retail | 5–8,000 | Engineering prior; no claim of empirical range |
| Utilities_Telecom | 20–3,000 | DEWA uses consumption slabs/surcharges; household bill totals are assumptions, not quoted tariff values |
| Health_Wellness | 10–10,000 | Engineering prior spanning pharmacy to clinical services |
| Travel | 100–15,000 | Engineering prior; dynamic fares/hotel quotes not scraped |
| Entertainment | 10–1,500 | VOX public offers include AED 25 children's re-releases; event/attraction tail is assumed |
| Government_Fees | 10–10,000 | Engineering prior; service-specific official fees require later calibration |
| Housing_Education | 50–50,000 | Engineering prior; annual tuition/rent installments need dedicated scenarios |
| Digital_Subscriptions | 5–600 | Engineering prior; no unverifiable current subscription prices claimed |
| Others | 5–5,000 | Engineering prior; heterogeneous category |

Sources: [Carrefour rice](https://www.carrefouruae.com/mafuae/en//c/F1701240), [RTA nol fares](https://rta.ae/wps/portal/rta/ae/public-transport/Nol-Fares), [DEWA tariffs](https://www.dewa.gov.ae/en/consumer/billing/slab-tariff?bck=1), [VOX offers](https://uae.voxcinemas.com/ticket-offer/summary), [Starbucks products](https://www.starbucks.ae/en/espresso-drinks). These sources are reference-only; no product-page text is copied into training.

## 6. Existing datasets and prior work

- **Khalifa-associated ADIB source:** the project's README identifies [Bank Transactions SMS datasetss](https://www.kaggle.com/datasets/engreemali/bank-transactions-sms-datasetss). The public Kaggle API returned `licenseName: Unknown` on the research date. It is not downloaded or mined for generator templates. The user-supplied redacted copy is retained locally for evaluation only; its provenance/permission should be resolved before any broader use or publication. This project does not claim that availability on Kaggle grants training rights.
- **Ledger's own baseline:** the repository README reports random-fold macro-F1 94.9%, external-bank 59.4%, and unseen-merchant 51.2% for its established setup. Those scores are not directly comparable with this benchmark's more aggressive deduplication, strict template partitions and changed annotation population. Existing model construction is reused rather than replaced.
- **SME transaction augmentation:** [Aluffi et al., 2025](https://arxiv.org/abs/2508.05425) combine synthetic generation, classification and calibration. Their abstract reports 73.49% ±5.09 held-out accuracy and 90.36% ±6.52 for high-confidence predictions. These are SME transaction accuracy figures, not 12-class UAE SMS macro-F1. The paper is a research citation; its prose/data are not copied into training.
- **Broader financial synthesis:** [Synthetic Data Applications in Finance](https://arxiv.org/abs/2401.00081) surveys uses and limitations. [Realistic Synthetic Financial Transactions for Anti-Money Laundering Models](https://arxiv.org/abs/2306.16424) concerns AML transaction networks, a different task. Neither supplies a directly comparable UAE spending-category baseline here.
- **Multilingual baselines:** [DistilBERT multilingual cased](https://huggingface.co/distilbert/distilbert-base-multilingual-cased) is an Apache-2.0 model covering 104 languages. Fine-tuning was attempted but failed under host-memory pressure. The resource-bounded alternative is [multilingual MiniLM L12 v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2), whose public API metadata explicitly reports Apache-2.0. The pinned quantized ONNX encoder is frozen and a classifier is trained on its mean-pooled features. This is not full fine-tuning. Model licensing does not make every downstream SMS source reusable.

## Reproduction and remaining limitations

Run `python synth/research_sources.py`, then `python synth/build_gazetteer.py`. The query is explicit and uses structured CC0 entity labels, types and country facts. The curated seed is project-authored and disclosed separately. Retrieval is not a current-business registry: closed, renamed, duplicate or misclassified entities may remain. The original response is preserved as a dated snapshot; refreshing it creates a new dataset version.

Exact authenticated bank templates, sender IDs and comprehensive Arabic examples remain research gaps. The public release is honestly labelled synthetic and illustrative. It should not be advertised as a verified bank-format corpus or as evidence of generalization to all listed banks.

## Gazetteer CSV

The CSV block below is appended from the public gazetteer by `synth/write_research.py`; the standalone CSV retains extra provenance/eligibility columns.

```csv
descriptor,brand,category,country,emirate,confidence,source
0XARBITRAGE,0xarbitrage,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q136027499
3DR MODELS,3dr Models,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q96371069
72 HOTEL,72 Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150598
ACE HARDWARE,ACE Hardware,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ACME ONE,ACME One,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140129834
ADDC,ADDC,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ADNOC,ADNOC,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AG HOTEL,AG Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997604
ALHOSN UNIVERSITY,ALHOSN University,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4652368
AMLED SCHOOL,AMLED SCHOOL,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088175
ARAR GROUP,ARAR GROUP,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140447597
ARVIEW,ARView,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141974854
AVE.COM,AVE.com,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q300136
ABDULRAHMAN ALNUAIMI AUDITING OF ACCOUNTS LLC,Abdulrahman AlNuaimi Auditing of Accounts LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140011278
ABIDOS HOTEL APARTMENT AL BARSHA,Abidos Hotel Apartment Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150266
ABIDOS HOTEL APARTMENT DUBAILAND,Abidos Hotel Apartment Dubailand,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997625
ABJAD GRAND HOTEL,Abjad Grand Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856053
ABU DHABI AVIATION,Abu Dhabi Aviation,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q334931
ABU DHABI COMMERCIAL BANK,Abu Dhabi Commercial Bank,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4670123
ABU DHABI FALCON HOSPITAL,Abu Dhabi Falcon Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q4670129
ABU DHABI FINANCIAL GROUP,Abu Dhabi Financial Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q22080735
ABU DHABI GAS INDUSTRIES LIMITED,Abu Dhabi Gas Industries Limited,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4670132
ABU DHABI HEALTH SERVICES,Abu Dhabi Health Services,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q77084502
"ABU DHABI INDIAN SCHOOL BRANCH 1, AL WATHBA","Abu Dhabi Indian School Branch 1, Al Wathba",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q112160952
ABU DHABI INTERNATIONAL SCHOOL,Abu Dhabi International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q65073370
ABU DHABI INVESTMENT AUTHORITY,Abu Dhabi Investment Authority,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q334956
ABU DHABI INVESTMENT COUNCIL,Abu Dhabi Investment Council,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4670139
ABU DHABI ISLAMIC BANK,Abu Dhabi Islamic Bank,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4670141
ABU DHABI MAR,Abu Dhabi MAR,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q334959
ABU DHABI MALL,Abu Dhabi Mall,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q4670143
ABU DHABI MEDIA,Abu Dhabi Media,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4115940
ABU DHABI NATIONAL ENERGY COMPANY,Abu Dhabi National Energy Company,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6349602
ABU DHABI NATIONAL EXHIBITIONS COMPANY,Abu Dhabi National Exhibitions Company,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4670149
ABU DHABI NATIONAL INSURANCE COMPANY,Abu Dhabi National Insurance Company,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q20990736
ABU DHABI POLICE,Abu Dhabi Police,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ABU DHABI PORTS COMPANY,Abu Dhabi Ports Company,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q15177997
ABU DHABI POWER CORPORATION,Abu Dhabi Power Corporation,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q65519744
ABU DHABI SCHOOL OF MANAGEMENT,Abu Dhabi School of Management,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q134359499
ABU DHABI UNITED GROUP,Abu Dhabi United Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q16240669
ABU DHABI UNIVERSITY,Abu Dhabi University,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4670157
ABU DHABI UNIVERSITY–DUBAI,Abu Dhabi University–Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q116909517
ACADEMY OF TECHNICAL TRAINING,Academy of Technical Training,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4671535
ACCOR,Accor,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ACE-LEADERS,Ace-Leaders,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141852924
ACQUISITY AI,Acquisity AI,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139577600
ACTION HOTEL RAS AL KHAIMAH,Action Hotel Ras Al Khaimah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856079
ADENGAGE,AdEngage,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141545329
ADAGIO PREMIUM THE PALM,Adagio Premium The Palm,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150205
ADDRESS BOULEVARD,Address Boulevard,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q7712376
ADDRESS CREEK HARBOUR,Address Creek Harbour,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q136652705
ADDRESS DOWNTOWN,Address Downtown,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150315
ADDRESS DUBAI MALL,Address Dubai Mall,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150327
ADDRESS DUBAI MARINA,Address Dubai Marina,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150724
ADDRESS FOUNTAIN VIEWS,Address Fountain Views,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150325
ADDRESS MONTGOMERIE,Address Montgomerie,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150736
ADDRESS SKY VIEW,Address Sky View,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997627
ADIDAS,Adidas,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ADOBE,Adobe,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AEROVISTA,Aerovista,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q247886
AFRICANA HOTEL,Africana Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997680
AGILE FINANCIAL TECHNOLOGIES,Agile Financial Technologies,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140697011
AGODA,Agoda,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AHMAD ALUMINIUM & GLASS CONT,Ahmad Aluminium & Glass Cont,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139832716
AIR ARABIA,Air Arabia,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AIRBNB,Airbnb,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AJMAN BEACH HOTEL,Ajman Beach Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111115160
AJMAN HOTEL,Ajman Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997716
"AJMAN SARAY, A LUXURY COLLECTION RESORT, AJMAN","Ajman Saray, a Luxury Collection Resort, Ajman",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150614
AJMAN SPECIALTY GENERAL HOSPITAL,Ajman Specialty General Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q4699898
AJMAN UNIVERSITY,Ajman University,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q12204508
AKAS-INN HOTEL APARTMENT,Akas-Inn Hotel Apartment,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150255
AL ADAB IRANIAN PRIVATE SCHOOL FOR BOYS,Al Adab Iranian Private School for Boys,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088120
AL ADAB IRANIAN PRIVATE SCHOOL FOR GIRLS,Al Adab Iranian Private School for Girls,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088123
AL AIN ENGLISH SPEAKING SCHOOL,Al Ain English Speaking School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4703452
AL AIN HOSPITAL,Al Ain Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q30254307
AL AIN PALACE HOTEL ABU DHABI,Al Ain Palace Hotel Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150552
AL AIN UNIVERSITY,Al Ain University,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4703454
AL AIN WATER,Al Ain Water,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AL AMEEN SCHOOL,Al Ameen School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4703475
"AL AMEER ENGLISH SCHOOL, AJMAN","Al Ameer English School, Ajman",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q22948341
AL ARQM PRIVATE SCHOOL,Al Arqm Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088126
AL BADA HOTEL AND RESORT,Al Bada Hotel and Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997610
AL BAHAR HOTEL & RESORT,Al Bahar Hotel & Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150642
AL BAIK,Al Baik,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AL BAIT HOTEL,Al Bait Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q101312717
AL BANDAR ARJAAN BY ROTANA – DUBAI CREEK,Al Bandar Arjaan by Rotana – Dubai Creek,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150476
AL BANDAR ROTANA – DUBAI CREEK,Al Bandar Rotana – Dubai Creek,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150473
AL BARSHA PREMIUM HOTEL APARTMENTS,Al Barsha Premium Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997615
AL BASATEEN PRIVATE NURSERY,Al Basateen Private Nursery,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088129
AL BASATEEN PRIVATE NURSERY HATTA BRANCH,Al Basateen Private Nursery Hatta branch,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088131
AL BATEEN SECONDARY SCHOOL,Al Bateen Secondary School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q22948350
AL BUSTAN CENTRE & RESIDENCE,Al Bustan Centre & Residence,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997691
AL BUSTAN HOTEL,Al Bustan Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997699
AL BUSTAN HOTEL FLATS,Al Bustan Hotel Flats,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997704
AL BUSTAN TOWER HOTEL SUITES,Al Bustan Tower Hotel Suites,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997705
AL DHAFRA PRIVATE SCHOOL,Al Dhafra Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4703739
AL DIAR CAPITAL HOTEL,Al Diar Capital Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150568
AL DIAR DANA HOTEL,Al Diar Dana Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150562
AL DIAR MINA HOTEL,Al Diar Mina Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150563
AL DIAR SAWA HOTEL APARTMENTS,Al Diar Sawa Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997608
AL DIYAFAH HIGH SCHOOL,Al Diyafah High School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088133
AL EMAN EDUCATIONAL EST ( AL EMAN PRIVATE SCHOOL ),Al Eman Educational Est ( Al Eman private School ),Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088134
AL FALAH SCHOOL,Al Falah School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q12241659
AL FARDAN INVESTMENTS LIMITED,Al Fardan Investments Limited,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q114066246
AL FAREJ HOTEL,Al Farej Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997685
AL GHURAIR GROUP,Al Ghurair Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4702428
AL GHURAIR INVESTMENT LLC,Al Ghurair Investment LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4703879
AL GHURAIR UNIVERSITY,Al Ghurair University,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4703880
"AL HABTOOR PALACE, PREFERRED HOTELS & RESORTS","Al Habtoor Palace, Preferred Hotels & Resorts",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150286
AL HABTOOR POLO RESORT,Al Habtoor Polo Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150285
AL HAYAT HOTEL APARTMENTS,Al Hayat Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997707
AL HAYAT HOTEL SUITES,Al Hayat Hotel Suites,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997694
AL HIKMAH PRIVATE SCHOOL - AL JURF BRANCH,Al Hikmah Private School - Al Jurf Branch,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q130544386
AL HILAL BANK,Al Hilal Bank,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4122339
AL ITTIHAD PRIVATE SCHOOL (BR),Al Ittihad Private School (BR),Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088142
AL ITTIHAD PRIVATE SCHOOL,Al Ittihad Private school,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088136
AL JABER AVIATION,Al Jaber Aviation,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q2855408
AL JADDAF ROTANA SUITE HOTEL,Al Jaddaf Rotana Suite Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150404
AL JALILA CHILDREN'S SPECIALTY HOSPITAL,Al Jalila Children's Specialty Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q4704111
AL JAWHARA GARDENS HOTEL,Al Jawhara Gardens Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997679
AL JAWHARA METRO HOTEL,Al Jawhara Metro Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111888203
AL JAZIRA CLUB HOTEL,Al Jazira Club Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997601
AL KHALEEJ GRAND HOTEL,Al Khaleej Grand Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856040
AL KHALEEJ NATIONAL SCHOOL,Al Khaleej National School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088144
AL KHALEEJ PLAZA HOTEL,Al Khaleej Plaza Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856042
AL KHALIDIAH RESORT,Al Khalidiah Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997700
AL KHOORY ATRIUM HOTEL,Al Khoory Atrium Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150252
"AL KHOORY EXECUTIVE HOTEL, AL WASL","Al Khoory Executive Hotel, Al Wasl",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150353
AL KHOORY HOTEL APARTMENTS,Al Khoory Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150249
AL MAAREF PRIVATE SCHOOL (LLC),Al Maaref Private School (LLC),Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088147
AL MAHA ARJAAN HOTEL APARTMENT BY ROTANA ABU DHABI,Al Maha Arjaan Hotel Apartment by Rotana Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997634
AL MAHA REGENCY HOTEL SUITES,Al Maha Regency Hotel Suites,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856072
AL MAHA RESIDENCE RAK,Al Maha Residence Rak,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997725
"AL MAHA, A LUXURY COLLECTION DESERT RESORT & SPA, DUBAI","Al Maha, a Luxury Collection Desert Resort & Spa, Dubai",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150332
AL MAJAZ PREMIERE HOTEL APARTMENTS,Al Majaz Premiere Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997701
AL MALLAH,Al Mallah,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AL MANAR GRAND HOTEL APARTMENT,Al Manar Grand Hotel Apartment,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150418
AL MANAR HOTEL APARTMENTS,Al Manar Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150578
AL MANZEL HOTEL APARTMENTS,Al Manzel Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150558
AL MAWAKEB SCHOOL - AL GARHOUD,Al Mawakeb School - Al Garhoud,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088148
AL MAWAKEB SCHOOL - BR,Al Mawakeb School - Br,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088151
AL MAWAKEB SCHOOL AL KHWANEEJ,Al Mawakeb School Al Khwaneej,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089033
AL MAWAKEB SCHOOLS,Al Mawakeb Schools,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q22031316
AL MAYA,Al Maya,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AL MIZHAR AMERICAN ACADEMY SCHOOL,Al Mizhar American Academy School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088153
AL NAHDA NATIONAL SCHOOLS,Al Nahda National Schools,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4704526
AL NIBRAS INTERNATIONAL PRIVATE SCHOOL,Al Nibras International private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088154
AL NOOR HOSPITAL,Al Noor Hospital,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4704553
AL NUKHA ROASTERY,Al Nukha Roastery,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139519703
AL QASIMIA UNIVERSITY,Al Qasimia University,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q38250910
AL RAEIN HOTEL APARTMENTS,Al Raein Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997650
AL RAHA BEACH HOTEL,Al Raha Beach Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150572
AL RAIS CARGO,Al Rais Cargo,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q4704677
AL RASHID AL SALEH PRIVATE SCHOOL,Al Rashid Al Saleh Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088156
AL RAYA HOTEL APARTMENTS,Al Raya Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856034
AL REEF LEBANESE BAKERY,Al Reef Lebanese Bakery,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AL SADIQ ISLAMIC ENGLISH SCHOOL,Al Sadiq Islamic English School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088158
AL SALAM COMMUNITY SCHOOL,Al Salam Community School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089071
AL SALAM GRAND HOTEL,Al Salam Grand Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997696
AL SALAM PRIVATE SCHOOL,Al Salam Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088164
AL SALAM PRIVATE SCHOOL & NURSERY,Al Salam Private School & Nursery,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q39057691
AL SARAB HOTEL,Al Sarab Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856046
AL SAYEGH AIRLINES,Al Sayegh Airlines,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q4704768
"AL SEEF HERITAGE HOTEL DUBAI, CURIO COLLECTION BY HILTON","Al Seef Heritage Hotel Dubai, Curio Collection by Hilton",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q96755874
AL SEEF RESORT & SPA BY ANDALUS,Al Seef Resort & Spa by Andalus,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150199
AL SHIRAWI ENTERPRISES LLC,Al Shirawi Enterprises LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140889254
AL SHUROOQ PRIVATE SCHOOL,Al Shurooq Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088166
AL TAYER GROUP,Al Tayer Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4704873
AL WAHDA MALL,Al Wahda Mall,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q4704936
AL WALEED PALACE HOTEL APARTMENT AL BARSHA,Al Waleed Palace Hotel Apartment Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856021
AL WALEED PALACE HOTEL APARTMENTS - OUD METHA,Al Waleed Palace Hotel Apartments - Oud Metha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150401
"AL WATHBA, A LUXURY COLLECTION DESERT RESORT & SPA, ABU DHABI","Al Wathba, a Luxury Collection Desert Resort & Spa, Abu Dhabi",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150191
AL YASMINA SCHOOL,Al Yasmina School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4704999
AL ZAHRA HOSPITAL,Al Zahra Hospital,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AL-BAHAR METAL ENCLOSURES & CABINETS MANUFACTURING,Al-Bahar Metal Enclosures & Cabinets Manufacturing,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141603405
AL-FUTTAIM GROUP,Al-Futtaim Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4702408
ALHAMRA HOTEL,AlHamra Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997710
ALWASL UNIVERSITY,AlWasl University,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5146743
ALAIN HOTEL AJMAN,Alain Hotel Ajman,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997712
ALAR INTERNATIONAL DMCC,Alar International DMCC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141852925
ALDAR HOTEL,Aldar Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997709
ALHAJISPERFUMES,Alhajisperfumes,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141784916
ALMOTAHIDA EDUCATION GROUP,Almotahida Education Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q134973220
ALOFT ABU DHABI,Aloft Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150186
ALOFT AL AIN,Aloft Al Ain,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150702
"ALOFT CITY CENTRE DEIRA, DUBAI","Aloft City Centre Deira, Dubai",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150477
ALOFT DUBAI SOUTH,Aloft Dubai South,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997733
"ALOFT ME'AISAM, DUBAI","Aloft Me'aisam, Dubai",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150730
ALOFT PALM JUMEIRAH,Aloft Palm Jumeirah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150237
ALPHAIT ENGINEERING,AlphaIT Engineering,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141625931
AMAN DUBAI,Aman Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q133029787
AMANA CONTRACTING AND STEEL BUILDINGS,Amana Contracting and Steel Buildings,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q17003668
AMAZON,Amazon,Shopping_Retail,AE,,project_category;descriptor_unverified,project:scripts/rules.py
AMAZON PRIME,Amazon Prime,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AMAZON.AE,Amazon.ae,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AMBASSADOR INTERNATIONAL ACADEMY,Ambassador International Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089072
AMBASSADOR KINDERGARTEN LLC,Ambassador Kindergarten LLC,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088168
AMBASSADOR SCHOOL L.L.C,Ambassador School L.L.C,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088171
AMER CENTER,Amer Center,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AMERICAN ACADEMY IN AL-MIZHAR,American Academy in Al-Mizhar,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4742861
AMERICAN COMMUNITY SCHOOL SHARJAH,American Community School Sharjah,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4743497
AMERICAN COMMUNITY SCHOOL OF ABU DHABI,American Community School of Abu Dhabi,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4743501
AMERICAN HOSPITAL DUBAI,American Hospital Dubai,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AMERICAN INTERNATIONAL SCHOOL,American International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088172
"AMERICAN INTERNATIONAL SCHOOL, ABU DHABI","American International School, Abu Dhabi",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4744173
AMERICAN SCHOOL OF CREATIVE SCIENCE,American School of Creative Science,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088173
AMERICAN SCHOOL OF DUBAI,American School of Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4744936
AMERICAN UNIVERSITY IN DUBAI,American University in Dubai,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AMERICAN UNIVERSITY IN THE EMIRATES,American University in the Emirates,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4745311
AMERICAN UNIVERSITY OF RAS AL KHAIMAH,American University of Ras Al Khaimah,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q85845369
AMERICAN UNIVERSITY OF SHARJAH,American University of Sharjah,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AMERICANA,Americana,Food_Dining,AE,,project_category;descriptor_unverified,project:scripts/rules.py
AMITY SCHOOL DUBAI,Amity School Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q122231783
AMITY SCHOOL L.L.C,Amity School L.L.C,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089006
ANANTARA DOWNTOWN DUBAI HOTEL,Anantara Downtown Dubai Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q142066296
ANANTARA EASTERN MANGROVES ABU DHABI HOTEL,Anantara Eastern Mangroves Abu Dhabi Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150202
ANANTARA QASR AL SARAB DESERT RESORT,Anantara Qasr al Sarab Desert Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150676
ANANTARA SIR BANI YAS ISLAND AL SAHEL VILLA RESORT,Anantara Sir Bani Yas Island Al Sahel Villa Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150695
ANANTARA SIR BANI YAS ISLAND AL YAMM VILLA RESORT,Anantara Sir Bani Yas Island Al Yamm Villa Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150689
ANANTARA THE PALM DUBAI RESORT,Anantara The Palm Dubai Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150241
ANDAZ DUBAI THE PALM,Andaz Dubai The Palm,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150218
ANDAZ DUBAI THE PALM APARTMENTS,Andaz Dubai The Palm Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q136513117
ANGHAMI,Anghami,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ANGSANA HOTEL TOWER 1,Angsana Hotel Tower 1,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q124092763
ANIMATED TIMES,Animated Times,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140355874
APARTHOTEL ADAGIO ABU DHABI AL BUSTAN,Aparthotel Adagio Abu Dhabi Al Bustan,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150189
APARTHOTEL ADAGIO DUBAI DEIRA,Aparthotel Adagio Dubai Deira,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150506
APARTHOTEL ADAGIO FUJAIRAH,Aparthotel Adagio Fujairah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150639
APPLE,Apple,Digital_Subscriptions,AE,,project_category;descriptor_unverified,project:scripts/rules.py
APPLE INTERNATIONAL SCHOOL,Apple International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088176
APPLE MUSIC,Apple Music,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
APPLE STORE,Apple Store,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
APPLE ICLOUD,Apple iCloud,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AQUAVENTURE,Aquaventure,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ARAB UNITY SCHOOL,Arab Unity School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4783263
ARABIAN CENTER,Arabian Center,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q18205153
ARABIAN COURTYARD HOTEL & SPA,Arabian Courtyard Hotel & Spa,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150452
ARABIAN TEA HOUSE,Arabian Tea House,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ARABIC LANGUAGE ACADEMY,Arabic language academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q118192952
ARABTEC,Arabtec,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4783497
ARAMEX,Aramex,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ARAVI HOTEL,Aravi Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150507
ARBELLA BOUTIQUE HOTEL,Arbella Boutique Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997708
ARCADIA HIGH SCHOOL,Arcadia High School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089074
ARCSEN,Arcsen,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q142084423
ARMADA BLUEBAY,Armada BlueBay,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150729
ARMANI HOTEL DUBAI,Armani Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150312
ARYANA HOTEL,Aryana Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150590
ASCOTT PARK PLACE DUBAI,Ascott Park Place Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150357
ASFAR RESORTS AL AIN,Asfar Resorts Al Ain,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997744
ASHBILIYA,Ashbiliya,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140516222
ASIANA HOTEL DUBAI,Asiana Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150547
ASTER HOSPITAL,Aster Hospital,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ASTER PHARMACY,Aster Pharmacy,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ASTORIA HOTEL,Astoria Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111151473
ASWAAQ,Aswaaq,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AT.MOSPHERE,At.mosphere,Food_Dining,AE,,type_mapped,http://www.wikidata.org/entity/Q135004753
ATANA HOTEL,Atana Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150232
ATLANTIS THE PALM,Atlantis The Palm,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
"ATLANTIS, THE PALM","Atlantis, The Palm",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q756690
ATLAS MARA LIMITED,Atlas Mara Limited,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q17513924
AUDIOCULT,Audiocult,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q106075383
AURIS BOUTIQUE HOTEL APARTMENTS,Auris Boutique Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150265
"AUSTRALIAN INTERNATIONAL SCHOOL, SHARJAH","Australian International School, Sharjah",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q30640877
AUTO.AE,Auto.ae,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141801646
AUTOPRO,AutoPro,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AUTOZONE UAE - AUTOZONE ASSEMBLING LLC,AutoZone UAE - AutoZone Assembling LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141041395
AUTOMATIC RESTAURANT,Automatic Restaurant,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AVAIL DEPOSITS,Avail Deposits,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q138783719
AVANI DEIRA DUBAI HOTEL,Avani Deira Dubai Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150550
AVANI IBN BATTUTA DUBAI HOTEL,Avani Ibn Battuta Dubai Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150697
AVIS,Avis,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
AXI,Axi,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q137162596
AXYS HOLDING,Axys Holding,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q138786602
AYLA BAWADI HOTEL,Ayla Bawadi Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150240
AYLA GRAND HOTEL,Ayla Grand Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150231
AYLA HOTEL,Ayla Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150738
AZDAN,Azdan,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140128899
AZURX,AzurX,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141948010
BM ACACIA HOTEL AND APARTMENTS,BM Acacia Hotel and Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150630
BM BEACH HOTEL,BM Beach Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150646
BM BEACH RESORT,BM Beach Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150628
BSA TRADING LLC,BSA Trading LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141563709
BAB AL-QASR,Bab al-Qasr,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q797528
BABYSHOP,Babyshop,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BAHI AJMAN PALACE HOTEL,Bahi Ajman Palace Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150611
BAIT AL MANDI,Bait Al Mandi,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BAITY HOTEL APARTMENTS,Baity Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997641
BALANCED SCORE TRAINING CENTER,Balanced Score Training Center,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q135258806
BANAMIND,Banamind,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139783097
BAQER MOHEBI,Baqer Mohebi,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BARBEQUE NATION,Barbeque Nation,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BARCELÓ AL JADDAF,Barceló Al Jaddaf,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150396
BARCELÓ BUSINESS BAY,Barceló Business Bay,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q142083525
BARCELÓ RESIDENCES DUBAI MARINA,Barceló Residences Dubai Marina,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111151481
BARRACUDA BEACH RESORT,Barracuda Beach Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150623
BATEEL,Bateel,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BATH AND BODY WORKS,Bath and Body Works,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BATTERY MAN DUBAI UAE,Battery Man Dubai UAE,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139715207
BEACH ROTANA - ABU DHABI,Beach Rotana - Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150559
BEACH ROTANA - ALL SUITES,Beach Rotana - All Suites,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150557
BEACH ROTANA ABU DHABI,Beach Rotana Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q4875753
BEACH ROTANA RESIDENCES,Beach Rotana Residences,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150560
BEACH WALK HOTEL,Beach Walk Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997624
BEARHOST,Bearhost,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141008038
BEAUFORT ASSOCIATES,Beaufort Associates,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141806826
BEDOUIN OASIS CAMP,Bedouin Oasis Camp,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150624
BEIT AL KHAIR,Beit Al Khair,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BELFORD UNIVERSITY,Belford University,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4882384
BELLA ENTERTAINMENT,Bella Entertainment,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141551928
BENTHAM SCIENCE PUBLISHERS,Bentham Science Publishers,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q2896740
BESSERN,Bessern,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q110209236
BEST WESTERN PLUS PEARL CREEK,Best Western Plus Pearl Creek,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150465
BEYIN DIGITAL TECHNOLOGY LIMITED,Beyin Digital Technology Limited,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141050364
BIELA.DEV,Biela.dev,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q135916733
BIKANERVALA,Bikanervala,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BILVA INDIAN SCHOOL,Bilva Indian School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088180
BINSINA PHARMACY,BinSina Pharmacy,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BINARY STUDIO,Binary Studio,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q138746621
BITUMAX,Bitumax,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q123165555
BLOCKWILL,BlockWill,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140380819
BLOOMINGDALES,Bloomingdales,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BLUEMINT SERVICES,BlueMint Services,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141061917
BOLT,Bolt,Transport_Auto,AE,,project_category;descriptor_unverified,project:scripts/rules.py
BONNINGTON JUMEIRAH LAKES TOWERS,Bonnington Jumeirah Lakes Towers,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150713
BOOKING.COM,Booking.com,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BOOTS PHARMACY,Boots Pharmacy,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BORETS INTERNATIONAL FZE,Borets International FZE,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q130558477
BOROUGE,Borouge,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4946303
BOSPORUS,Bosporus,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BRANDS FOR LESS,Brands For Less,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BRIGHT RIDERS,Bright Riders,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089036
BRIGHTON COLLEGE DUBAI,Brighton College Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089041
BRITISH COUNCIL,British Council,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BRITISH GULF INTERNATIONAL AIRLINES,British Gulf International Airlines,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q784062
"BRITISH INTERNATIONAL SCHOOL, ABU DHABI","British International School, Abu Dhabi",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q15204892
BRITISH UNIVERSITY IN DUBAI,British University in Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4971189
BROADWAY HOTEL,Broadway Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997668
BUDGET RENT A CAR,Budget Rent a Car,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BUDS PUBLIC SCHOOL,Buds Public School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088182
"BUDS PUBLIC SCHOOL, DUBAI","Buds Public School, Dubai",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4985169
BUFFALO WILD WINGS,Buffalo Wild Wings,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BULGARI RESORT DUBAI,Bulgari Resort Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150303
BURJUMAN,BurJuman,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q2386719
BURJUMAN ARJAAN BY ROTANA DUBAI,BurJuman Arjaan by Rotana Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150437
BURGER KING,Burger King,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BURJ AL-ARAB,Burj al-Arab,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q62939
BURJEEL HOSPITAL,Burjeel Hospital,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BYBIT,Bybit,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q109424729
BYBLOS HOTEL,Byblos Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150215
C CENTRAL RESORT THE PALM,C Central Resort The Palm,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150242
CAFU,CAFU,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CBA REAL ESTATE,CBA Real Estate,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140149171
CFO VENTURES,CFO Ventures,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139934755
CAESARS PALACE DUBAI,Caesars Palace Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150711
CAFFE NERO,Caffe Nero,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CAMBRIDGE ACADEMY FOR HIGHER EDUCATION,Cambridge Academy for Higher Education,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q16256173
CAMBRIDGE INTERNATIONAL SCHOOL,Cambridge International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5025462
CANADIAN UNIVERSITY DUBAI,Canadian University Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5030654
CANAL CENTRAL HOTEL,Canal Central Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150290
CANOPY BY HILTON DUBAI AL SEEF,Canopy by Hilton Dubai Al Seef,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150457
CANVA,Canva,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CAPITAL CENTRE ARJAAN BY ROTANA,Capital Centre Arjaan by Rotana,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150183
CAPITOL HOTEL,Capitol Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150393
CARAVELLA,Caravella,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q131753218
CAREEM,Careem,Transport_Auto,AE,,project_category;descriptor_unverified,project:scripts/rules.py
CAREEM PLUS,Careem Plus,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CAREEM RIDE,Careem Ride,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CARGO PLUS AVIATION,Cargo Plus Aviation,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q5039269
CARGOZ,Cargoz,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q142066923
CARIBOU COFFEE,Caribou Coffee,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CARLTON AL BARSHA,Carlton Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150254
CARLTON DOWNTOWN HOTEL,Carlton Downtown Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150338
CARLTON PALACE HOTEL,Carlton Palace Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150486
CARLTON TOWER HOTEL,Carlton Tower Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150468
CARREFOUR,Carrefour,Groceries,AE,,project_category;descriptor_unverified,project:scripts/rules.py
CARTIER,Cartier,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CASITEL,Casitel,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141984009
CAVIAR,Caviar,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q134548977
CENTARA MIRAGE BEACH RESORT DUBAI,Centara Mirage Beach Resort Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150576
CENTER VILLE HOTEL,Center Ville Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q112026982
CENTREPOINT,Centrepoint,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CENTRO AL MANHAL HOTEL BY ROTANA ABU DHABI,Centro Al Manhal Hotel by Rotana Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997606
CENTRO CAPITAL CENTRE BY ROTANA,Centro Capital Centre by Rotana,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997598
CENTRO SHARJAH HOTEL BY ROTANA,Centro Sharjah Hotel by Rotana,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997711
CENTRO YAS ISLAND-BY ROTANA ABU DHABI,Centro Yas Island-by Rotana Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997730
CHA PAYOM,Cha Payom,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q125873635
CHAIN305,Chain305,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141969910
CHALHOUB,Chalhoub,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CHAMPION CLEANERS,Champion Cleaners,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CHATGPT,ChatGPT,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CHELSEA GARDENS HOTEL APARTMENT,Chelsea Gardens Hotel Apartment,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150699
CHILI'S,Chili's,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CHOITHRAMS,Choithrams,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CINEMA CITY,Cinema City,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CITADINES METRO CENTRAL APARTMENTS,Citadines Metro Central Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150219
CITY AVENUE HOTEL,City Avenue Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997687
CITY CENTER ME'AISEM,City Center Me'aisem,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q25112681
CITY CENTRE AJMAN,City Centre Ajman,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q55607691
CITY FARMS,City Farms,Groceries,AE,,project_category;descriptor_unverified,project:scripts/rules.py
CITY PREMIERE HOTEL APARTMENTS,City Premiere Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150304
CITY PREMIERE MARINA HOTEL APARTMENTS,City Premiere Marina Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150733
CITY SEASONS AL HAMRA HOTEL,City Seasons Al Hamra Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150374
CITY SEASONS TOWERS HOTEL DUBAI,City Seasons Towers Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150440
CITY STAY BEACH HOTEL APARTMENTS,City Stay Beach Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150626
CITY STAY PRIME HOTEL APARTMENT,City Stay Prime Hotel Apartment,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997623
CITY UNIVERSITY AJMAN,City University Ajman,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q15210735
CITY WALK,City Walk,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q115200269
CITYMAX HOTEL AL BARSHA,Citymax Hotel Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150268
CITYMAX HOTEL AL BARSHA AT THE MALL,Citymax Hotel Al Barsha at the Mall,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150269
CITYMAX HOTEL BUR DUBAI,Citymax Hotel Bur Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150414
CITYMAX HOTEL BUSINESS BAY,Citymax Hotel Business Bay,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150296
CITYMAX HOTEL RAS AL KHAIMAH,Citymax Hotel Ras Al Khaimah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150653
CITYMAX SHARJAH,Citymax Sharjah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150602
CLARION SCHOOL L.L.C,Clarion School L.L.C,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088184
"CLARION SCHOOL, DUBAI","Clarion School, Dubai",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q25110780
CLASS HOTEL APARTMENTS,Class Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997612
CLAUDE,Claude,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CLEARMIND,ClearMind,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141775320
CLEARTRIP,Cleartrip,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CLEDOR,Cledor,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140448431
CLEMENCEAU GROUP,Clemenceau Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141734550
CLEVELAND CLINIC ABU DHABI,Cleveland Clinic Abu Dhabi,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
CLICK AIRWAYS,Click Airways,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q2620605
CLIFTON INTERNATIONAL HOTEL,Clifton International Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997722
CLOUDFLARE MIDDLE EAST FZ-LLC,Cloudflare Middle East FZ-LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q113446850
COBBLESTONE ENERGY DMCC,Cobblestone Energy DMCC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q113466767
COLLEGIATE AMERICAN SCHOOL,Collegiate American School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088186
COMFORT INN HOTEL DEIRA,Comfort Inn Hotel Deira,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150491
CONCORDE HOTEL - FUJAIRAH,Concorde Hotel - Fujairah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150638
CONRAD ABU DHABI ETIHAD TOWERS,Conrad Abu Dhabi Etihad Towers,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150180
CONRAD DUBAI,Conrad Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q550379
CONSOLIDATED ENTERPRISES - CONVOY,Consolidated Enterprises - Convoy,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q73998153
CONTINENTAL CLUB PROPERTY,Continental Club Property,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141679360
COPTHORNE AIRPORT HOTEL,Copthorne Airport Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150502
COPTHORNE HOTEL DUBAI,Copthorne Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150481
COPTHORNE HOTEL SHARJAH,Copthorne Hotel Sharjah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150595
CORAL DUBAI DEIRA HOTEL,Coral Dubai Deira Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150533
CORNICHE HOSPITAL,Corniche Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q30254311
CORNICHE HOTEL ABU DHABI,Corniche Hotel Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150378
COSMOPOINTS LOYALTY TECH LTD,Cosmopoints Loyalty Tech Ltd,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141665244
COSTA COFFEE,Costa Coffee,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
COURSERA,Coursera,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
"COURTYARD BY MARRIOTT AL BARSHA, DUBAI","Courtyard by Marriott Al Barsha, Dubai",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150261
"COURTYARD BY MARRIOTT WORLD TRADE CENTER, ABU DHABI","Courtyard by Marriott World Trade Center, Abu Dhabi",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150368
COVAZE,Covaze,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141901311
CRAFIXX,Crafixx,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141459027
CREATIVE CITY,Creative City,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5183501
"CREDENCE HIGH SCHOOL, DUBAI","Credence High School, Dubai",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q55608544
CRESCENT ENGLISH SCHOOL,Crescent English School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088187
CRICKSLAB,Crickslab,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141164285
CRISTAL HOTEL ABU DHABI,Cristal Hotel Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150369
CROWNE PLAZA ABU DHABI,Crowne Plaza Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150373
CROWNE PLAZA ABU DHABI YAS ISLAND,Crowne Plaza Abu Dhabi Yas Island,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150671
CROWNE PLAZA DUBAI,Crowne Plaza Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856031
CROWNE PLAZA DUBAI APARTMENTS,Crowne Plaza Dubai Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150352
CROWNE PLAZA DUBAI DEIRA,Crowne Plaza Dubai Deira,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150549
CROWNE PLAZA DUBAI FESTIVAL CITY,Crowne Plaza Dubai Festival City,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150449
CROWNE PLAZA DUBAI MARINA,Crowne Plaza Dubai Marina,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150718
CROWNE PLAZA JUMEIRAH DUBAI,Crowne Plaza Jumeirah Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150392
CRYPTO RAVEN,Crypto Raven,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q126167348
CURTIN UNIVERSITY DUBAI,Curtin University Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q111263363
CYLUNOR,Cylunor,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139567746
D24 FINTECH GROUP,D24 Fintech Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141006142
DEWA,DEWA,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DEWA ACADEMY,DEWA Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089008
DHL,DHL,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DIA HOLDING,DIA Holding,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q142068873
DMDC GROUP,DMDC Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141818533
DP WORLD,DP World,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1154956
DPS ACADEMY,DPS Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q18112045
DUBZ,DUBZ,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q142027748
DAISO,Daiso,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DALMA MALL,Dalma Mall,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q5211513
DAMAC,Damac,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DAMAC MAISON CANAL VIEWS,Damac Maison Canal Views,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111151469
DAMAC MAISON COUR JARDIN,Damac Maison Cour Jardin,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150300
DAMAC MAISON DISTINCTION,Damac Maison Distinction,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150307
DAMAC MAISON DUBAI MALL STREET,Damac Maison Dubai Mall Street,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150329
"DAMAN, NATIONAL HEALTH INSURANCE COMPANY","Daman, National Health Insurance Company",Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5211937
DAMAS,Damas,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DANA GROUP,Dana Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q25041220
DANAT AL AIN RESORT,Danat Al Ain Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150246
DANAT AL EMARAT WOMEN & CHILDREN’S HOSPITAL,Danat Al Emarat Women & Children’s Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q5214934
DANAT JEBEL DHANNA RESORT,Danat Jebel Dhanna Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150686
DANUBE HOME,Danube Home,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DAR AL MAREFA SCHOOL,Dar Al Marefa School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088189
DAR AL SHIFAA HOSPITAL,Dar Al Shifaa Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q5221867
DARB,Darb,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DECATHLON,Decathlon,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DECKMETRIC,Deckmetric,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139738053
DECURITY,Decurity,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140554498
DEEPSOLVE,DeepSolve,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139822841
DEFAULTS EXPOSED,Defaults Exposed,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141755309
DEIRA CITY CENTRE,Deira City Centre,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q4037155
DEIRA INTERNATIONAL SCHOOL,Deira International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088191
DEIRA PRIVATE SCHOOL,Deira private school,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088193
DELHI PRIVATE SCHOOL,Delhi Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5253786
DELIVEROO,Deliveroo,Food_Dining,AE,,project_category;descriptor_unverified,project:scripts/rules.py
DELMON HOTEL,Delmon Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150500
"DELTA HOTELS BY MARRIOTT JUMEIRAH BEACH, DUBAI","Delta Hotels by Marriott Jumeirah Beach, Dubai",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150720
DENNY'S,Denny's,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DESERT ISLANDS RESORT & SPA BY ANANTARA,Desert Islands Resort & Spa by Anantara,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150701
DEUTSCHE BABCOCK MIDDLE EAST,Deutsche Babcock Middle East,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q3024834
DHAFRA BEACH HOTEL - PET FRIENDLY,Dhafra Beach Hotel - Pet Friendly,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150685
DILOGIC,Dilogic,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q130629567
DISNEY+,Disney+,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DIVINE SANSAR,Divine Sansar,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q138748884
DNATA TRAVEL,Dnata Travel,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DOFREEZE,Dofreeze,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140402854
DOLPHIN AIR,Dolphin Air,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q3712742
DOLPHIN ENERGY,Dolphin Energy,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5289621
DOMINO'S,Domino's,Food_Dining,AE,,project_category;descriptor_unverified,project:scripts/rules.py
DONATELLO HOTEL,Donatello Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150256
DORUS HOTEL,Dorus Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150531
DOTNOT,Dotnot,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140312156
DOUBLETREE BY HILTON ABU DHABI YAS ISLAND RESIDENCES,DoubleTree by Hilton Abu Dhabi Yas Island Residences,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q131452897
DOUBLETREE BY HILTON DUBAI - BUSINESS BAY,DoubleTree by Hilton Dubai - Business Bay,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q66437370
DOUBLETREE BY HILTON DUBAI - JUMEIRAH BEACH,DoubleTree by Hilton Dubai - Jumeirah Beach,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q50308536
DOUBLETREE BY HILTON DUBAI AL JADAF,DoubleTree by Hilton Dubai Al Jadaf,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q110533201
DOUBLETREE BY HILTON DUBAI M SQUARE HOTEL & RESIDENCES,DoubleTree by Hilton Dubai M Square Hotel & Residences,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150433
DOUBLETREE BY HILTON DUBAI PORT SAEED,DoubleTree by Hilton Dubai Port Saeed,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150517
DOUBLETREE BY HILTON FUJAIRAH CITY,DoubleTree by Hilton Fujairah City,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q130530561
DOUBLETREE BY HILTON HOTEL AND RESIDENCES DUBAI – AL BARSHA,DoubleTree by Hilton Hotel and Residences Dubai – Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111399889
DOUBLETREE BY HILTON RAS AL KHAIMAH,DoubleTree by Hilton Ras Al Khaimah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150654
DOUBLETREE BY HILTON RESORT & SPA MARJAN ISLAND,DoubleTree by Hilton Resort & Spa Marjan Island,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q33123648
DOUBLETREE BY HILTON SHARJAH WATERFRONT HOTEL & RESIDENCES,DoubleTree by Hilton Sharjah Waterfront Hotel & Residences,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q130726121
DOVECOTE GREEN PRIMARY SCHOOL,Dovecote Green Primary School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088196
DRAGON MARKET,Dragon Market,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q124504741
DREAM PALACE HOTEL,Dream Palace Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111115159
DROPBOX,Dropbox,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DUBAI AEROSPACE ENTERPRISE,Dubai Aerospace Enterprise,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5310498
DUBAI AMERICAN ACADEMY,Dubai American Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5310502
DUBAI ARABIAN AMERICAN PRIVATE SCHOOL,Dubai Arabian American Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088197
DUBAI BRITISH SCHOOL,Dubai British School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5310510
DUBAI BRITISH SCHOOL JUMEIRAH PARK,Dubai British School Jumeirah Park,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088200
DUBAI CARES,Dubai Cares,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DUBAI CARMEL SCHOOL,Dubai Carmel School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088201
DUBAI COLLEGE,Dubai College,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DUBAI COURTS,Dubai Courts,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DUBAI ECONOMY AND TOURISM,Dubai Economy and Tourism,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DUBAI ENGLISH SPEAKING COLLEGE,Dubai English Speaking College,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5310535
DUBAI ENGLISH SPEAKING SCHOOL,Dubai English Speaking School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088204
DUBAI ENGLISH SPEAKING PRIVATE COLLEGE -BRANCH,Dubai English Speaking private college -branch,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088202
DUBAI FESTIVAL CITY MALL,Dubai Festival City Mall,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q106882588
DUBAI FINANCIAL MARKET,Dubai Financial Market,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1973019
DUBAI FRAME,Dubai Frame,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DUBAI GEM PRIVATE SCHOOL,Dubai Gem Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088205
DUBAI GEM PRIVATE SCHOOL & NURSERY,Dubai Gem Private School & Nursery,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5310545
DUBAI GOLD & COMMODITIES EXCHANGE DMCC,Dubai Gold & Commodities Exchange Dmcc,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q17002324
DUBAI GOVERNMENT,Dubai Government,Government_Fees,AE,,project_category;descriptor_unverified,project:scripts/rules.py
DUBAI GRAND HOTEL BY FORTUNE,Dubai Grand Hotel by Fortune,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150583
DUBAI HEIGHTS ACADEMY,Dubai Heights Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089011
DUBAI HERBAL AND TREATMENT CENTRE,Dubai Herbal and Treatment Centre,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q17000864
DUBAI HILLS MALL,Dubai Hills Mall,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q55610055
DUBAI HOLDING,Dubai Holding,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1262892
DUBAI HOSPITAL,Dubai Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q5310555
DUBAI INSURANCE,Dubai Insurance,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DUBAI INTERNATIONAL ACADEMY,Dubai International Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5310560
DUBAI INTERNATIONAL ACADEMY ALBARSHA,Dubai International Academy AlBarsha,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089043
DUBAI INTERNATIONAL SCHOOL,Dubai International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q17000020
DUBAI INTERNATIONAL TERMINAL HOTEL,Dubai International Terminal Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856052
DUBAI INTERNATIONAL PRIVATE SCHOOL,Dubai International private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088206
DUBAI INTERNATIONAL PRIVATE SCHOOL - BR,Dubai International private School - BR,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088207
DUBAI INVESTMENT FUND,Dubai Investment Fund,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q114877710
DUBAI MALL,Dubai Mall,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q1133309
DUBAI MARINA MALL,Dubai Marina Mall,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q18450188
DUBAI MARRIOTT HARBOUR HOTEL & SUITES,Dubai Marriott Harbour Hotel & Suites,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q2651937
DUBAI MEN'S COLLEGE,Dubai Men's College,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5310585
DUBAI MODERN EDUCATION SCHOOL,Dubai Modern Education School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088208
DUBAI MULTI COMMODITIES CENTRE,Dubai Multi Commodities Centre,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5310589
DUBAI MUNICIPALITY,Dubai Municipality,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DUBAI NATIONAL SCHOOL,Dubai National School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088307
DUBAI NATIONAL SCHOOL ( BRANCH),Dubai National School ( Branch),Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088309
"DUBAI NATIONAL SCHOOL, AL BARSHA","Dubai National School, Al Barsha",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5310590
"DUBAI NATIONAL SCHOOL, AL TWAR","Dubai National School, Al Twar",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5310591
DUBAI OPERA,Dubai Opera,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DUBAI PALM HOTEL,Dubai Palm Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150544
DUBAI PARKS AND RESORTS,Dubai Parks and Resorts,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DUBAI POLICE,Dubai Police,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DUBAI POST,Dubai Post,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q108864321
DUBAI PROPERTIES,Dubai Properties,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DUBAI ROYAL AIR WING,Dubai Royal Air Wing,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q5310603
DUBAI SAFARI PARK,Dubai Safari Park,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DUBAI SCHOLARS PRIVATE SCHOOL,Dubai Scholars Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5310602
DUBAI SCHOOL OF DENTAL MEDICINE,Dubai School of Dental Medicine,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q19818743
DUBAI TAXI,Dubai Taxi,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
"DUKES THE PALM, A ROYAL HIDEAWAY HOTEL","Dukes The Palm, a Royal Hideaway Hotel",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150207
DUNECREST AMERICAN SCHOOL,Dunecrest American School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089046
DUNKIN,Dunkin,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DUSIT PRINCESS RESIDENCE - DUBAI MARINA,Dusit Princess Residence - Dubai Marina,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150740
DUSIT THANI ABU DHABI,Dusit Thani Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997603
DUSIT THANI DUBAI,Dusit Thani Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q115152710
DUSITD2 KENZ HOTEL DUBAI,Dusitd2 Kenz Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150217
DWIGHT SCHOOL DUBAI,Dwight school Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089049
EDGE GROUP,EDGE Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q64732479
ENOC,ENOC,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
EVPLUS.AE,EVPlus.ae,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139990146
EAGLE HILLS PROPERTIES,Eagle Hills Properties,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q60752215
EASTERN SKYJETS,Eastern SkyJets,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q5330469
EASYHOTEL JEBEL ALI,EasyHotel Jebel Ali,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150688
ECLIPSE BOUTIQUE SUITES,Eclipse Boutique Suites,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150371
ECOLOG INTERNATIONAL,Ecolog International,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1282039
EDGE CREEKSIDE HOTEL,Edge Creekside Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150479
EDGEERP CONSULTING,EdgeERP Consulting,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140123058
EDUCATIONAL SERVICES OVERSEAS LIMITED,Educational Services Overseas Limited,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5341261
EDUTECH,Edutech,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5341344
EJARI,Ejari,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
EKAR,Ekar,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
"ELEMENT AL JADDAF, DUBAI","Element Al Jaddaf, Dubai",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150406
"ELEMENT ME'AISAM, DUBAI","Element Me'aisam, Dubai",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997741
ELITE BYBLOS HOTEL,Elite Byblos Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150262
ELITE ENGLISH SCHOOL,Elite English School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088314
EMAAR COMMUNITY MANAGEMENT,Emaar Community Management,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
EMAAR PROPERTIES,Emaar Properties,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1153463
EMARAT,Emarat,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
EMAX,Emax,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
EMBASSY SUITES BY HILTON DUBAI BUSINESS BAY,Embassy Suites by Hilton Dubai Business Bay,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q130736677
EMERALD PALACE KEMPINSKI DUBAI,Emerald Palace Kempinski Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q65226036
EMERY,Emery,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141912232
EMICOOL,Emicool,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
EMIRATES,Emirates,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q180432
EMIRATES AIRLINE,Emirates Airline,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
EMIRATES AVIATION UNIVERSITY,Emirates Aviation University,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q30294768
EMIRATES FLIGHT CATERING,Emirates Flight Catering,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5372567
EMIRATES FLIGHT TRAINING ACADEMY,Emirates Flight Training Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q55075134
EMIRATES FUTURE INTERNATIONAL ACADEMY,Emirates Future International Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5372569
EMIRATES GLOBAL ALUMINIUM,Emirates Global Aluminium,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4119913
EMIRATES GRAND HOTEL APARTMENTS,Emirates Grand Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150342
EMIRATES INTERNATIONAL SCHOOL - MEADOWS,Emirates International School - Meadows,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q18353466
EMIRATES INTERNATIONAL PRIVATE SCHOOL L.L.C,Emirates International private School L.L.C,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088316
EMIRATES NUCLEAR ENERGY CORPORATION,Emirates Nuclear Energy Corporation,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q20018425
EMIRATES PALACE,Emirates Palace,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q1337845
EMIRATES PARK RESORT,Emirates Park Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997732
EMIRATES POST,Emirates Post,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
EMIRATES RED CRESCENT,Emirates Red Crescent,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
EMIRATES SKYCARGO,Emirates SkyCargo,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q1317487
EMIRATES STARS HOTEL APARTMENTS DUBAI,Emirates Stars Hotel Apartments Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150584
EMIRATES STARS HOTEL APARTMENTS SHARJAH,Emirates Stars Hotel Apartments Sharjah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997698
EMPOWER,Empower,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
EMPTYJET,EmptyJet,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141664302
ENERGETECH TRADING DMCC,EnergeTech Trading DMCC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q113466824
ENGLISH COLLEGE DUBAI,English College Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5378215
ENGLISH LANGUAGE PRIVATE SCHOOL,English Language Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088318
"ENGLISH LANGUAGE SCHOOL, DUBAI","English Language School, Dubai",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5378308
EQUITI GROUP,Equiti Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q133827174
EQUITI SECURITIES CURRENCIES BROKERS LLC,Equiti Securities Currencies Brokers LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141519939
ESTATEREELS,EstateReels,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141362988
ETIHAD AIRWAYS,Etihad Airways,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ETIHAD WATER AND ELECTRICITY,Etihad Water and Electricity,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ETISALAT,Etisalat,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ETISALAT UNIVERSITY COLLEGE,Etisalat University College,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5404636
EUROPCAR,Europcar,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
EVENTKRAFT,Eventkraft,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139695479
EWAN AJMAN SUITES HOTEL,Ewan Ajman Suites Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997717
EWAN TOWER HOTEL APARTMENTS,Ewan Tower Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997715
EXECUTIVE LIMO LUXURY CAR TRANSPORT LLC,Executive Limo Luxury Car Transport LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q137260189
EXECUTIVE SUITES BY MOUROUJ,Executive Suites by Mourouj,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856011
EXPEDIA,Expedia,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
EZERA DIGITAL TECHNOLOGIES FZCO,Ezera Digital Technologies FZCO,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141646120
FEWA,FEWA,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
FACEBOOK ADS,Facebook Ads,Others,AE,,project_category;descriptor_unverified,project:scripts/rules.py
FACES,Faces,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
FAIR GROW GENERAL TRADING LLC,Fair Grow General Trading LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141512943
FAIRGREEN INTERNATIONAL SCHOOL,Fairgreen International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089051
FAIRMONT AJMAN,Fairmont Ajman,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150612
FAIRMONT BAB AL BAHR,Fairmont Bab Al Bahr,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111151480
FAIRMONT DUBAI,Fairmont Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150361
FAIRMONT FUJAIRAH BEACH RESORT,Fairmont Fujairah Beach Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150663
FAIRMONT THE PALM,Fairmont The Palm,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q7733117
FALCON AVIATION SERVICES,Falcon Aviation Services,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q5431731
FALCON EXPRESS CARGO AIRLINES,Falcon Express Cargo Airlines,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q3738590
FALCON TECHNOLOGIES INTERNATIONAL,Falcon Technologies International,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q137652188
FANDOMWIRE,FandomWire,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140355827
FASTTRACK,Fasttrack,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
FEDEX,FedEx,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
FEDERAL TAX AUTHORITY,Federal Tax Authority,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
FENMAN,Fenman,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q110897953
FERRARI WORLD,Ferrari World,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
FILINGS.AE,Filings.AE,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141727930
FIRST ABU DHABI BANK,First Abu Dhabi Bank,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q29124183
FIRST CENTRAL HOTEL SUITES,First Central Hotel Suites,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150216
FIRSTCRY,FirstCry,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
FITNESS FIRST,Fitness First,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
FITNESS TIME,Fitness Time,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
"FIVE - PALM JUMEIRAH, BY QUINTESSENTIAL QUARTERS","Five - Palm Jumeirah, by Quintessential Quarters",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150204
FIVE GUYS,Five Guys,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
FIVE JUMEIRAH VILLAGE,Five Jumeirah Village,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997745
FLORA AL BARSHA HOTEL AT THE MALL,Flora Al Barsha Hotel at The Mall,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997621
FLORA CREEK DELUXE HOTEL APARTMENTS,Flora Creek Deluxe Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150474
FLORA INN HOTEL DUBAI AIRPORT,Flora Inn Hotel Dubai Airport,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150532
FLORIDA AL SOUQ HOTEL (PREVIOUSLY KNOWN FLORA AL SOUQ HOTEL),Florida Al Souq Hotel (Previously Known Flora Al Souq Hotel),Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997658
FLORIDA CITY HOTEL APARTMENTS,Florida City Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997660
FLYNAS,Flynas,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
FOREMARKE SCHOOL,Foremarke School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088321
"FORM HOTEL DUBAI, DUBAI, A MEMBER OF DESIGN HOTELSTM","Form Hotel Dubai, Dubai, a Member of Design HotelsTM",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997644
FORMENZO,Formenzo,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140135545
FORTUNE DEIRA HOTEL,Fortune Deira Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856050
FORTUNE GRAND HOTEL,Fortune Grand Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150540
FORTUNE HOTEL DEIRA,Fortune Hotel Deira,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111111802
FORTUNE KARAMA HOTEL,Fortune Karama Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150403
FORTUNE PARK HOTEL,Fortune Park Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997734
FORTUNE PEARL HOTEL,Fortune Pearl Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150548
FORTUNE PLAZA HOTEL,Fortune Plaza Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997692
FOUR POINTS BY SHERATON BUR DUBAI,Four Points by Sheraton Bur Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150445
FOUR POINTS BY SHERATON DOWNTOWN DUBAI,Four Points by Sheraton Downtown Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150419
FOUR POINTS BY SHERATON SHARJAH,Four Points by Sheraton Sharjah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150600
FOUR POINTS BY SHERATON SHEIKH ZAYED ROAD DUBAI,Four Points by Sheraton Sheikh Zayed Road Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q4263811
FOUR SEASONS HOTEL ABU DHABI AT AL MARYAH ISLAND,Four Seasons Hotel Abu Dhabi at Al Maryah Island,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150571
FOUR SEASONS HOTEL DUBAI INTERNATIONAL FINANCIAL CENTRE,Four Seasons Hotel Dubai International Financial Centre,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150349
FOUR SEASONS RESORT DUBAI AT JUMEIRAH BEACH,Four Seasons Resort Dubai at Jumeirah Beach,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111151478
FRASER SUITES DUBAI,Fraser Suites Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150234
FUJAIRAH CITY CENTRE,Fujairah City Centre,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q17003358
FUJAIRAH ROTANA RESORT & SPA - AL AQAH BEACH,Fujairah Rotana Resort & Spa - Al Aqah Beach,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150660
FURTHERMARKETS,FurtherMarkets,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141737572
FXPRO,FxPro,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5511172
FXTRUSTS,FxTrusts,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139512141
GCC DOMESTIC,GCC Domestic,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141150505
GCC EXCHANGE,GCC Exchange,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q60746711
GDRFA,GDRFA,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
GEMS ALBARSHA NATIONAL SCHOOL FOR BOYS,GEMS AlBarsha National School for Boys,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088323
"GEMS AMERICAN ACADEMY, ABU DHABI","GEMS American Academy, Abu Dhabi",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5513151
GEMS DUBAI AMERICAN ACADEMY,GEMS Dubai American Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088331
GEMS EDUCATION,GEMS Education,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
GEMS FOUNDERS SCHOOL,GEMS Founders School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088336
GEMS FOUNDERS SCHOOL MIZHAR,GEMS Founders School Mizhar,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089052
GEMS HERITAGE  INDIAN SCHOOL,GEMS Heritage  Indian School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088340
GEMS INTERNATIONAL SCHOOL- AL KHAIL,GEMS International School- Al Khail,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088341
GEMS JUMEIRAH PRIMARY SCHOOL,GEMS Jumeirah Primary School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088344
GEMS METROPOLE SCHOOL-,GEMS Metropole School-,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088346
GEMS MODERN ACADEMY,GEMS Modern Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5310587
GEMS NEW MILLENNIUM SCHOOL L.L.C,GEMS New Millennium School L.L.C,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088348
GEMS OUR OWN ENGLISH HIGH SCHOOL,GEMS Our Own English High School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088349
GEMS OUR OWN INDIAN SCHOOL,GEMS Our Own Indian School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088354
GEMS ROYAL DUBAI SCHOOL,GEMS Royal Dubai School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088358
GEMS UNITED SCHOOL,GEMS United School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088181
GEMS WELLINGTON ACADEMY (BRANCH),GEMS Wellington Academy (Branch),Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088360
GEMS WELLINGTON ACADEMY- AL KHAIL,GEMS Wellington Academy- Al Khail,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088362
GEMS WELLINGTON INTERNATIONAL SCHOOL,GEMS Wellington International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5513157
GEMS WELLINGTON PRIMARY SCHOOL,GEMS Wellington Primary School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088365
GEMS WINCHESTER SCHOOL,GEMS Winchester School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088367
GEMS WORLD ACADEMY,GEMS World Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5513158
GEOTAX,GEOTAX,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139935014
GIG GULF,GIG Gulf,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
GMC HOSPITAL AJMAN,GMC Hospital Ajman,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q5513737
GR IT SERVICES,GR IT Services,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139795818
GALADARI BROTHERS,Galadari Brothers,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q85850650
GALADARI EQUIPMENT SOLUTIONS,Galadari Equipment Solutions,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141611428
GAZEBO,Gazebo,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
GEANT,Geant,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
GEM WALLET LLC,Gem Wallet LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140942945
GEMS AL BARSHA NATIONAL SCHOOL FOR GIRLS,Gems Al Barsha National School For Girls,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088325
GEMS FIRSTPOINT SCHOOL,Gems FirstPoint School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088334
GERMAN INTERNATIONAL SCHOOL DUBAI,German International School Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088370
GEVORA HOTEL,Gevora Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q401098
GIGMAP,GigMap,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140502457
GILANI MOBILITY,Gilani Mobility,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139591253
GITHUB,GitHub,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
GLOBAL HOTEL ALLIANCE,Global Hotel Alliance,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q16840235
GLOBAL INDIAN INTERNATIONAL SCHOOL L.L.C,Global Indian International School L.L.C,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089014
GLOBAL INDIAN SCHOOL AJMAN,Global Indian School Ajman,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q85769315
GLOBE SOCCER DWC LLC,Globe Soccer DWC LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141852867
GOAT SKINS,Goat Skins,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q133869308
GOLD'S YACHT,Gold's Yacht,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141754050
GOLDEN SANDS HOTEL APARTMENTS,Golden Sands Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111111805
GOLDEN SANDS HOTEL SHARJAH,Golden Sands Hotel Sharjah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150585
GOLDEN STAY VACATION CONTINENTAL TOWER,Golden Stay Vacation Continental Tower,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997740
GOLDEN TULIP DEIRA,Golden Tulip Deira,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150497
GOLDEN TULIP DOWNTOWN ABU DHABI,Golden Tulip Downtown Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150376
GOLDEN TULIP MEDIA HOTEL,Golden Tulip Media Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150228
GOOBII,Goobii,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141775679
GOOGLE,Google,Digital_Subscriptions,AE,,project_category;descriptor_unverified,project:scripts/rules.py
GOOGLE (TEMPORARY HOLD),Google (temporary hold),Digital_Subscriptions,AE,,project_category;descriptor_unverified,project:scripts/rules.py
GOOGLE ONE,Google One,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
GRAMMAR SCHOOL,Grammar School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088373
"GRAMMAR SCHOOL, DUBAI","Grammar School, Dubai",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q55612895
GRAND CENTRAL HOTEL,Grand Central Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150529
GRAND COSMOPOLITAN HOTEL,Grand Cosmopolitan Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150250
GRAND EXCELSIOR HOTEL AL BARSHA,Grand Excelsior Hotel Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997620
GRAND EXCELSIOR HOTEL BUR DUBAI,Grand Excelsior Hotel Bur Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150416
GRAND EXCELSIOR HOTEL DEIRA,Grand Excelsior Hotel Deira,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150575
GRAND HEIGHTS HOTEL APARTMENTS,Grand Heights Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997611
GRAND HYATT ABU DHABI HOTEL & RESIDENCES EMIRATES PEARL,Grand Hyatt Abu Dhabi Hotel & Residences Emirates Pearl,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150179
GRAND HYATT DUBAI,Grand Hyatt Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q8017526
GRAND HYATT RESIDENCE,Grand Hyatt Residence,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997642
GRAND MAYFAIR HOTEL,Grand Mayfair Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150489
GRAND MERCURE HOTEL AND RESIDENCES DUBAI AIRPORT,Grand Mercure Hotel and Residences Dubai Airport,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150524
GRAND MILLENNIUM AL WAHDA,Grand Millennium Al Wahda,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150203
GRAND MILLENNIUM AL WAHDA ABU DHABI HOTEL,Grand Millennium Al Wahda Abu Dhabi Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150201
GRAND MILLENNIUM BUSINESS BAY,Grand Millennium Business Bay,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150298
GRAND MILLENNIUM DUBAI,Grand Millennium Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150230
GRAND PLAZA MÖVENPICK MEDIA CITY,Grand Plaza Mövenpick Media City,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150208
GRAND SINA HOTEL,Grand Sina Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997655
GRAND SQUARE HOTEL,Grand Square Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997677
GRAND STAY HOTEL DUBAI,Grand Stay Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150341
GRANDIOSE,Grandiose,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
GRAYTON HOTEL DUBAI,Grayton Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150432
GREAT HARBOUR PETROLEUM,Great Harbour Petroleum,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q131296030
GREEN GUARD CONTRACTING L.L.C,Green Guard Contracting L.L.C,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141603168
GREEN MUBAZZARAH CHALETS,Green Mubazzarah Chalets,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997737
GREENFIELD COMMUNITY SCHOOL,Greenfield Community School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5603956
GREENWOOD INTERNATIONAL SCHOOL,Greenwood International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5605035
GROSVENOR HOUSE A LUXURY COLLECTION HOTEL DUBAI,Grosvenor House a Luxury Collection Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150748
GROUP-IB,Group-IB,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q16471828
GROVIA DIGITAL,Grovia Digital,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141733237
GULF AIR,Gulf Air,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
GULF COURT HOTEL BUSINESS BAY,Gulf Court Hotel Business Bay,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150301
GULF CRAFT,Gulf Craft,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5617478
GULF FOOD INDUSTRIES,Gulf Food Industries,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q137864210
GULF INDIAN HIGH SCHOOL,Gulf Indian High School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5617493
GULF MODEL SCHOOL,Gulf Model School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088375
GYMNATION,GymNation,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
H&M,H&M,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
H. H. SHAIKH RASHID AL MAKTOUM PAKISTANI SCHOOL-DUBAI ( ENGLISH LANG),H. H. Shaikh Rashid Al Maktoum Pakistani School-Dubai ( English Lang),Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088377
HITEK AI,HITEK AI,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141554311
HKZ INTERIOR DECORATION LLC,HKZ Interior Decoration LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141554952
"HABITAT PRIVATE SCHOOL, AL JURF","Habitat Private School, Al Jurf",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q25112696
"HABTOOR GRAND RESORT, AUTOGRAPH COLLECTION","Habtoor Grand Resort, Autograph Collection",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150746
"HABTOOR PLACE DUBAI, LXR HOTELS & RESORTS","Habtoor Place Dubai, LXR Hotels & Resorts",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q99976218
HAFEZ HOTEL APARTMENTS AL RAS METRO STATION,Hafez Hotel Apartments Al Ras Metro Station,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997653
"HALA ARJAAN BY ROTANA, DELUXE HOTEL APARTMENTS","Hala Arjaan by Rotana, Deluxe Hotel Apartments",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150567
HALA INN HOTEL APARTMENTS,Hala Inn Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997718
HAMDAN BIN MOHAMMED SMART UNIVERSITY,Hamdan Bin Mohammed Smart University,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q5644372
HAMPTON BY HILTON DUBAI AIRPORT,Hampton by Hilton Dubai Airport,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150581
HAMPTON BY HILTON DUBAI AL BARSHA,Hampton by Hilton Dubai Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q76620470
HAMPTON BY HILTON DUBAI AL SEEF,Hampton by Hilton Dubai Al Seef,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150454
HAMPTON BY HILTON MARJAN ISLAND,Hampton by Hilton Marjan Island,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q130530756
HAMRIYAH FREE ZONE,Hamriyah Free Zone,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5646373
HARDEE'S,Hardee's,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
HARTLAND INTERNATIONAL SCHOOL,Hartland International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088379
HATTA DAMANI LODGES RESORT,Hatta Damani Lodges Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856075
HATTA FORT HOTEL,Hatta Fort Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q18210518
HATTA SEDR TRAILERS RESORT,Hatta Sedr Trailers Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997719
HAWTHORN SUITES BY WYNDHAM ABU DHABI CITY CENTER,Hawthorn Suites by Wyndham Abu Dhabi City Center,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150564
HEALTHHUB,HealthHub,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
HEALTHPOINT,Healthpoint,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q30314139
HELL'S KITCHEN,Hell's Kitchen,Food_Dining,AE,,type_mapped,http://www.wikidata.org/entity/Q113801611
HERIOT-WATT UNIVERSITY DUBAI,Heriot-Watt University Dubai,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
HERTZ,Hertz,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
HILI RAYHAAN BY ROTANA,Hili Rayhaan by Rotana,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150239
HILTON,Hilton,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
HILTON ABU DHABI YAS ISLAND,Hilton Abu Dhabi Yas Island,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150668
HILTON AL AIN,Hilton Al Ain,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q30525186
HILTON CAPITAL GRAND ABU DHABI,Hilton Capital Grand Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q74527699
HILTON DUBAI AL HABTOOR CITY,Hilton Dubai Al Habtoor City,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q62485477
HILTON DUBAI CREEK,Hilton Dubai Creek,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q7281354
HILTON DUBAI CREEK HOTEL & RESIDENCES,Hilton Dubai Creek Hotel & Residences,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q130617734
HILTON DUBAI JUMEIRAH,Hilton Dubai Jumeirah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q30147522
HILTON DUBAI PALM JUMEIRAH,Hilton Dubai Palm Jumeirah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q141128546
HILTON DUBAI THE WALK,Hilton Dubai The Walk,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q22976715
HILTON GARDEN INN DUBAI AL JADAF CULTURE VILLAGE,Hilton Garden Inn Dubai Al Jadaf Culture Village,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q60732352
HILTON GARDEN INN DUBAI BUSINESS BAY,Hilton Garden Inn Dubai Business Bay,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q130742287
HILTON GARDEN INN DUBAI DEIRA,Hilton Garden Inn Dubai Deira,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150538
HILTON GARDEN INN DUBAI JUMEIRAH,Hilton Garden Inn Dubai Jumeirah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q66660297
"HILTON GARDEN INN DUBAI, MALL AVENUE","Hilton Garden Inn Dubai, Mall Avenue",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q27981667
HILTON GARDEN INN RAS AL KHAIMAH,Hilton Garden Inn Ras Al Khaimah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q64933804
HILTON RAS AL KHAIMAH BEACH RESORT,Hilton Ras Al Khaimah Beach Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q63642510
HIMAYAH KINDERGARTEN FOR EDUCATION - KARAMA,Himayah Kindergarten for Education - Karama,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089069
HIMAYAH SCHOOL FOR EDUCATION BOYS - DEIRA (ABU HAIL),Himayah School for Education Boys - Deira (Abu Hail),Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089068
HIMAYAH SCHOOL FOR EDUCATION GIRLS - AL KARAMA,Himayah School for Education Girls - Al Karama,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088312
HOLIDAY INN ABU DHABI,Holiday Inn Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150190
HOLIDAY INN ABU DHABI DOWNTOWN,Holiday Inn Abu Dhabi Downtown,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150372
HOLIDAY INN BUR DUBAI - EMBASSY DISTRICT,Holiday Inn Bur Dubai - Embassy District,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150451
HOLIDAY INN DUBAI AL BARSHA,Holiday Inn Dubai Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150258
HOLIDAY INN DUBAI AL-MAKTOUM AIRPORT,Holiday Inn Dubai Al-Maktoum Airport,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150679
HOLIDAY INN DUBAI FESTIVAL CITY,Holiday Inn Dubai Festival City,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150458
HOLIDAY INN EXPRESS DUBAI AIRPORT,Holiday Inn Express Dubai Airport,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150537
HOLIDAY INN EXPRESS DUBAI INTERNET CITY,Holiday Inn Express Dubai Internet City,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150220
HOLIDAY INN EXPRESS DUBAI SAFA PARK,Holiday Inn Express Dubai Safa Park,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111151487
"HOLIDAY INN EXPRESS DUBAI, JUMEIRAH","Holiday Inn Express Dubai, Jumeirah",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150390
HOLLAND AND KNIGHT (UNITED ARAB EMIRATES),Holland and Knight (United Arab Emirates),Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139771217
HOME BOX,Home Box,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
HOME CENTRE,Home Centre,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
HORIZON INTERNATIONAL SCHOOL - LLC,Horizon International School - LLC,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088381
HORIZONS ENGLISH SCHOOL,Horizons English School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088383
HOTEL INDIGO DUBAI DOWNTOWN,Hotel Indigo Dubai Downtown,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150326
HOTEL RIU DUBAI,Hotel Riu Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q135919371
HOWARD JOHNSON PLAZA BY WYNDHAM DUBAI DEIRA,Howard Johnson Plaza By Wyndham Dubai Deira,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150515
HUES BOUTIQUE HOTEL,Hues Boutique Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150551
HUNTICA,Huntica,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141133865
HYATT,Hyatt,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
HYATT CENTRIC JUMEIRAH DUBAI,Hyatt Centric Jumeirah Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q136163135
HYATT PLACE DUBAI AL RIGGA,Hyatt Place Dubai Al Rigga,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150530
HYATT PLACE DUBAI JUMEIRAH,Hyatt Place Dubai Jumeirah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150395
HYATT PLACE DUBAI WASL DISTRICT,Hyatt Place Dubai Wasl District,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150523
HYATT PLACE DUBAI/BANIYAS SQUARE,Hyatt Place Dubai/Baniyas Square,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150470
HYATT REGENCY DUBAI,Hyatt Regency Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q5952885
HYATT REGENCY DUBAI CREEK HEIGHTS,Hyatt Regency Dubai Creek Heights,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150434
HYATT REGENCY GALLERIA RESIDENCE DUBAI,Hyatt Regency Galleria Residence Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997682
HYDROPOLIS,Hydropolis,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q1372419
IAT,IAT,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089031
ICP,ICP,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
IKEA,IKEA,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
IMG WORLDS OF ADVENTURE,IMG Worlds of Adventure,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
INAS EXIM LLC,INAS ExIm LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q138684973
INSEAT,INSEAT,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140385457
IP & IT CONSULTANTS,IP & IT Consultants,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q136676362
ISS RELOCATIONS,ISS Relocations,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140590781
ITSS L.L.C-FZ,ITSS L.L.C-FZ,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141148059
IVI MIDDLE EAST FERTILITY CLINIC,IVI Middle East Fertility Clinic,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q50036763
IBIS ABU DHABI GATE,Ibis Abu Dhabi Gate,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150195
IBIS AL BARSHA,Ibis Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856015
IBIS AL RIGGA DUBAI,Ibis Al Rigga Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150514
IBIS DEIRA CITY CENTRE DUBAI,Ibis Deira City Centre Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150490
IBIS FUJAIRAH,Ibis Fujairah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150635
IBIS MALL OF THE EMIRATES DUBAI,Ibis Mall of The Emirates Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150263
IBIS ONE CENTRAL,Ibis One Central,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150356
IBIS STYLES DRAGON MART DUBAI,Ibis Styles Dragon Mart Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150462
IBIS STYLES DUBAI AIRPORT HOTEL,Ibis Styles Dubai Airport Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150526
IBIS STYLES DUBAI JUMEIRA,Ibis Styles Dubai Jumeira,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150387
IBIS STYLES SHARJAH,Ibis Styles Sharjah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856067
IBIS WORLD TRADE CENTRE DUBAI,Ibis World Trade Centre Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150359
IBN BATTUTA MALL,Ibn Battuta Mall,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q511504
ICADEMY MIDDLE EAST FZ.LLC,Icademy Middle East FZ.LLC,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088422
ICON HOTEL APARTMENTS,Icon Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997686
IGNITE SCHOOL,Ignite School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089054
INBUSINESS ADVISORY DMCC,InBusiness Advisory DMCC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140008069
"INDIAN SCHOOL, RAS AL-KHAIMAH","Indian School, Ras al-Khaimah",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q6021529
INFORMA MIDDLE EAST,Informa Middle East,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q22809043
INSTASHOP,Instashop,Groceries,AE,,project_category;descriptor_unverified,project:scripts/rules.py
INTEL (UNITED ARAB EMIRATES),Intel (United Arab Emirates),Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535247
INTERCONTINENTAL ABU DHABI,InterContinental Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150181
INTERCONTINENTAL DUBAI FESTIVAL CITY,InterContinental Dubai Festival City,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150450
INTERCONTINENTAL DUBAI MARINA,InterContinental Dubai Marina,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150723
INTERCONTINENTAL FUJAIRAH RESORT,InterContinental Fujairah Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150658
INTERCONTINENTAL RESIDENCE SUITES DUBAI FESTIVAL CITY,InterContinental Residence Suites Dubai Festival City,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150459
INTERCITYHOTEL DUBAI JADDAF WATERFRONT,IntercityHotel Dubai Jaddaf Waterfront,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997648
INTERNATIONAL ACADEMIC SCHOOL,International Academic School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088384
INTERNATIONAL CONCEPT FOR EDUCATION,International Concept for Education,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q65032794
INTERNATIONAL INDIAN SCHOOL AJMAN,International Indian School Ajman,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q17064158
INTERNATIONAL PETROLEUM INVESTMENT COMPANY,International Petroleum Investment Company,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1666805
INTERNATIONAL SCHOOL OF ARTS & SCIENCES,International School of Arts & Sciences,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088387
INTERNATIONAL SCHOOL OF CHOUEIFAT,International School of Choueifat,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4118558
INTERNATIONAL SCHOOL OF CREATIVE SCIENCE,International School of Creative Science,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088390
INVESTMENT CORPORATION OF DUBAI,Investment Corporation of Dubai,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q3153926
"IRANIAN HOSPITAL, DUBAI","Iranian Hospital, Dubai",Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q20707857
IRANIAN KHADIJE KOBRA SCHOOL,Iranian Khadije Kobra School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088392
IRANIAN SALMAN FARSI BOYS SCHOOL,Iranian Salman Farsi Boys School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088395
IRANIAN TOWHEED BOYS SCHOOL,Iranian Towheed Boys School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088400
IRANIAN TOWHEED GIRLS SCHOOL,Iranian Towheed Girls School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088397
IRASH LLC,Irash LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q136893009
ISHTAR AIRLINES,Ishtar Airlines,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q5977169
ISLAMIA ENGLISH SCHOOL,Islamia English School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q6082150
ISLAMIC SCHOOL FOR TRAINING & EDUCATION,Islamic School for Training & Education,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088405
ITTIHAD UNIVERSITY,Ittihad University,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q6095050
IVORY GRAND HOTEL APARTMENTS,Ivory Grand Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150267
J5 HOTELS BUR DUBAI,J5 Hotels Bur Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150435
J5 HOTELS PORT SAEED DUBAI,J5 Hotels Port Saeed Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150509
J5 RIMAL HOTEL APARTMENTS,J5 Rimal Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997684
J5 VILLAS HOLIDAY HOMES - BARSHA GARDENS,J5 Villas Holiday Homes - Barsha Gardens,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997614
JA BEACH HOTEL,JA Beach Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150684
JA HATTA FORT HOTEL,JA Hatta Fort Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150618
JA LAKE VIEW HOTEL,JA Lake View Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150681
JA OASIS BEACH TOWER APARTMENTS,JA Oasis Beach Tower Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150721
JA OCEAN VIEW HOTEL,JA Ocean View Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150710
JA PALM TREE COURT,JA Palm Tree Court,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150682
JAUPIN,JAUPIN,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141795905
JMH GROUP,JMH Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q18352755
JSS INTERNATIONAL SCHOOL LLC,JSS International School LLC,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088413
JSS PRIVATE SCHOOL LLC,JSS PRIVATE SCHOOL LLC,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088417
JSS PRIVATE SCHOOL,JSS Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q16934981
JW MARRIOTT HOTEL DUBAI,JW Marriott Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q20390119
JW MARRIOTT MARQUIS DUBAI,JW Marriott Marquis Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q1244144
JACOB'S GARDEN HOTEL,Jacob's Garden Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856036
JANNAH BURJ AL SARAB,Jannah Burj Al Sarab,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997688
JANNAH PLACE DUBAI MARINA,Jannah Place Dubai Marina,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150705
JAPANESE SCHOOL,Japanese School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088407
JAZEERA AIRWAYS,Jazeera Airways,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
JEBEL ALI SCHOOL,Jebel Ali School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088412
JEDDA STAR,Jedda Star,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141150646
JOLLIBEE,Jollibee,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
JONRAD HOTEL,Jonrad Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997674
JOSÉ BY PIZARRO,José by Pizarro,Food_Dining,AE,,type_mapped,http://www.wikidata.org/entity/Q131287753
JOYALUKKAS,Joyalukkas,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
JUBLO,Jublo,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q96602145
JULPHAR,Julphar,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6310404
JUMBO ELECTRONICS,Jumbo Electronics,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
JUMEIRA BACCALAUREATE SCHOOL,Jumeira Baccalaureate School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q16255363
JUMEIRA ROTANA HOTEL DUBAI,Jumeira Rotana Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997632
JUMEIRA ROTANA – DUBAI,Jumeira Rotana – Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150363
JUMEIRAH,Jumeirah,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
JUMEIRAH AL NASEEM,Jumeirah Al Naseem,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150278
JUMEIRAH AL QASR,Jumeirah Al Qasr,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150275
JUMEIRAH BEACH HOTEL,Jumeirah Beach Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q647585
JUMEIRAH COLLEGE,Jumeirah College,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
JUMEIRAH CREEKSIDE HOTEL,Jumeirah Creekside Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150466
JUMEIRAH DAR AL MASYAF,Jumeirah Dar Al Masyaf,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150272
JUMEIRAH EMIRATES TOWERS,Jumeirah Emirates Towers,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150351
JUMEIRAH ENGLISH SPEAKING SCHOOL,Jumeirah English Speaking School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q6310949
JUMEIRAH ENGLISH SPEAKING SCHOOL (BR),Jumeirah English Speaking School (Br),Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088419
JUMEIRAH LAKES TOWERS FREE ZONE,Jumeirah Lakes Towers Free Zone,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q17065767
JUMEIRAH LIVING MARINA GATE,Jumeirah Living Marina Gate,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997743
"JUMEIRAH LIVING WORLD TRADE CENTRE RESIDENCE, SUITES AND HOTEL APARTMENTS","Jumeirah Living World Trade Centre Residence, Suites and Hotel Apartments",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150385
JUMEIRAH MINA A'SALAM,Jumeirah Mina A'Salam,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150277
JUMEIRAH ZABEEL SARAY,Jumeirah Zabeel Saray,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q6310960
JUMEIRAH AT SAADIYAT ISLAND RESORT,Jumeirah at Saadiyat Island Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150675
JUSTLIFE,Justlife,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
KFC,KFC,Food_Dining,AE,,project_category;descriptor_unverified,project:scripts/rules.py
KTS GLOBAL,KTS Global,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q138189229
KAMAL BUSINESS HUB,Kamal Business Hub,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q124071543
KANG PACIFIC AIRLINES,Kang Pacific Airlines,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q6362271
KARAK HOUSE,Karak House,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
KEETA,Keeta,Food_Dining,AE,,project_category;descriptor_unverified,project:scripts/rules.py
KEMPINSKI HOTEL & RESIDENCES PALM JUMEIRAH,Kempinski Hotel & Residences Palm Jumeirah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150750
KEMPINSKI HOTEL AJMAN,Kempinski Hotel Ajman,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q6387088
KEMPINSKI HOTEL MALL OF THE EMIRATES,Kempinski Hotel Mall of the Emirates,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q6387092
KENT COLLEGE DUBAI,Kent College Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088425
KHALIDIYA HOTEL,Khalidiya Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150197
KHALIDIYA PALACE RAYHAAN BY ROTANA,Khalidiya Palace Rayhaan by Rotana,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150176
KHALIDIYAH MALL,Khalidiyah Mall,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q6399626
KHALIFA UNIVERSITY,Khalifa University,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
KHALIFA UNIVERSITY OF SCIENCE TECHNOLOGY AND RESEARCH - SHARJAH CAMPUS,Khalifa University of Science Technology and Research - Sharjah Campus,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q39793447
KHALIFA BIN ZAYED AIR COLLEGE,Khalifa bin Zayed Air College,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q63323653
KHIMJI RAMDAS RELOCATION SERVICES,Khimji Ramdas Relocation Services,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140720512
KIBSONS,Kibsons,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
KIDSY,Kidsy,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q138733094
KINGS PARK HOTEL,Kings Park Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997683
KINGS SCHOOL AL BARSHA,Kings School Al Barsha,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088427
KINGS SCHOOL NAD AL SHEBA,Kings School Nad Al Sheba,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088434
KINGS SCHOOL DUBAI,Kings school Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088431
KINGSGATE AL JADAF,Kingsgate Al Jadaf,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997647
KINGSGATE HOTEL ABU DHABI BY MILLENNIUM,Kingsgate Hotel Abu Dhabi by Millennium,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150384
KINOKUNIYA,Kinokuniya,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
KINSHASA AIRWAYS,Kinshasa Airways,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q6414268
KRISPY KREME,Krispy Kreme,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
KULLĪYAT AL-DIRĀSĀT AL-ISLĀMĪYAH WA-AL-ʻARABĪYAH,Kullīyat al-Dirāsāt al-Islāmīyah wa-al-ʻArabīyah,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q12235965
KUWAIT AIRWAYS,Kuwait Airways,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
L'ARABIA HOTEL APARTMENTS,L'Arabia Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997600
LA QUINTA BY WYNDHAM BUR DUBAI,La Quinta by Wyndham Bur Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150397
"LA VILLE HOTEL & SUITES CITY WALK, DUBAI, AUTOGRAPH COLLECTION","La Ville Hotel & Suites City WALK, Dubai, Autograph Collection",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150317
LANDMARK GRAND HOTEL,Landmark Grand Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856044
LANDMARK GROUP,Landmark Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6484773
LANDMARK HOTEL BANIYAS DUBAI,Landmark Hotel Baniyas Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997665
LANDMARK PLAZA HOTEL DUBAI,Landmark Plaza Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997664
LANDMARK RIQQA HOTEL,Landmark Riqqa Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150521
LANDMARK SUMMIT HOTEL,Landmark Summit Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997673
LANGPROS LANGUAGE SOLUTIONS,Langpros Language Solutions,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q135038070
LATIFA HOSPITAL,Latifa Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q6496088
LATIFA SCHOOL,Latifa School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089030
LATIFA SCHOOL FOR GIRLS,Latifa School for Girls,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q6496089
LAUNDRYHEAP,Laundryheap,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
LAVENDER HOTEL SHARJAH (PREVIOUSLY LORDS HOTEL),Lavender Hotel Sharjah (Previously Lords Hotel),Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150592
LE MERIDIEN ABU DHABI,Le Meridien Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150566
LE MERIDIEN AL AQAH BEACH RESORT,Le Meridien Al Aqah Beach Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150659
LE MERIDIEN FAIRWAY,Le Meridien Fairway,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150482
LE MÉRIDIEN DUBAI HOTEL & CONFERENCE CENTRE,Le Méridien Dubai Hotel & Conference Centre,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150527
LE ROYAL MERIDIEN ABU DHABI,Le Royal Meridien Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111151486
LE ROYAL MERIDIEN BEACH RESORT & SPA DUBAI,Le Royal Meridien Beach Resort & Spa Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150737
LE WANA HOTEL,Le Wana Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997676
LEGOLAND DUBAI,Legoland Dubai,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
LEMON TREE HOTEL JUMEIRAH DUBAI,Lemon Tree Hotel Jumeirah Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150280
LEMON TREE HOTELS,Lemon Tree Hotels,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6521344
LEMONSTONE AI,Lemonstone AI,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140301206
LENOUAR,Lenouar,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140050708
"LEVA HOTEL AND SUITES, MAZAYA CENTRE","Leva Hotel and Suites, Mazaya Centre",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150308
LEVEL SHOES,Level Shoes,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
LI BEIRUT,Li Beirut,Food_Dining,AE,,type_mapped,http://www.wikidata.org/entity/Q131287951
LIFE PHARMACY,Life Pharmacy,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
LINCOLN UNIVERSITY OF BUSINESS AND MANAGEMENT,Lincoln University of Business and Management,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q28220745
LINKEDIN PREMIUM,LinkedIn Premium,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
LITTLE CAESARS,Little Caesars,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
LITTLE FLOWERS ENGLISH SCHOOL,Little Flowers English school,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088439
LIWA UNIVERSITY,Liwa University,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q18455299
LONDON SUITES HOTEL,London Suites Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997638
LOOP MOBILE FZCO,Loop Mobile FZCO,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141465146
LOOTAH GAS,Lootah Gas,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
LOTUS GRAND HOTEL,Lotus Grand Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997672
LOTUS RETREAT HOTEL,Lotus Retreat Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111111798
LOU LOU'A BEACH RESORT,Lou Lou'a Beach Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150593
LOUVRE ABU DHABI,Louvre Abu Dhabi,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
LULU GROUP INTERNATIONAL,LuLu Group International,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6702930
LULU,Lulu,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
LUMITECH,Lumitech,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140461855
LUSTY CREATORS,Lusty Creators,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139827247
LUXURY SUPERCAR RENTALS DUBAI,Luxury Supercar Rentals Dubai,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139796357
LYCEE FRANCAIS INTERNATIONAL,Lycee Francais International,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088662
LYCEE FRANCAIS INTERNATIONAL GEORGES POMPIDOU PRIMARY OUD METHA,Lycee Francais International Georges Pompidou Primary Oud Metha,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088665
LYCEE FRANCAIS INTERNATIONAL GEORGES POMPIDOU SCHOOL ( DUBAI BRANCH ),Lycee Francais International Georges Pompidou School ( Dubai Branch ),Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088666
LYCÉE FRANÇAIS INTERNATIONAL DE DUBAÏ,Lycée Français International de Dubaï,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q19572733
LYCÉE FRANÇAIS JEAN MERMOZ,Lycée Français Jean Mermoz,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089018
LYCÉE LIBANAIS FRANCOPHONE PRIVÉ,Lycée Libanais Francophone Privé,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q24960024
LYCÉE LOUIS MASSIGNON,Lycée Louis Massignon,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q3268821
MD HOTEL BY GEWAN FORMERLY CASSELLS,MD Hotel By Gewan Formerly Cassells,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150247
ME DUBAI BY MELIÁ,ME Dubai by Meliá,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150302
MEED,MEED,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6715314
MIDTRANS SHIPPING AND SERVICES,MIDTRANS SHIPPING AND SERVICES,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q43032906
MODUL UNIVERSITY DUBAI,MODUL University Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q22948633
MSB PRIVATE SCHOOL,MSB Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088124
MT MESSE STAND,MT Messe Stand,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140967119
MUSE TRENDY TOY,MUSE Trendy Toy,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139955597
MAFEEMUSHKIL,MafeeMushkil,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140455019
MAFRAQ HOSPITAL,Mafraq Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q30280817
MAGIC PLANET,Magic Planet,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q120799993
MAGRUDY,Magrudy,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MAI DUBAI,Mai Dubai,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MAINET X,Mainet X,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q117287614
MAISAN HOTEL,Maisan Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997735
MAISON PRIVÉE ARABIA,Maison Privée Arabia,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140453869
MAJESTIC CITY RETREAT HOTEL,Majestic City Retreat Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150425
MAJID AL FUTTAIM GROUP,Majid Al Futtaim Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1617128
MAJLIS GRAND MERCURE RESIDENCE ABU DHABI,Majlis Grand Mercure Residence Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150553
MAKTOOB,Maktoob,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6740419
MALABAR GOLD,Malabar Gold,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MALL OF AL AIN,Mall of Al Ain,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q4703453
MAMOURA DIVERSIFIED GLOBAL HOLDING,Mamoura Diversified Global Holding,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1684478
"MANDARIN ORIENTAL JUMEIRA, DUBAI","Mandarin Oriental Jumeira, Dubai",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111151476
MANGOPROXY,MangoProxy,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140858798
MANGROVE HOTEL,Mangrove Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150650
MANHATTAN AVENUE HOTEL,Manhattan Avenue Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997640
MANOR HALL INTERNATIONAL SCHOOL,Manor Hall International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q113961993
MANSION EDITION,Mansion Edition,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141541029
MANZIL DOWNTOWN,Manzil Downtown,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150309
MARA GROUP,Mara Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q17009483
MARBELLA RESORT,Marbella Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856060
MARCO POLO HOTEL,Marco Polo Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150543
MARIANA HOTEL,Mariana Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997656
MARINA BYBLOS HOTEL,Marina Byblos Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150712
MARINA HOTEL APARTMENTS,Marina Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150741
"MARINA MALL, ABU DHABI","Marina Mall, Abu Dhabi",Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q3293168
MARJAN ISLAND RESORT & SPA - MANAGED BY ACCOR,Marjan Island Resort & Spa - Managed by Accor,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997721
MARRIOTT,Marriott,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
"MARRIOTT EXECUTIVE APARTMENTS DOWNTOWN, ABU DHABI","Marriott Executive Apartments Downtown, Abu Dhabi",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997607
MARRIOTT EXECUTIVE APARTMENTS DUBAI AL JADDAF,Marriott Executive Apartments Dubai Al Jaddaf,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150391
MARRIOTT EXECUTIVE APARTMENTS DUBAI CREEK,Marriott Executive Apartments Dubai Creek,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150484
"MARRIOTT HOTEL AL FORSAN, ABU DHABI","Marriott Hotel Al Forsan, Abu Dhabi",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150379
MARRIOTT HOTEL AL JADDAF DUBAI,Marriott Hotel Al Jaddaf Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150389
MARRIOTT HOTEL DOWNTOWN ABU DHABI,Marriott Hotel Downtown Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150200
MASAFI,Masafi,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MASDAR,Masdar,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1163521
MAWAQIF,Mawaqif,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MAWARID FINANCE,Mawarid Finance,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6794362
MAX FASHION,Max Fashion,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MAXIMUS AIR CARGO,Maximus Air Cargo,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q1530024
MCDONALD'S,McDonald's,Food_Dining,AE,,project_category;descriptor_unverified,project:scripts/rules.py
MEDCARE,Medcare,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MEDIA ONE HOTEL,Media One Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150752
MEDIA ROTANA DUBAI,Media Rotana Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150229
MEDIA.NET,Media.net,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q24885109
MEDIALINKS EVENTS STAFFING AGENCY,Medialinks Events Staffing Agency,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q142068287
MEDICINA PHARMACY,Medicina Pharmacy,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MEDICLINIC,Mediclinic,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MEDICLINIC CITY HOSPITAL,Mediclinic City Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q30260571
MELIÁ DESERT PALM DUBAI,Meliá Desert Palm Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150516
MELODICA MUSIC CENTER,Melodica Music Center,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q106367291
MENA PLAZA HOTEL ALBARSHA,Mena Plaza Hotel Albarsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856023
MERCATO SHOPPING MALL,Mercato Shopping Mall,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q6818049
MERCURE DUBAI BARSHA HEIGHTS HOTEL SUITES,Mercure Dubai Barsha Heights Hotel Suites,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150222
MERCURE GRAND JEBEL HAFEET AL AIN HOTEL,Mercure Grand Jebel Hafeet Al Ain Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150731
MERCURE HOTEL APARTMENTS DUBAI BARSHA HEIGHTS,Mercure Hotel Apartments Dubai Barsha Heights,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150224
MERMAID BEACH HOTEL LLC,Mermaid Beach Hotel LLC,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997713
METROPOLITAN HOTEL DUBAI,Metropolitan Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150281
MICROSOFT 365,Microsoft 365,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MIDDLESEX UNIVERSITY DUBAI,Middlesex University Dubai,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MIDEX AIRLINES,Midex Airlines,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q875472
MILESTONE HOTEL APARTMENT,Milestone Hotel Apartment,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856038
MILLENNIUM AIRPORT HOTEL DUBAI,Millennium Airport Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150512
MILLENNIUM AL BARSHA,Millennium Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150260
MILLENNIUM AL RAWDAH HOTEL,Millennium Al Rawdah Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150192
MILLENNIUM ATRIA BUSINESS BAY,Millennium Atria Business Bay,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150287
MILLENNIUM CENTRAL AL MAFRAQ,Millennium Central Al Mafraq,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150366
MILLENNIUM CENTRAL DOWNTOWN,Millennium Central Downtown,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150335
MILLENNIUM MONTROSE EXECUTIVE APARTMENT,Millennium Montrose Executive Apartment,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997613
MILLENNIUM PLACE BARSHA HEIGHTS HOTEL,Millennium Place Barsha Heights Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150210
MILLENNIUM PLACE DUBAI MARINA,Millennium Place Dubai Marina,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150714
MILLENNIUM PLAZA HOTEL DUBAI,Millennium Plaza Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150350
MINDBE EDUCATION,MindBE Education,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139850401
MINERSHUB,MinersHub,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139741696
MINISTRY OF FOREIGN AFFAIRS,Ministry of Foreign Affairs,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MINISTRY OF HUMAN RESOURCES AND EMIRATISATION,Ministry of Human Resources and Emiratisation,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MIRAGE HOTEL,Mirage Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997729
MIRAMAR AL AQAH BEACH RESORT,Miramar Al Aqah Beach Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150657
MIRDIF CITY CENTRE,Mirdif City Centre,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q6873078
MIRDIF PRIVATE SCHOOL,Mirdif Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088668
MIRFA HOTEL,Mirfa Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150365
MOBIMATTER,MobiMatter,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141623199
"MODEL PRIVATE SCHOOL, ABU DHABI","Model Private School, Abu Dhabi",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q4670145
MODERN SKILLS SCHOOL,Modern Skills School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088671
MOHAMED BIN ZAYED UNIVERSITY OF ARTIFICIAL INTELLIGENCE,Mohamed bin Zayed University of Artificial Intelligence,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q79048705
MOHAMMED BIN RASHID CITY,Mohammed bin Rashid City,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q3023507
MOON VALLEY HOTEL APARTMENT,Moon Valley Hotel Apartment,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150448
MOONRISE,Moonrise,Food_Dining,AE,,type_mapped,http://www.wikidata.org/entity/Q135903184
MOORFIELDS EYE HOSPITAL DUBAI,Moorfields Eye Hospital Dubai,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MOSCOW HOTEL,Moscow Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150487
MOTIONGATE,Motiongate,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MOUNT ROYAL HOTEL,Mount Royal Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997666
MOUNTS.AE,Mounts.ae,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141134069
MUGHAL SUITES,Mughal Suites,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997727
MULTIBANK GROUP,MultiBank Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q85786964
MUMZWORLD,Mumzworld,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MURDOCH UNIVERSITY DUBAI,Murdoch University Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q18391415
MUSAFIR,Musafir,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MUSEUM OF THE FUTURE,Museum of the Future,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
MUSHRIF MALL,Mushrif Mall,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q6941289
MUSTADEEM,Mustadeem,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141325330
MY PINCH OF WOW,My Pinch of Wow,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141252646
MYSK AL FAYA RETREAT,Mysk Al Faya Retreat,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q112026981
MYSK KINGFISHER RETREAT,Mysk Kingfisher Retreat,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150629
MÖVENPICK GRAND AL BUSTAN DUBAI,Mövenpick Grand Al Bustan Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150511
MÖVENPICK HOTEL & APARTMENTS BUR DUBAI,Mövenpick Hotel & Apartments Bur Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q6926792
MÖVENPICK HOTEL APARTMENTS AL MAMZAR DUBAI,Mövenpick Hotel Apartments Al Mamzar Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150580
MÖVENPICK HOTEL APARTMENTS DOWNTOWN DUBAI,Mövenpick Hotel Apartments Downtown Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150323
MÖVENPICK HOTEL JUMEIRAH BEACH,Mövenpick Hotel Jumeirah Beach,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150728
NASDAQ DUBAI,NASDAQ Dubai,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6952530
NEXPACE,NEXPACE,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139792265
NMC HEALTH,NMC Health,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6954702
NMC HOSPITAL,NMC Hospital,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NSTYLE,NStyle,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NT.PAYMENTS,NT.Payments,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q126646506
NAKHEEL COMMUNITY MANAGEMENT,Nakheel Community Management,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NAKHEEL MALL,Nakheel Mall,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q115803914
NAKHEEL PROPERTIES,Nakheel Properties,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1964041
NAMSHI,Namshi,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NANDO'S,Nando's,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NAQSH MEDIA,Naqsh Media,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141313947
NASSIMA TOWER HOTEL APARTMENTS,Nassima Tower Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150355
NATIONAL CHARITY SCHOOL-BOYS AND GIRLS,National Charity School-Boys and Girls,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088674
NATIONAL MARINE DREDGING COMPANY,National Marine Dredging Company,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q22123646
NATIONAL TAKAFUL,National Takaful,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NAZCAA DUBAI,Nazcaa Dubai,Food_Dining,AE,,type_mapped,http://www.wikidata.org/entity/Q134100374
NEHAL HOTEL,Nehal Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150554
NEJOUM AL EMARAT,Nejoum Al Emarat,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150604
NEOPHARMA,Neopharma,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q119659563
NEOVISION WEALTH MANAGEMENT,Neovision Wealth Management,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141494021
NESTO,Nesto,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NETFLIX,Netflix,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NEW ACADEMY SCHOOL,New Academy School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088676
NEW ERA LEARNING,New Era Learning,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140078880
NEW INDIAN MODEL SCHOOL,New Indian Model School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q15262060
NEW PENNINSULA HOTEL,New Penninsula Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997651
NEW WORLD  SCHOOL PRIVATE,New World  School Private,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088679
NEWLANDS SCHOOL,Newlands School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089022
NEXALA AI,Nexala AI,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140680961
NEXT GENERATION SCHOOL,Next Generation School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088680
NEXTORIA INFORMATION TECHNOLOGY LLC,Nextoria Information Technology LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q142067841
NIHAL HOTEL,Nihal Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150493
NIKE,Nike,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NIKKI BEACH RESORT & SPA DUBAI,Nikki Beach Resort & Spa Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150362
NINTENDO,Nintendo,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NOJOUM HOTEL APARTMENTS LLC,Nojoum Hotel Apartments LLC,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150546
NOON,Noon,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NOON DAILY,Noon Daily,Groceries,AE,,project_category;descriptor_unverified,project:scripts/rules.py
NOON FOOD,Noon Food,Food_Dining,AE,,project_category;descriptor_unverified,project:scripts/rules.py
NOON MINUTES,Noon Minutes,Groceries,AE,,project_category;descriptor_unverified,project:scripts/rules.py
NOON ONE,Noon One,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NOOR CAPITAL,Noor Capital,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q105750185
NORD ANGLIA INTERNATIONAL SCHOOL,Nord Anglia International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088687
NORD ANGLIA INTERNATIONAL SCHOOL DUBAI,Nord Anglia International School Dubai,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NORTH AMERICAN INTERNATIONAL SCHOOL,North American International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088691
NORTH LONDON COLLEGIATE SCHOOL DUBAI,North London Collegiate School Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089024
NOTION,Notion,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NOUR ARJAAN BY ROTANA - FUJAIRAH,Nour Arjaan by Rotana - Fujairah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150641
NOVA PARK HOTEL,Nova Park Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150601
NOVEL HOTEL CITY CENTER,Novel Hotel City Center,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150370
NOVO CINEMAS,Novo Cinemas,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
NOVOTEL ABU DHABI AL BUSTAN,Novotel Abu Dhabi Al Bustan,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150188
NOVOTEL ABU DHABI GATE,Novotel Abu Dhabi Gate,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150194
NOVOTEL BUR DUBAI,Novotel Bur Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150428
NOVOTEL DUBAI AL BARSHA,Novotel Dubai Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150245
NOVOTEL DUBAI DEIRA CITY CENTRE,Novotel Dubai Deira City Centre,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150488
NOVOTEL FUJAIRAH,Novotel Fujairah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150634
NOVOTEL SHARJAH EXPO CENTRE,Novotel Sharjah Expo Centre,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150587
NOVOTEL SUITES DUBAI MALL OF THE EMIRATES,Novotel Suites Dubai Mall of the Emirates,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150264
NOVOTEL WORLD TRADE CENTRE DUBAI,Novotel World Trade Centre Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150360
NUMBER ONE TOWER SUITES,Number One Tower Suites,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150340
NUMBER SLEVEN FZ-LLC,Number Sleven FZ-LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139825940
NUMIX AUTOMOTIVE COATINGS,Numix Automotive Coatings,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139985526
NURAN MARINA SERVICED RESIDENCES,Nuran Marina Serviced Residences,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111399890
OLA ENERGY,OLA Energy,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q126916526
OSN+,OSN+,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
OYO 157 AL KHAIMA HOTEL,OYO 157 Al Khaima Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067192
OYO 160 LUMBINI DREAM GARDEN GUEST HOUSE LLC,OYO 160 Lumbini Dream Garden Guest House Llc,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067185
OYO 270 DREAM LAND HOTEL,OYO 270 Dream Land Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067180
OYO 314 24 GOLD HOTEL,OYO 314 24 Gold Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067184
"OYO 323 HOME 417, IMPERIAL RESIDENCE TOWER B, STUDIO","OYO 323 Home 417, Imperial Residence Tower B, Studio",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067179
OYO 328 CITY PLAZA HOTEL,OYO 328 City Plaza Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111068536
OYO 338 TRANSWORLD HOTEL,OYO 338 Transworld Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067186
OYO 339 VIENNA HOTEL,OYO 339 Vienna Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067176
OYO 350 AL RABIA,OYO 350 Al Rabia,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067177
OYO 367 EUREKA HOTEL,OYO 367 Eureka Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067187
OYO 393 AL WEHDA HOTEL,OYO 393 Al Wehda Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067188
OYO 394 DANA AL BUHAIRA BEACH HOTEL,OYO 394 Dana Al Buhaira Beach Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067814
"OYO 409 HOME 910, 1711, 2111, 2107","OYO 409 Home 910, 1711, 2111, 2107",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067816
OYO 410 HOME 2BHK,OYO 410 Home 2bhk,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067815
"OYO 471 HOME 403, 503, 603","OYO 471 Home 403, 503, 603",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458831
OYO 472 HOME 709,OYO 472 Home 709,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458830
OYO 491 RAHAB HOTEL,OYO 491 Rahab Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067190
OYO 504 HOME CANAL VIEW STUDIO APARTMENT,OYO 504 Home Canal View Studio Apartment,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458736
"OYO 512 HOME SKYCOURT TOWER 1217, 1BHK","OYO 512 Home Skycourt Tower 1217, 1BHK",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458777
OYO 517 HOME 2BHK NAJMA TOWER,OYO 517 Home 2BHK NAJMA TOWER,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067198
OYO 518 HOME 1 BHK NAJMA TOWER,OYO 518 Home 1 BHK Najma Tower,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067196
OYO 539 HOME MUBARAK AL AMERI,OYO 539 Home Mubarak Al Ameri,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458832
OYO 558 HOME NAJMA TOWER 2BR,OYO 558 Home Najma tower 2br,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067193
OYO 561 HOME NAJMA TOWER A1BR,OYO 561 Home Najma tower A1br,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067183
OYO 578 OASIS DEIRA HOTEL,OYO 578 Oasis Deira Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067197
"OYO 587 HOME 115,ELITE RESIDENCE 3","OYO 587 Home 115,Elite Residence 3",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458746
OYO 589 HOME 48 -NAJMA 2BR,OYO 589 Home 48 -Najma 2br,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067195
OYO 590 HOME NAJMA 1BED,OYO 590 Home Najma 1bed,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067191
OYO 591 HOME 231 RESORTZ RESIDENCE,OYO 591 Home 231 Resortz Residence,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458750
OYO 598 HOME PARK ISLAND,OYO 598 Home park island,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458762
OYO 605 HOME QASR SABAH 1 BR,OYO 605 Home Qasr Sabah 1 br,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067194
"OYO 618 HOME 1707, BOULEVARD CENTRAL 2","OYO 618 Home 1707, Boulevard Central 2",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458751
OYO 662 HOME CENTURIM 1806,OYO 662 Home centurim 1806,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458763
OYO 676 HOME CANAL VIEWS BUSINESS BAY,OYO 676 Home Canal Views Business Bay,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458749
OYO 699 HOME MAZIL NAIF,OYO 699 Home mazil naif,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458764
OYO 700 HOME GRACE RESIDENCY,OYO 700 Home grace residency,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458761
OYO 701 HOME ZARONI BLDG IC,OYO 701 Home Zaroni bldg IC,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458786
OYO 702 HOME EWAN RESIDENCE,OYO 702 Home ewan residence,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458765
OYO 703 HOME MAG555 STUDIO 621,OYO 703 Home Mag555 studio 621,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458748
OYO 704 HOME EWAN RESIDENCE 2BR,OYO 704 Home ewan residence 2br,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458752
OYO 705 HOME JVC LIVING GARDEN,OYO 705 Home jvc living garden,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458766
OYO 717 HOME SOBHA HARTLAND 2436,OYO 717 Home Sobha Hartland 2436,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458767
OYO 718 HOME DG BLDG61,OYO 718 Home dg bldg61,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458768
OYO 719 HOME AZIZI AURA DG,OYO 719 Home Azizi aura dg,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458769
OYO 726 HOME AFNAN MIDTOWN,OYO 726 Home afnan midtown,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458770
OYO 727 HOME RED RESIDENCE 203,OYO 727 Home red residence 203,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458771
OYO 728 HOME ELITE 8 604,OYO 728 Home elite 8 604,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458772
OYO 729 HOME PARK GATE 1703,OYO 729 Home park gate 1703,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458742
OYO 731 HOME VILLA 52,OYO 731 Home villa 52,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458741
OYO 733 HOME MAYFAIR RESIDENCE,OYO 733 Home Mayfair residence,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458787
OYO 734 HOME BAHAR 6,OYO 734 Home bahar 6,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458773
OYO 740 HOME DG 195,OYO 740 Home DG 195,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458774
OYO 741 HOME LAKESIDE RESIDENCE 917,OYO 741 Home lakeside residence 917,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458745
OYO 755 HOME SOBHA GREENS,OYO 755 Home Sobha Greens,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458784
OYO 756 HOME ALCOVE 2BR,OYO 756 Home alcove 2br,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458780
OYO 757 HOME ALCOVE STUDIO,OYO 757 Home alcove studio,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458753
OYO 762 HOME G01 ALCOVE 1BR,OYO 762 Home G01 ALCOVE 1BR,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458781
"OYO 764 HOME 2312 BAYZ BY DANUBE, BUSINESS BAY- STUDIO","OYO 764 Home 2312 Bayz By Danube, Business Bay- Studio",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458755
"OYO 765 HOME 1521 GOLF VITA - TOWER A, DAMAC HILLS","OYO 765 Home 1521 Golf Vita - Tower A, Damac Hills",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458775
OYO 766 HOME 524 ELITE SPORTS RESIDENCE 10,OYO 766 Home 524 Elite Sports Residence 10,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458759
OYO 767 HOME 410 ALCOVE RESIDENCES JVC,OYO 767 Home 410 Alcove Residences JVC,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458776
"OYO 784 HOME 312 ELITE RESEIDENCE - 1, SPORTS CITY - STUDIO","OYO 784 Home 312 Elite Reseidence - 1, Sports City - Studio",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458778
OYO 785 HOME 1501 HUB CANAL 1,OYO 785 Home 1501 Hub Canal 1,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458783
"OYO 786 HOME 118 ALCOVE RESIDENTIAL BUILDING, JVC","OYO 786 Home 118 Alcove Residential Building, JVC",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458760
OYO 787 HOME HUBCANAL 2 SPORTS CITY,OYO 787 Home Hubcanal 2 Sports City,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458782
"OYO 788 HOME AG TOWER- 1009A & 1011B, BUSINESS BAY","OYO 788 Home AG TOWER- 1009A & 1011B, Business Bay",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458756
"OYO 789 HOME AG TOWER - 1011A & 1111A, BUSINESS BAY","OYO 789 Home AG TOWER - 1011A & 1111A, Business Bay",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458758
OYO 793 AL ARRAF HOTEL,OYO 793 Al Arraf Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458793
OYO 794 GREAT COUNTRY HOTEL,OYO 794 Great Country Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458794
OYO 795 AL KARAWAN HOTEL,OYO 795 Al Karawan Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458795
OYO 796 HOME MARINA RESIDENCE 3BR,OYO 796 Home Marina Residence 3br,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458757
OYO 797 CITY RELAX HOTEL,OYO 797 City Relax Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458792
OYO 800 MOON CREEK HOTEL,OYO 800 Moon Creek Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458791
"OYO 808 HOME ROYAL REGENCY - 1 BEDROOM, DUBAI MARINA","OYO 808 Home Royal Regency - 1 Bedroom, Dubai Marina",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458788
"OYO 809 HOME ROYAL REGENCY - STUDIO, DUBAI MARINA","OYO 809 Home Royal Regency - Studio, Dubai Marina",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458789
"OYO 810 HOME ROYAL REGENCY - 2 BEDROOM, DUBAI MARINA","OYO 810 Home Royal Regency - 2 Bedroom, Dubai Marina",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458785
OYO 817 HOME AL QUDRA TOWN HOUSE,OYO 817 Home Al qudra town house,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458743
OYO 818 HOME BURJ NUJOOM STUDIO,OYO 818 Home burj nujoom studio,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458754
OYO 819 HOME NSHAMA 1BR,OYO 819 Home Nshama 1br,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458779
"OYO 823 HOME 104 ALCOVE RESIDENCES, JVC","OYO 823 Home 104 Alcove Residences, JVC",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458744
OYO 832 HOME MONT ROSE,OYO 832 Home Mont rose,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458739
OYO 833 HOME BAYZ BY DANUBE,OYO 833 Home bayz by danube,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458738
OYO 834 HOME LA RIVERIA 2BR,OYO 834 Home la riveria 2br,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458737
OYO HOME 483 1BHK TAMCON DIP,OYO Home 483 1BHK Tamcon DIP,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111067178
OAKS IBN BATTUTA GATE DUBAI,Oaks Ibn Battuta Gate Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150696
OAKS LIWA HEIGHTS SUITES,Oaks Liwa Heights Suites,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111151482
OAKTREE PRIMARY SCHOOL,Oaktree Primary School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088694
"OASIS HOSPITAL, AL AIN","Oasis Hospital, Al Ain",Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q7074423
OASIS STUDIO,Oasis Studio,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141254569
OCCIDENTAL DUBAI PRODUCTION CITY,Occidental Dubai Production City,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150716
OCCIDENTAL SHARJAH GRAND,Occidental Sharjah Grand,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150597
OCEANIC KHORFAKKAN RESORT & SPA,Oceanic Khorfakkan Resort & Spa,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150649
OFFICERS CLUB & HOTEL,Officers Club & Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997599
OLIVA,Oliva,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139700629
OMAN AIR,Oman Air,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ONE&ONLY THE PALM,One&Only The Palm,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111151477
OPERATION FALAFEL,Operation Falafel,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ORCHID VUE HOTEL,Orchid Vue Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150443
ORGANIC FOODS AND CAFE,Organic Foods and Cafe,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ORIENT INSURANCE,Orient Insurance,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ORYX HOTEL,Oryx Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856008
OUNASS,Ounass,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
OUR OWN HIGH SCHOOL,Our Own High School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7111126
OXFORD SCHOOL,Oxford School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088696
P.F. CHANG'S,P.F. Chang's,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
POP 758 GRAND MAYFAIR HOTEL,POP 758 Grand Mayfair Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458790
POP 824 AL ARAB JAVI INN,POP 824 Al Arab Javi Inn,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111458740
PADEL26,Padel26,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q114601695
PAKISTAN EDUCATION ACADEMY,Pakistan Education Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q25041107
PAKISTAN EDUCATIONAL ACADEMY,Pakistan Educational Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088698
PAKISTAN ISLAMIA HIGHER SECONDARY SCHOOL,Pakistan Islamia Higher Secondary School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7125613
PALACE DOWNTOWN,Palace Downtown,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150310
PALACE DUBAI CREEK HARBOUR,Palace Dubai Creek Harbour,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q136652752
PALAZZO VERSACE DUBAI,Palazzo Versace Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q7127010
PALM AVIATION,Palm Aviation,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q7127963
PALMA BEACH RESORT & SPA,Palma Beach Resort & Spa,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150620
PAN EMIRATES,Pan Emirates,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
PANORAMA BUR DUBAI HOTEL,Panorama Bur Dubai Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997645
PANORAMA HOTEL DEIRA,Panorama Hotel Deira,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150501
PAPA JOHN'S,Papa John's,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
PARAMOUNT HOTEL DUBAI,Paramount Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150319
PARFUMIX,Parfumix,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141806152
PARIS-SORBONNE UNIVERSITY ABU DHABI,Paris-Sorbonne University Abu Dhabi,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q3551475
"PARK ARJAAN BY ROTANA, ABU DHABI","Park Arjaan by Rotana, Abu Dhabi",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150196
PARK HOTEL APARTMENTS,Park Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150405
PARK HYATT ABU DHABI HOTEL & VILLAS,Park Hyatt Abu Dhabi Hotel & Villas,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150667
PARK HYATT DUBAI,Park Hyatt Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150463
PARK HYATT DUBAI CREEK GOLF & YATCH CLUB,Park Hyatt Dubai Creek Golf & Yatch Club,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q136513000
PARK INN BY RADISSON ABU DHABI YAS ISLAND,Park Inn by Radisson Abu Dhabi Yas Island,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150672
PARK INN BY RADISSON DUBAI MOTOR CITY,Park Inn by Radisson Dubai Motor City,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150221
PARK REGIS BOUTIQUE HOTEL,Park Regis Boutique Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150283
PARK REGIS BUSINESS BAY HOTEL,Park Regis Business Bay Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150293
PARK REGIS KRIS KIN HOTEL,Park Regis Kris Kin Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150441
PARK ROTANA ABU DHABI,Park Rotana Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150198
PARKIN,Parkin,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
PARKSIDE HOTEL APARTMENT,Parkside Hotel Apartment,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997736
PATREON,Patreon,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
PAUL BAKERY,Paul Bakery,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
PAYPAL,PayPal,Shopping_Retail,AE,,project_category;descriptor_unverified,project:scripts/rules.py
PEARL HOTEL & SPA,Pearl Hotel & Spa,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150619
PEARL MARINA HOTEL APARTMENTS,Pearl Marina Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150703
PEARL ROTANA CAPITAL CENTRE,Pearl Rotana Capital Centre,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150182
PERFORMA,Performa,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139718267
PETROLEUM INSTITUTE,Petroleum Institute,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7178947
PHILADELPHIA PRIVATE SCHOOL,Philadelphia Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088703
PHOENICIA HOTEL,Phoenicia Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997661
PHOENIX AVIATION,Phoenix Aviation,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q2036150
PHOENIX DISON TEC,Phoenix Dison Tec,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141499619
PHOENIX PLAZA HOTEL APARTMENTS,Phoenix Plaza Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997605
PICKL,Pickl,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
PIONEER EDUCATION LIMITED,Pioneer Education Limited,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141987693
PIZZA HUT,Pizza Hut,Food_Dining,AE,,project_category;descriptor_unverified,project:scripts/rules.py
PLATINUMLIST,Platinumlist,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
PLAYSTATION,PlayStation,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
PLAYGAMA,Playgama,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140768339
POPEYES,Popeyes,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
PREMIER INN ABU DHABI CAPITAL CENTRE,Premier Inn Abu Dhabi Capital Centre,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150184
PREMIER INN ABU DHABI INTERNATIONAL AIRPORT,Premier Inn Abu Dhabi International Airport,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150669
PREMIER INN DUBAI AL JADDAF,Premier Inn Dubai Al Jaddaf,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150421
PREMIER INN DUBAI DRAGON MART,Premier Inn Dubai Dragon Mart,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150453
PREMIER INN DUBAI IBN BATTUTA MALL,Premier Inn Dubai Ibn Battuta Mall,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150698
PREMIER INN DUBAI INTERNATIONAL AIRPORT,Premier Inn Dubai International Airport,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150535
PREMIER INN DUBAI INVESTMENTS PARK,Premier Inn Dubai Investments Park,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150693
PREMIER INN DUBAI SILICON OASIS,Premier Inn Dubai Silicon Oasis,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150321
PRESIDENT HOTEL,President Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150407
PRESIDENTIAL FLIGHT (UAE),Presidential Flight (UAE),Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q4670122
PRIME ALLEY TECHNOLOGY,Prime Alley Technology,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141488941
PRIME MEDICAL CENTER,Prime Medical Center,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
PRIME OASIS,Prime Oasis,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140918648
PRIMUS PRIVATE SCHOOL LLC,Primus Private School LLC,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088718
PRINTPLAST,PrintPlast,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139578378
PROPSPACE,PropSpace,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140736998
PULLMAN DUBAI CITY CENTRE RESIDENCES,Pullman Dubai City Centre Residences,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997667
PULLMAN DUBAI CREEK CITY CENTRE,Pullman Dubai Creek City Centre,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150485
PULLMAN DUBAI DOWNTOWN,Pullman Dubai Downtown,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q136648373
PULLMAN DUBAI JUMEIRAH LAKES TOWERS,Pullman Dubai Jumeirah Lakes Towers,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150742
PULLMAN SHARJAH,Pullman Sharjah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150588
PUMA,Puma,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
PURE GOLD,Pure Gold,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
PUSHE,Pushe,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q129911569
PYTHIA TECHNOLOGIES,Pythia Technologies,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139763404
QANU,Qanu,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141806277
QARAR LEGAL FOR ABU DHABI COURTS TRANSACTION CLEARANCE,Qarar Legal for Abu Dhabi Courts Transaction Clearance,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141740818
QATAR AIRWAYS,Qatar Airways,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
QUEEN ELIZABETH 2 HOTEL,Queen Elizabeth 2 Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150427
QUEEN INTERNATIONAL SCHOOL,Queen International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088708
QUEEN PALACE HOTEL,Queen Palace Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997609
QUEEN'S HOTEL,Queen's Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150480
QUERIDA MEXICAN & FRIENDS,Querida Mexican & Friends,Food_Dining,AE,,type_mapped,http://www.wikidata.org/entity/Q139801933
RAK AIRWAYS,RAK Airways,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q1478590
RAK CERAMICS,RAK Ceramics,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7275734
RAK HOSPITAL,RAK Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q18392892
RAK MEDICAL AND HEALTH SCIENCES UNIVERSITY,RAK Medical and Health Sciences University,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7294680
RAKBANK,RAKBANK,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7275733
RARE BRASSERIE & BAR,RARE Brasserie & Bar,Food_Dining,AE,,type_mapped,http://www.wikidata.org/entity/Q140577438
RTA,RTA,Transport_Auto,AE,,project_category;descriptor_unverified,project:scripts/rules.py
RTA NOL,RTA NOL,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
RABDAN ACADEMY,Rabdan Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q110235875
"RADISSON BLU HOTEL & RESORT, ABU DHABI CORNICHE","Radisson Blu Hotel & Resort, Abu Dhabi Corniche",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150185
"RADISSON BLU HOTEL & RESORT, AL AIN","Radisson Blu Hotel & Resort, Al Ain",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150227
RADISSON BLU HOTEL ABU DHABI YAS ISLAND,Radisson Blu Hotel Abu Dhabi Yas Island,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150673
"RADISSON BLU HOTEL, AJMAN","Radisson Blu Hotel, Ajman",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150615
"RADISSON BLU HOTEL, DUBAI CANAL VIEW","Radisson Blu Hotel, Dubai Canal View",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150331
"RADISSON BLU HOTEL, DUBAI DEIRA CREEK","Radisson Blu Hotel, Dubai Deira Creek",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150471
"RADISSON BLU HOTEL, DUBAI MEDIA CITY","Radisson Blu Hotel, Dubai Media City",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150755
"RADISSON BLU HOTEL, DUBAI WATERFRONT","Radisson Blu Hotel, Dubai Waterfront",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150297
"RADISSON BLU RESIDENCE, DUBAI MARINA","Radisson Blu Residence, Dubai Marina",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150732
"RADISSON BLU RESORT, FUJAIRAH","Radisson Blu Resort, Fujairah",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150662
RADISSON RED DUBAI SILICON OASIS,Radisson Red Dubai Silicon Oasis,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150322
RAFFLES DUBAI,Raffles Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q7282574
RAFFLES INTERNATIONAL SCHOOL -UM SUQEIM SOUTH BR,Raffles International School -Um Suqeim South BR,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088710
RAFFLES WORLD ACADEMY,Raffles World Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088713
RAHA INTERNATIONAL SCHOOL,Raha International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q17069707
RAINTREE ROLLA HOTEL,Raintree Rolla Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150436
RAISING CANE'S,Raising Cane's,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
RAMADA ABU DHABI CORNICHE,Ramada Abu Dhabi Corniche,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997689
RAMADA DOWNTOWN ABU DHABI,Ramada Downtown Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997636
RAMADA DOWNTOWN DUBAI,Ramada Downtown Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111151472
RAMADA HOTEL & SUITES AJMAN,Ramada Hotel & Suites Ajman,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997714
RAMADA HOTEL & SUITES BY WYNDHAM JBR,Ramada Hotel & Suites by Wyndham JBR,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150709
RAMADA BY WYNDHAM BEACH HOTEL AJMAN,Ramada by Wyndham Beach Hotel Ajman,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150608
RAMADA BY WYNDHAM DUBAI BARSHA HEIGHTS,Ramada by Wyndham Dubai Barsha Heights,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150213
RAMEE ROYAL HOTEL,Ramee Royal Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150447
RANCHES PRIMARY SCHOOL,Ranches Primary School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088720
RAS AL KHAIMAH ACADEMY,Ras Al Khaimah Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7294634
RAS AL KHAIMAH FREE TRADE ZONE,Ras Al Khaimah Free Trade Zone,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q2013744
RAS AL KHAIMAH HOTEL,Ras Al Khaimah Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150647
RASHID HOSPITAL,Rashid Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q7294896
RASHID SCHOOL,Rashid School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089028
RASHID SCHOOL FOR BOYS,Rashid School For Boys,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7294921
RAVI RESTAURANT,Ravi Restaurant,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
RAVINARO,Ravinaro,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141598324
RAVIZ CENTER POINT HOTEL,Raviz Center Point Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150446
RAWA,Rawa,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141806007
RAYNA TOURS,Rayna Tours,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
RECOHUB,Recohub,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141801195
RED CASTLE HOTEL,Red Castle Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856058
REDINGTON (INDIA) LIMITED,Redington (India) Limited,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7305951
REEL CINEMAS,Reel Cinemas,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
REEM MALL,Reem Mall,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q117751497
REFINA,Refina,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141912926
REFLECTIONS HOTEL,Reflections Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997639
REGENT INTERNATIONAL PRIVATE SCHOOL,Regent International Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088721
REGENT INTERNATIONAL SCHOOL,Regent International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q56277581
REGENT PALACE HOTEL,Regent Palace Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997649
RENAISSANCE BUSINESS BAY HOTEL,Renaissance Business Bay Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q142083541
RENAISSANCE SCHOOL,Renaissance School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089066
RENECO (UNITED ARAB EMIRATES),Reneco (United Arab Emirates),Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q107518646
REPTON DUBAI,Repton Dubai,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
REPTON SCHOOL,Repton School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088723
REPTON SCHOOL DUBAI,Repton School Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7314368
RESIDENCE INN BY MARRIOTT AL JADDAF,Residence Inn by Marriott Al Jaddaf,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997637
REVIER DUBAI,Revier Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856028
RHODIUM FX,Rhodium FX,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141143074
RISING SCHOOL LLC,Rising School LLC,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089026
RIVERSTON SCHOOL DUBAI,Riverston School Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089056
RIVIERA HOTEL,Riviera Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150475
RIXOS BAB AL BAHR - ALL INCLUSIVE,Rixos Bab Al Bahr - All Inclusive,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150625
RIXOS PREMIUM DUBAI JBR,Rixos Premium Dubai JBR,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150722
RIXOS PREMIUM SAADIYAT ISLAND – ULTRA ALL INCLUSIVE,Rixos Premium Saadiyat Island – Ultra All Inclusive,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150666
RIXOS THE PALM LUXURY SUITE COLLECTION,Rixos the Palm Luxury Suite Collection,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150233
RK DANCE STUDIO DUBAI,Rk Dance Studio Dubai,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q116802790
ROCHESTER INSTITUTE OF TECHNOLOGY OF DUBAI,Rochester Institute of Technology of Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7353990
RODA AL MUROOJ RESIDENCES,Roda Al Murooj Residences,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997628
RODA AMWAJ SUITES,Roda Amwaj Suites,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111331540
RODA BEACH RESORT,Roda Beach Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150284
RODA LINKS AL NASR,Roda Links Al Nasr,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150411
ROSE GARDEN HOTEL APARTMENTS - BARSHA,Rose Garden Hotel Apartments - Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150253
ROSE GARDEN HOTEL APARTMENTS - BUR DUBAI,Rose Garden Hotel Apartments - Bur Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150442
ROSE PARK HOTEL AL BARSHA,Rose Park Hotel Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150248
ROSE PLAZA HOTEL AL BARSHA,Rose Plaza Hotel Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997622
ROSE TOWER,Rose Tower,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q648338
ROSEWOOD ABU DHABI,Rosewood Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q2167337
ROTANA,Rotana,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ROTANA JET,Rotana Jet,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q4845484
ROVE AT THE PARK,Rove At The Park,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856081
ROVE CITY CENTRE,Rove City Centre,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150504
ROVE DOWNTOWN,Rove Downtown,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150337
ROVE DUBAI MARINA,Rove Dubai Marina,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997739
ROVE HEALTHCARE CITY,Rove Healthcare City,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150409
ROVE HOTELS,Rove Hotels,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ROVE LA MER BEACH,Rove La Mer Beach,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150343
ROVE TRADE CENTRE,Rove Trade Centre,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150388
ROXY CINEMAS,Roxy Cinemas,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ROYAL ASCOT HOTEL,Royal Ascot Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150438
ROYAL BEACH HOTEL & RESORT,Royal Beach Hotel & Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150665
ROYAL CENTRAL HOTEL THE PALM,Royal Central Hotel The Palm,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150236
ROYAL CONTINENTAL HOTEL,Royal Continental Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150498
ROYAL FALCON HOTEL,Royal Falcon Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150534
ROYAL GRAND SUITE HOTEL,Royal Grand Suite Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150586
ROYAL JET,Royal Jet,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q7374357
ROYAL M HOTEL FUJAIRAH MALL,Royal M Hotel Fujairah Mall,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150632
"ROYAL ROSE ABU DHABI, A CURIO COLLECTION BY HILTON AFFILIATED HOTEL","Royal Rose Abu Dhabi, a Curio Collection by Hilton Affiliated Hotel",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150382
ROYAL VIEW HOTEL,Royal View Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997726
ROYALE STAYS - PROPERTY MANAGEMENT DUBAI,Royale Stays - Property Management Dubai,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140361158
ROYALTON HOTEL,Royalton Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997675
RUSSIAN INTERNATIONAL SCHOOL,Russian International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088725
RUSSIAN INTERNATIONAL SCHOOL IN DUBAI,Russian International School in Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q21666064
RUSTAR FLOATING RESTAURANT,Rustar Floating Restaurant,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7382455
SEWA,SEWA,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SKORB,SKORB,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q16960304
SLS DUBAI HOTEL & RESIDENCES,SLS Dubai Hotel & Residences,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150316
SNOXFEDC,SNOXFEDC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141178355
STARZPLAY,STARZPLAY,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SAADIYAT ROTANA RESORT AND VILLAS,Saadiyat Rotana Resort and Villas,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150574
SABARI INDIAN SCHOOL LLC,Sabari Indian School LLC,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088728
SADDLE,Saddle,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SAFA BRITISH SCHOOL,Safa British School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088162
SAFA COMMUNITY SCHOOL,Safa Community School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088732
SAFFRON BOUTIQUE HOTEL,Saffron Boutique Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111111806
SAFFRON HOTEL,Saffron Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150508
SAHARA BEACH RESORT & SPA,Sahara Beach Resort & Spa,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997702
SAHARA DUNE ADVENTURES,Sahara Dune Adventures,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q142065243
SAHARA PRINTER RENTALS,Sahara Printer Rentals,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q137021158
SAINT OBJETS,Saint Objets,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139590932
SALIK,Salik,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SAMAYA HOTEL DEIRA,Samaya Hotel Deira,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150478
SAMSUNG STORE,Samsung Store,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SAN MARCO HOTEL,San Marco Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150536
SANDY BEACH HOTEL & RESORT,Sandy Beach Hotel & Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997728
SARA BEAUTY HOME SPA,Sara Beauty Home Spa,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140367531
SAUDI GERMAN HOSPITAL,Saudi German Hospital,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SAUDIA,Saudia,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SAVOY CENTRAL HOTEL APARTMENTS,Savoy Central Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150429
SAVOY CREST HOTEL APARTMENT,Savoy Crest Hotel Apartment,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150431
SAVOY PARK HOTEL APARTMENTS,Savoy Park Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111331500
SAVOY SUITES HOTEL APARTMENTS,Savoy Suites Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111331502
SCRYDE TECH,Scryde Tech,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q138848971
SEA VIEW HOTEL DUBAI,Sea View Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150412
SEAWORLD ABU DHABI,SeaWorld Abu Dhabi,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SEAWINGS,Seawings,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q7442287
SECURITY QUOTIENT,Security Quotient,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140547154
SEOUL ROUTINE,Seoul Routine,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141929664
SEPHORA,Sephora,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SETIX,Setix,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140043924
SHAHID,Shahid,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SHAIKH KHALIFA BIN ZAYED BANGLADESH ISLAMIA SCHOOL,Shaikh Khalifa Bin Zayed Bangladesh Islamia School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7462421
SHAKE SHACK,Shake Shack,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SHAMIL,Shamil,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SHANGRI-LA DUBAI,Shangri-La Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150336
"SHANGRI-LA QARYAT AL BERI, ABU DHABI","Shangri-La Qaryat Al Beri, Abu Dhabi",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997602
SHARAF DG,Sharaf DG,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SHARJAH AMERICAN INTERNATIONAL PRIVATE SCHOOL,Sharjah American International Private school,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088734
SHARJAH AMERICAN INTERNATIONAL SCHOOL,Sharjah American International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7489763
SHARJAH DIRECTORATE OF PUBLIC WORKS,Sharjah Directorate of Public Works,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q18210231
SHARJAH ENGLISH SCHOOL,Sharjah English School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7489767
SHARJAH INDIAN SCHOOL,Sharjah Indian School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7489769
SHARJAH MUNICIPALITY,Sharjah Municipality,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SHARJAH PALACE HOTEL,Sharjah Palace Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997695
SHARJAH POLICE,Sharjah Police,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SHARJAH PREMIERE HOTEL & RESORT,Sharjah Premiere Hotel & Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150596
SHEIKH KHALIFA SPECIALTY HOSPITAL,Sheikh Khalifa Specialty Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q136324149
SHEIKH RASHID BIN SAEED ISLAMIC INSTITUTE,Sheikh Rashid Bin Saeed Islamic Institute,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088737
SHEIN,Shein,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SHERATON ABU DHABI HOTEL & RESORT,Sheraton Abu Dhabi Hotel & Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150561
SHERATON DUBAI CREEK HOTEL & TOWERS,Sheraton Dubai Creek Hotel & Towers,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150469
"SHERATON GRAND HOTEL, DUBAI","Sheraton Grand Hotel, Dubai",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150364
SHERATON JUMEIRAH BEACH RESORT,Sheraton Jumeirah Beach Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150708
"SHERATON MALL OF THE EMIRATES HOTEL, DUBAI","Sheraton Mall of the Emirates Hotel, Dubai",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150276
SHERATON SHARJAH BEACH RESORT AND SPA,Sheraton Sharjah Beach Resort and Spa,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150606
SHOEMART,Shoemart,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SIGMA CAPITAL,Sigma Capital,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140506641
SIGNATURE 1 HOTEL TECOM,Signature 1 Hotel Tecom,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150212
SIGNATURE HOTEL AL BARSHA,Signature Hotel Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997618
SIGNATURE INN DEIRA,Signature Inn Deira,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997681
SIGNATURE INN HOTEL DEIRA,Signature inn Hotel Deira,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111111793
SIMPLIFYLABS,SimplifyLabs,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140420370
SKECHERS,Skechers,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SKI DUBAI,Ski Dubai,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SKYLINK ARABIA,SkyLink Arabia,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q7537187
SKYE VENTURE FZC,Skye Venture FZC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139597231
SKYLARK HOTEL APARTMENTS,Skylark Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150251
SKYLINE UNIVERSITY COLLEGE,Skyline University College,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7537928
SKYRAY CAPITAL,Skyray Capital,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q131909534
SMANA HOTEL AL RAFFA,Smana Hotel Al Raffa,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150399
SMART VISION SCHOOL,Smart Vision School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088739
SNAPCHAT,Snapchat,Digital_Subscriptions,AE,,project_category;descriptor_unverified,project:scripts/rules.py
SNAPCHAT+,Snapchat+,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SOFITEL ABU DHABI CORNICHE,Sofitel Abu Dhabi Corniche,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150555
SOFITEL DUBAI DOWNTOWN,Sofitel Dubai Downtown,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150313
SOFITEL DUBAI JUMEIRAH BEACH,Sofitel Dubai Jumeirah Beach,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150715
SOFITEL DUBAI THE OBELISK,Sofitel Dubai The Obelisk,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150413
SOFITEL DUBAI THE PALM LUXURY APARTMENTS,Sofitel Dubai The Palm Luxury Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150235
SOFITEL DUBAI THE PALM RESORT & SPA,Sofitel Dubai The Palm Resort & Spa,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150238
SOLE RISTORANTE,Sole Ristorante,Food_Dining,AE,,type_mapped,http://www.wikidata.org/entity/Q131292674
SOLVEO SOLUTIONS,Solveo Solutions,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141968098
SOMEWHERE HOTEL APARTMENT,Somewhere Hotel Apartment,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150483
SONDER AT JBR THE WALK,Sonder at JBR The Walk,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111151484
SOUQ EXTRA,Souq Extra,Groceries,AE,,project_category;descriptor_unverified,project:scripts/rules.py
SOUQ.COM,Souq.com,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q22688437
SOUTH VIEW SCHOOL,South View School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089058
SOUTHERN SUN HOTEL ABU DHABI,Southern Sun Hotel Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150565
SPACE IMAGING MIDDLE EAST,Space Imaging Middle East,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7572381
SPARK RESIDENCE DELUXE HOTEL APARTMENTS,Spark Residence Deluxe Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997703
SPINNEYS,Spinneys,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SPLASH,Splash,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SPOTIFY,Spotify,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SPRINGDALES SCHOOL LLC,Springdales School LLC,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088741
ST JOSEPH'S SCHOOL,St Joseph's School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7593860
ST. MARY CATHOLIC HIGH SCHOOL DUBAI - AL MUHAISNAH,St. Mary Catholic High School Dubai - Al Muhaisnah,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088743
ST. MARY'S CATHOLIC HIGH SCHOOL,St. Mary's Catholic High School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7590126
STAR INTERNATIONAL SCHOOL,Star International School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088747
STAR INTERNATIONAL SCHOOL ( BRANCH ),Star International School ( Branch ),Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088749
STAR METRO DEIRA HOTEL APARTMENTS,Star Metro Deira Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150539
STARBUCKS,Starbucks,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
START BUSINESS SERVICES,Start Business Services,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140400410
STAYBRIDGE SUITES ABU DHABI YAS ISLAND,Staybridge Suites Abu Dhabi Yas Island,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q18392962
STAYBRIDGE SUITES DUBAI AL-MAKTOUM AIRPORT,Staybridge Suites Dubai Al-Maktoum Airport,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150680
STAYBRIDGE SUITES DUBAI FINANCIAL CENTRE,Staybridge Suites Dubai Financial Centre,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997630
STEAM,Steam,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
STELLA DI MARE DUBAI MARINA HOTEL,Stella Di Mare Dubai Marina Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150707
STRATALINK,StrataLink,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140889512
STUDIO M ARABIAN PLAZA,Studio M Arabian Plaza,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150577
STUDIO ONE HOTEL,Studio One Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150226
SUBWAY,Subway,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SUHA JBR HOTEL APARTMENTS,Suha JBR Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150725
SUITEFLEET,SuiteFleet,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140136550
SUKOON INSURANCE,Sukoon Insurance,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SUMMERLAND MOTEL,Summerland Motel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856055
SUN & SANDS SEA VIEW HOTEL,Sun & Sands Sea View Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997690
SUN AND SAND SPORTS,Sun and Sand Sports,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SUN AND SANDS HOTEL,Sun and Sands Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150495
SUNMARKE SCHOOL,Sunmarke School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088752
SUNRISE ENGLISH PRIVATE SCHOOL,Sunrise English Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q65079690
SUPER CARE PHARMACY,Super Care Pharmacy,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
SUSTAIN LEADERSHIP CONSULTANCY,Sustain Leadership Consultancy,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q134774207
SWISS INTERNATIONAL SCIENTIFIC SCHOOL,Swiss International Scientific School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088756
SWISS INTERNATIONAL SCIENTIFIC SCHOOL IN DUBAI,Swiss International Scientific School in Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q58768688
SWISSOTEL LIVING AL GHURAIR DUBAI,Swissotel Living Al Ghurair Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150518
SWISSÔTEL AL GHURAIR DUBAI,Swissôtel Al Ghurair Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150520
SWISSÔTEL AL MUROOJ DUBAI,Swissôtel Al Murooj Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997629
SYNAPTICA GROUP,Synaptica Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139594997
SYNCROW,Syncrow,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140718883
SYNERGY UNIVERSITY DUBAI CAMPUS,Synergy University Dubai Campus,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q18211094
TACH,TACH,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q113957074
TAMM,TAMM,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TAQA DISTRIBUTION,TAQA Distribution,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TECOM GROUP,TECOM Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q28016149
TOD,TOD,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TOP GRAND CONTINENTAL FLAMINGO HOTEL,TOP Grand Continental Flamingo Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150375
TRIX20,TRIX20,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141944068
TAALEEM,Taaleem,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TABBY,Tabby,Shopping_Retail,AE,,project_category;descriptor_unverified,project:scripts/rules.py
TABREED,Tabreed,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TADBEER- EXCELLENCE CENTER,Tadbeer- Excellence Center,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q123136467
TAJ DUBAI,Taj Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150305
TAJ JUMEIRAH LAKES TOWERS,Taj Jumeirah Lakes Towers,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150749
TAKAHISA JAPANESE RESTAURANT,Takahisa Japanese restaurant,Food_Dining,AE,,type_mapped,http://www.wikidata.org/entity/Q112117005
TALABAT,Talabat,Food_Dining,AE,,project_category;descriptor_unverified,project:scripts/rules.py
TAMANI HOTEL MARINA,Tamani Hotel Marina,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q2627336
TAMARA,Tamara,Shopping_Retail,AE,,project_category;descriptor_unverified,project:scripts/rules.py
TANAFOS APP,Tanafos App,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141798665
TASHEEL,Tasheel,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TASJEEL,Tasjeel,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TAWAM HOSPITAL,Tawam Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q30281077
TAWJEEH,Tawjeeh,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TAWUNIYA,Tawuniya,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TEAM RHINO MARKETING CONSULTANTS FZE,Team Rhino Marketing Consultants FZE,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140088859
TECHLANCERS MIDDLE EAST,Techlancers Middle East,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139916222
"TELAL RESORT, AL AIN","Telal Resort, Al Ain",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150677
TELECOMMUNICATIONS AND DIGITAL GOVERNMENT REGULATORY AUTHORITY,Telecommunications and Digital Government Regulatory Authority,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7695863
TEMU,Temu,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TEXAS CHICKEN,Texas Chicken,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
THE ABU DHABI EDITION,The Abu Dhabi Edition,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150177
THE ABU DHABI INDIAN SCHOOL,The Abu Dhabi Indian School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q15177994
THE ACT HOTEL,The Act Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150599
THE ALPHA SCHOOL LLC,The Alpha School LLC,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089025
"THE APARTMENTS, DUBAI WORLD TRADE CENTRE HOTEL APARTMENTS","The Apartments, Dubai World Trade Centre Hotel Apartments",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150358
THE AQUILA SCHOOL,The Aquila School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089063
THE ARBOR SCHOOL,The Arbor School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089064
THE ARCADIA PREPARATORY SCHOOL,The Arcadia Preparatory School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088759
THE BRITISH SCHOOL – AL KHUBAIRAT,The British School – Al Khubairat,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7720202
THE CANVAS DUBAI - MGALLERY HOTEL COLLECTION,The Canvas Dubai - MGallery Hotel Collection,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150415
THE CENTRAL SCHOOL,The Central School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088760
"THE CHEDI AL BAIT, SHARJAH","The Chedi Al Bait, Sharjah",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150605
THE CHEESECAKE FACTORY,The Cheesecake Factory,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
THE CHILDRENS GARDEN KINDERGARTEN,The Childrens Garden Kindergarten,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088762
THE CITY SCHOOL INTERNATIONAL PRIVATE,The City School International Private,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088763
THE CLOSET VALET,The Closet Valet,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q135437462
THE COVE ROTANA RESORT RAS AL KHAIMAH,The Cove Rotana Resort Ras Al Khaimah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150643
THE DRY AGE BOUTIQUE,The Dry Age Boutique,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q107342018
THE EMIRATES ACADEMY OF HOSPITALITY MANAGEMENT,The Emirates Academy of Hospitality Management,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q17156215
THE EMIRATES GROUP,The Emirates Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7731899
THE FIRST COLLECTION BUSINESS BAY,The First Collection Business Bay,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q142083561
THE H DUBAI,The H Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150386
THE INDIAN ACADEMY,The Indian Academy,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088766
THE INDIAN HIGH SCHOOL,The Indian High School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088768
"THE INDIAN HIGH SCHOOL, DUBAI","The Indian High School, Dubai",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7741856
THE INDIAN HIGH SCHOOL-BRANCH,The Indian High School-Branch,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088770
THE INDIAN INTERNATIONAL SCHOOL (DSO BRANCH),The Indian International School (DSO Branch),Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088774
THE INTERNATIONAL SCHOOL OF CHOUEIFAT - BRANCH,The International School of Choueifat - Branch,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088777
THE KINDERGARTEN STARTERS,The Kindergarten Starters,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088779
THE LEELA HOTEL,The Leela Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150496
THE LONGBEACH CAMPGROUND,The Longbeach Campground,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150645
THE MANOR BY JA,The Manor by JA,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150692
THE MEYDAN HOTEL,The Meydan Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150291
THE MILLENIUM SCHOOL,The Millenium School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088781
"THE OBEROI BEACH RESORT, AL ZORAH","The Oberoi Beach Resort, Al Zorah",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150616
THE OBEROI BUSINESS BAY,The Oberoi Business Bay,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q7754626
THE OBEROI DUBAI,The Oberoi Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150294
THE PHILIPPINE SCHOOL,The Philippine School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088782
"THE PHILIPPINE SCHOOL, DUBAI","The Philippine School, Dubai",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7756912
THE RETREAT PALM DUBAI MGALLERY BY SOFITEL,The Retreat Palm Dubai MGallery by Sofitel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150244
"THE RITZ-CARLTON ABU DHABI, GRAND CANAL","The Ritz-Carlton Abu Dhabi, Grand Canal",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150193
"THE RITZ-CARLTON RAS AL KHAIMAH, AL HAMRA BEACH","The Ritz-Carlton Ras Al Khaimah, Al Hamra Beach",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150633
"THE RITZ-CARLTON RAS AL KHAIMAH, AL WADI DESERT","The Ritz-Carlton Ras Al Khaimah, Al Wadi Desert",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997720
"THE RITZ-CARLTON, DUBAI","The Ritz-Carlton, Dubai",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150734
"THE RITZ-CARLTON, DUBAI INTERNATIONAL FINANCIAL CENTRE","The Ritz-Carlton, Dubai International Financial Centre",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150348
THE S HOTEL AL BARSHA,The S Hotel Al Barsha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856018
THE SHEFFIELD PRIVATE SCHOOL,The Sheffield Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q18393764
THE ST. REGIS ABU DHABI,The St. Regis Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150187
"THE ST. REGIS SAADIYAT ISLAND RESORT, ABU DHABI","The St. Regis Saadiyat Island Resort, Abu Dhabi",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150573
THE TOWER PLAZA HOTEL DUBAI,The Tower Plaza Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997631
THE UPTOWN HOTEL APARTMENT,The Uptown Hotel Apartment,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997723
THE VIEW AL BARSHA HOTEL APARTMENTS,The View Al Barsha Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997617
"THE WB ABU DHABI, CURIO COLLECTION BY HILTON","The WB Abu Dhabi, Curio Collection by Hilton",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q60752571
THE WALK,The Walk,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q7773263
THE WESTIN ABU DHABI GOLF RESORT & SPA,The Westin Abu Dhabi Golf Resort & Spa,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150380
THE WESTIN DUBAI MINA SEYAHI BEACH RESORT & MARINA,The Westin Dubai Mina Seyahi Beach Resort & Marina,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150753
THE WESTMINSTER SCHOOL,The Westminster School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088784
THE WINCHESTER SCHOOL,The Winchester School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088996
"THE WINCHESTER SCHOOL, JEBEL ALI","The Winchester School, Jebel Ali",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q107121387
THEPAYSTUBS,ThePayStubs,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140051499
THRIFTY,Thrifty,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
THUMBAY GROUP,Thumbay Group,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q17070955
THUMBAY HOSPITAL,Thumbay Hospital,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
THURAYA,Thuraya,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1349140
TICKETMASTER,Ticketmaster,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TIFFANY,Tiffany,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TIKTOK,TikTok,Others,AE,,project_category;descriptor_unverified,project:scripts/rules.py
TILAL LIWA HOTEL - MADINAT ZAYED,Tilal Liwa Hotel - Madinat Zayed,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997597
TIM HORTONS,Tim Hortons,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TIME DUNES HOTEL APARTMENTS OUD METHA,Time Dunes Hotel Apartments Oud Metha,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150408
TIME GRAND PLAZA HOTEL DUBAI,Time Grand Plaza Hotel Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997693
"TIME GRAND PLAZA HOTEL, DUBAI AIRPORT","Time Grand Plaza Hotel, Dubai Airport",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150579
TIME OAK HOTEL & SUITES,Time Oak Hotel & Suites,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150211
TIME ONYX HOTEL APARTMENTS,Time Onyx Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997697
TIME RUBY HOTEL APARTMENTS,Time Ruby Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150591
TIPS AND TOES,Tips and Toes,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TITANIUM FINANCIAL LTD,Titanium Financial Ltd,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141274698
TOMSHER TECHNOLOGIES,Tomsher Technologies,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141612022
TOP STARS HOTEL,Top Stars Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997633
TOP TO BOTTOM SOCIAL,Top To Bottom Social,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140356114
TOPGOLF DUBAI,Topgolf Dubai,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TOWERS ROTANA,Towers Rotana,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150344
TRAVELERVIP,TravelerVIP,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q17035325
TRENDYOL,Trendyol,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TREPPAN HOTEL & SUITES BY FAKHRUDDIN,Treppan Hotel & Suites by Fakhruddin,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150754
TRIBUTECH,Tributech,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141816982
TRIDENT SUPPORT,Trident Support,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q56583145
TRIP.COM,Trip.com,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
TRUMP INTERNATIONAL HOTEL AND TOWER,Trump International Hotel and Tower,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q1782708
TRYP BY WYNDHAM ABU DHABI CITY CENTER,Tryp by Wyndham Abu Dhabi City Center,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150383
TULIP AL BARSHA HOTEL APARTMENT,Tulip Al Barsha Hotel Apartment,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997619
TULIP HOTEL APARTMENTS,Tulip Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150439
"TUMBI HOTEL DUBAI THE PALM, TAPESTRY COLLECTION BY HILTON","Tumbi Hotel Dubai The Palm, Tapestry Collection by Hilton",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q135988378
TUSCAN CONSULTING,Tuscan Consulting,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141962277
TWO SEASONS HOTEL & APARTMENTS FORMER GLORIA,Two Seasons Hotel & Apartments Former Gloria,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150225
TYCOONS CREATORS,Tycoons Creators,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140357411
UAE EXCHANGE,UAE Exchange,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7863720
UAE PEPTIDE LAB,UAE Peptide Lab,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139719513
UPS,UPS,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
UBER,Uber,Transport_Auto,AE,,project_category;descriptor_unverified,project:scripts/rules.py
UDEMY,Udemy,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
UDRIVE,Udrive,Transport_Auto,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
UMM AL QUWAIN UNIVERSITY,Umm Al Quwain University,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q118900038
UNINEST DUBAILAND,Uninest Dubailand,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111111804
UNION COOP,Union Coop,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
UNION NATIONAL BANK,Union National Bank,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q17071108
UNIQLO,Uniqlo,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
UNITED ARAB EMIRATES UNIVERSITY,United Arab Emirates University,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
UNITED INTERNATIONAL PRIVATE SCHOOL,United International Private School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86088999
UNIVERSAL AMERICAN SCHOOL - BRANCH,Universal American School - Branch,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089002
UNIVERSITY OF DUBAI,University of Dubai,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
UNIVERSITY OF KHORFAKKAN,University of Khorfakkan,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q134703678
UNIVERSITY OF SHARJAH,University of Sharjah,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7896294
UNIVERSITY OF WOLLONGONG IN DUBAI,University of Wollongong in Dubai,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
UPTOWN SCHOOL,Uptown School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089003
UPTOWN SCHOOL DUBAI,Uptown School Dubai,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q21707793
UPWORK,Upwork,Others,AE,,project_category;descriptor_unverified,project:scripts/rules.py
URBAN AL KHOORY HOTEL,Urban Al Khoory Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856025
URBAN COMPANY,Urban Company,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
"V HOTEL DUBAI, CURIO COLLECTION BY HILTON","V Hotel Dubai, Curio Collection by Hilton",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q110221761
V HOTEL FUJAIRAH,V Hotel Fujairah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856077
VFS GLOBAL,VFS Global,Government_Fees,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
VOX CINEMAS,VOX Cinemas,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
VAULT WEALTH,Vault Wealth,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141807176
VERCAA,Vercaa,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q124152825
VERONA RESORT,Verona Resort,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111856074
VERRE,Verre,Food_Dining,AE,,type_mapped,http://www.wikidata.org/entity/Q16258506
VERSAILLES BY RAVIZ HOTEL,Versailles by Raviz Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150492
VICTORY HEIGHTS PRIMARY SCHOOL,Victory Heights Primary School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q86089005
VIDA BEACH RESORT UMM AL QUWAIN,Vida Beach Resort Umm Al Quwain,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150622
VIDA CREEK HARBOUR,Vida Creek Harbour,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150400
VIDA DOWNTOWN,Vida Downtown,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150306
VILLA ROTANA HOTEL,Villa Rotana Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997626
VILLAGGIO HOTEL ABU DHABI,Villaggio Hotel Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150367
VIRGIN MEGASTORE,Virgin Megastore,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
VIRGIN MOBILE UAE,Virgin Mobile UAE,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
VISATOP,VisaTop,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140355254
VIVA,Viva,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
VOCO DUBAI,Voco Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150354
VOREL,Vorel,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139902757
W ABU DHABI - YAS ISLAND,W Abu Dhabi - Yas Island,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q1127815
W DUBAI - THE PALM,W Dubai - The Palm,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150743
W MOTORS,W Motors,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5827792
WOLKER,WOLKER,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140918649
WOLKIS,WOLKIS,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140918647
WAFI CITY,Wafi City,Shopping_Retail,AE,,type_mapped,http://www.wikidata.org/entity/Q2659361
WAGAMAMA,Wagamama,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
WAITROSE,Waitrose,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
WALDORF ASTORIA DUBAI INTERNATIONAL FINANCIAL CENTRE,Waldorf Astoria Dubai International Financial Centre,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150347
WALDORF ASTORIA DUBAI PALM JUMEIRAH,Waldorf Astoria Dubai Palm Jumeirah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q34204337
WALDORF ASTORIA RAS AL KHAIMAH,Waldorf Astoria Ras Al Khaimah,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q66423173
WAREHOUSE GYM,Warehouse Gym,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
WARNER BROS WORLD,Warner Bros World,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
WASHMEN,Washmen,Others,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
WASL,Wasl,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
WATERFRONT MARKET,Waterfront Market,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
WE ARE KAIROS,We Are Kairos,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141499509
WE DID IT,We Did It,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q142067042
WECARBON,WeCarbon,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141852480
WEB TONIC,Web Tonic,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q137862551
WELCOME HOTEL APARTMENTS 1,Welcome Hotel Apartments 1,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150420
WELLNESS LABS,Wellness Labs,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139973563
WEST HOTEL,West Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997678
WEST ZONE,West Zone,Groceries,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
WESTERN HOTEL - GHAYATHI,Western Hotel - Ghayathi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150678
WESTERN HOTEL - MADINAT ZAYED,Western Hotel - Madinat Zayed,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150175
WESTFORD,Westford,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q17036156
"WESTMINSTER SCHOOL, DUBAI","Westminster School, Dubai",Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q7989202
WILD WADI,Wild Wadi,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
WITHFEELING,WithFeeling,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140689575
WIZZ AIR,Wizz Air,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
WIZZ AIR ABU DHABI,Wizz Air Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q97332689
WORDCRAFT,Wordcraft,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141720930
WUSOOL CAPITAL,Wusool Capital,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140032972
WYKYK FZ-LLC,Wykyk FZ-LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141283700
WYNDHAM DUBAI DEIRA,Wyndham Dubai Deira,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150461
WYNDHAM DUBAI MARINA,Wyndham Dubai Marina,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997738
WYNDHAM GARDEN AJMAN CORNICHE,Wyndham Garden Ajman Corniche,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150609
XM,XM,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q123257035
XPANCEO,XPANCEO,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q124545010
XVA ART HOTEL,XVA Art Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150456
XBOX,Xbox,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
XCLUSIVE HOTEL APARTMENTS,Xclusive Hotel Apartments,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150424
XCLUSIVE MAPLES HOTEL APARTMENT,Xclusive Maples Hotel Apartment,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150430
XPANSE CGI,Xpanse CGI,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q8044964
YABS PUBLIC RELATIONS MANAGEMENT LLC,YABS Public Relations Management LLC,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140135669
YAS ISLAND ROTANA HOTEL ABU DHABI,Yas Island Rotana Hotel Abu Dhabi,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997731
YAS WATERWORLD,Yas Waterworld,Entertainment,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
YORK INTERNATIONAL HOTEL,York International Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150444
YOUTUBE PREMIUM,YouTube Premium,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ZAATAR W ZEIT,Zaatar w Zeit,Food_Dining,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
"ZABEEL HOUSE BY JUMEIRAH, THE GREENS","Zabeel House by Jumeirah, The Greens",Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150209
ZAGY HOTEL,Zagy Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997671
ZAHRA ALI PHOTOGRAPHY,Zahra Ali Photography,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139671016
ZAIN INTERNATIONAL HOTEL,Zain International Hotel,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111997669
ZARA,Zara,Shopping_Retail,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ZAYED AL AWWAL SECONDARY SCHOOL,Zayed Al Awwal Secondary School,Housing_Education,AE,,type_mapped,http://www.wikidata.org/entity/Q17053990
ZAYED MILITARY HOSPITAL,Zayed Military Hospital,Health_Wellness,AE,,type_mapped,http://www.wikidata.org/entity/Q30281276
ZAYED UNIVERSITY,Zayed University,Housing_Education,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ZIQOO HOTEL APARTMENTS DUBAI,ZiQoo Hotel Apartments Dubai,Travel,AE,,type_mapped,http://www.wikidata.org/entity/Q111150700
ZIARAH TRAVEL,Ziarah Travel,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141818079
ZIINA,Ziina,Others,AE,,project_category;descriptor_unverified,project:scripts/rules.py
ZOMATO,Zomato,Food_Dining,AE,,project_category;descriptor_unverified,project:scripts/rules.py
ZOOM,Zoom,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
ZULEKHA HOSPITAL,Zulekha Hospital,Health_Wellness,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
BEIN CONNECT,beIN CONNECT,Digital_Subscriptions,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
DATAHABIBI,dataHabibi,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140395393
DNATA,dnata,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5285844
DNATA TRAVEL SERVICES,dnata Travel Services,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5285841
DRESS24K,dress24k,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139504113
DU,du,Utilities_Telecom,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
E& INTERNATIONAL HOLDING,e& International Holding,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q132225529
E-JUNIOR,e-Junior,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5321415
ESTAIE,estaie,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141960854
FLYDUBAI,flydubai,Travel,AE,,curated_category;descriptor_unverified,project:independently_curated_public_business_facts
IGNITE ENERGY ACCESS,ignite energy access,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140656114
IMISOFTS,imisofts,Others,AE,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140782827
ABC ISLAMIC BANK,ABC Islamic Bank,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4650172
AMA INTERNATIONAL UNIVERSITY,AMA International University,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q4652536
AHLIA UNIVERSITY,Ahlia University,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q4695192
AL AALI SHOPPING COMPLEX,Al Aali Shopping Complex,Shopping_Retail,BH,,type_mapped,http://www.wikidata.org/entity/Q4253442
AL AREEN PALACE & SPA BY ACCOR,Al Areen Palace & Spa by Accor,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399866
AL BARAKA BANKING GROUP,Al Baraka Banking Group,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4033652
AL ENMA MALL,Al Enma Mall,Shopping_Retail,BH,,type_mapped,http://www.wikidata.org/entity/Q4703779
AL HEKMA INTERNATIONAL SCHOOL,Al Hekma International School,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q55603477
AL MUNTAZAH,Al Muntazah,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4704490
AL MUROOJ HOTEL,Al Murooj Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997563
AL NOOR INTERNATIONAL SCHOOL,Al Noor International School,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q14980519
AL RAJA SCHOOL,Al Raja School,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q4704679
AL RAYA SUITES HOTEL,Al Raya Suites Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997577
AL SAFIR HOTEL,Al Safir Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855966
AL TAAWON SECONDARY SCHOOL,Al Taawon Secondary School,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q48817764
ALUMINUM BAHRAIN,Aluminum Bahrain,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q447457
AMERICAN MISSION HOSPITAL,American Mission Hospital,Health_Wellness,BH,,type_mapped,http://www.wikidata.org/entity/Q28221035
AMERICAN UNIVERSITY OF BAHRAIN,American University of Bahrain,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q85741244
APPLIED SCIENCE UNIVERSITY,Applied Science University,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q4781578
ARAB BANKING CORPORATION,Arab Banking Corporation,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4783149
ARAB OPEN UNIVERSITY,Arab Open University,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q3679860
ARABIAN GULF UNIVERSITY,Arabian Gulf University,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q4118306
ARCH HOTEL,Arch Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855973
ARIG,Arig,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4790574
ARMAN HOTEL JUFFAIR MALL,Arman Hotel Juffair Mall,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997567
ASDAL GULF INN BOUTIQUE HOTEL SEEF,Asdal Gulf Inn Boutique Hotel Seef,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111856003
ATIRAM PREMIER HOTEL,Atiram Premier Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855981
BAHRAIN AIR,Bahrain Air,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q803632
BAHRAIN AIRPORT HOTEL,Bahrain Airport Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997590
BAHRAIN BAYAN SCHOOL,Bahrain Bayan School,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q4842733
BAHRAIN CARLTON HOTEL,Bahrain Carlton Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997559
BAHRAIN DEVELOPMENT BANK,Bahrain Development Bank,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q28405964
BAHRAIN INTERNATIONAL HOTEL,Bahrain International Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997581
BAHRAIN PETROLEUM COMPANY,Bahrain Petroleum Company,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q803640
BAHRAIN POLYTECHNIC,Bahrain Polytechnic,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q4842757
BAHRAIN RADIO AND TELEVISION CORPORATION,Bahrain Radio and Television Corporation,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12203165
BAHRAIN ROYAL MEDICAL SERVICES,Bahrain Royal Medical Services,Health_Wellness,BH,,type_mapped,http://www.wikidata.org/entity/Q4842759
BAHRAIN SCHOOL,Bahrain School,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q4842760
BAHRAIN SPECIALIST HOSPITAL,Bahrain Specialist Hospital,Health_Wellness,BH,,type_mapped,http://www.wikidata.org/entity/Q4842761
BANAGAS,Banagas,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4853777
BATELCO,Batelco,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4868756
BIRLA INSTITUTE OF TECHNOLOGY INTERNATIONAL CENTRE,Birla Institute of Technology International Centre,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q4916525
BLAIRE EXECUTIVE SUITES,Blaire Executive Suites,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997560
BRITISH SCHOOL OF BAHRAIN,British School of Bahrain,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q4970997
CITY CENTRE BAHRAIN,City Centre Bahrain,Shopping_Retail,BH,,type_mapped,http://www.wikidata.org/entity/Q4842738
"COLLEGE OF HEALTH SCIENCES, BAHRAIN","College of Health Sciences, Bahrain",Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q5146725
CONRAD BAHRAIN FINANCIAL HARBOUR,Conrad Bahrain Financial Harbour,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q131459487
CROWNE PLAZA BAHRAIN,Crowne Plaza Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399884
CRYSTAL PALACE HOTEL,Crystal Palace Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997574
DHL INTERNATIONAL AVIATION ME,DHL International Aviation ME,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q326794
DANA MALL,Dana Mall,Shopping_Retail,BH,,type_mapped,http://www.wikidata.org/entity/Q16828841
DELMON UNIVERSITY FOR SCIENCE & TECHNOLOGY,Delmon University for Science & Technology,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q5254290
DIVA HOTEL,Diva Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855972
DOWNTOWN ROTANA,Downtown Rotana,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399876
DR. SULAIMAN AL HABIB MEDICAL SERVICES GROUP,Dr. Sulaiman Al Habib Medical Services Group,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12242596
DRAGON HOTEL AND RESORT,Dragon Hotel And Resort,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997592
ELITE CRYSTAL HOTEL,Elite Crystal Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399870
ELITE GRANDE,Elite Grande,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399877
ELITE RESORT & SPA,Elite Resort & Spa,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399886
ELITE SEEF RESIDENCE AND HOTEL,Elite Seef Residence and Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399880
FAKHRO GROUP,Fakhro Group,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5431554
FOUR SEASONS HOTEL BAHRAIN BAY,Four Seasons Hotel Bahrain Bay,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q21619071
FRASER SUITES DIPLOMATIC AREA BAHRAIN,Fraser Suites Diplomatic Area Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399883
FRASER SUITES SEEF BAHRAIN,Fraser Suites Seef Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111888202
FRENCH SCHOOL OF BAHRAIN,French School of Bahrain,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q19903998
FRSAN PLAZA,Frsan Plaza,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997569
GRAND SAFIR HOTEL,Grand Safir Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997570
GULF AVIATION,Gulf Aviation,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q5617382
GULF COURT HOTEL,Gulf Court Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997578
GULF GATE HOTEL,Gulf Gate Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855993
GULF HOTEL BAHRAIN,Gulf Hotel Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399868
GULF INTERNATIONAL BANK,Gulf International Bank,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q17060339
GULF PEARL HOTEL,Gulf Pearl Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997580
GULF SUITES HOTEL AMWAJ,Gulf Suites Hotel Amwaj,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997593
GULF TRAVELLER,Gulf Traveller,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q1554282
GULF UNIVERSITY,Gulf University,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q16784179
HAPPY DAYS HOTEL,Happy Days Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997584
HILTON BAHRAIN,Hilton Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q141891904
HILTON BAHRAIN CITY CENTRE HOTEL & RESIDENCES,Hilton Bahrain City Centre Hotel & Residences,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q139792223
HOTEL DIVA MANAMA,Hotel Diva Manama,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997571
IBIS SEEF MANAMA,Ibis Seef Manama,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399871
IBIS STYLES MANAMA DIPLOMATIC AREA,Ibis Styles Manama Diplomatic Area,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111856005
IBN AL HYTHAM ISLAMIC SCHOOL,Ibn Al Hytham Islamic School,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q5984175
IBN KHULDOON NATIONAL SCHOOL,Ibn Khuldoon National School,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q5984219
INDIAN SCHOOL,Indian School,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q14966892
INTERCONTINENTAL REGENCY BAHRAIN,InterContinental Regency Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399875
INTERNATIONAL HOSPITAL OF BAHRAIN,International Hospital of Bahrain,Health_Wellness,BH,,type_mapped,http://www.wikidata.org/entity/Q12060763
INVESTCORP,Investcorp,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6060636
ISLAMIC EDUCATION SOCIETY,Islamic Education Society,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q6082432
ISTA SUITES SEEF,Ista Suites Seef,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997587
ITHMAAR BANK,Ithmaar Bank,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q3155929
JOB ALERT SERVICE,Job Alert Service,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140314451
JUFFAIR GATE HOTEL,Juffair Gate Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997562
JUFFAIR MALL,Juffair Mall,Shopping_Retail,BH,,type_mapped,http://www.wikidata.org/entity/Q24211432
KHK MMA,KHK MMA,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q30589011
KHALEEJI COMMERCIAL BANK,Khaleeji Commercial Bank,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6399409
KING HAMAD UNIVERSITY HOSPITAL,King Hamad University Hospital,Health_Wellness,BH,,type_mapped,http://www.wikidata.org/entity/Q43896466
KINGDOM UNIVERSITY,Kingdom University,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q16893462
LAGOONA BEACH LUXURY RESORT AND SPA,Lagoona Beach Luxury Resort and Spa,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855996
LE MÉRIDIEN CITY CENTRE BAHRAIN,Le Méridien City Centre Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399873
LOUMAGE HOTEL & SUITES,Loumage Hotel & Suites,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997583
MTI CONSULTING,MTI Consulting,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q13645604
MADRASAT AL-HIDĀYAH AL-KHULAYFĪYAH,Madrasat al-Hidāyah al-khulayfīyah,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q12241670
MAINSTREAM MEDIA,Mainstream Media,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q17068186
MAJESTIC ARJAAN BY ROTANA – MANAMA,Majestic Arjaan by Rotana – Manama,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399887
MANAMA TOWER HOTEL,Manama Tower Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997582
MANSOURI MANSIONS HOTEL,Mansouri Mansions Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997558
"MARRIOTT EXECUTIVE APARTMENTS MANAMA, BAHRAIN","Marriott Executive Apartments Manama, Bahrain",Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855975
MERCURE GRAND HOTEL SEEF / ALL SUITES,Mercure Grand Hotel Seef / All Suites,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399874
MESHAL HOTEL & SPA,Meshal Hotel & Spa,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997586
MOON PLAZA HOTEL,Moon Plaza Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997557
MÖVENPICK HOTEL BAHRAIN,Mövenpick Hotel Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399888
NASEEM INTERNATIONAL SCHOOL,Naseem International School,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q14980523
NASS CORPORATION B.S.C.,Nass Corporation B.S.C.,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6967349
NATIONAL BANK OF BAHRAIN,National Bank of Bahrain,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6970886
NORDIC HOTEL & SPA,Nordic Hotel & Spa,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997588
NOVOTEL BAHRAIN AL DANA RESORT,Novotel Bahrain Al Dana Resort,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111415794
NUZUL AL SALAM HOTEL,Nuzul Al Salam Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q79468074
OYO 102 SEA SHELL HOTEL,OYO 102 Sea Shell Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111064721
OYO 111 INFINITY SUITES,OYO 111 Infinity Suites,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111064720
OYO 112 SEMIRAMIS HOTEL,OYO 112 Semiramis Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111064722
OYO 115 SUNSHINE TOWER,OYO 115 Sunshine Tower,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111458724
OYO 116 CARAWAN PLAZA HOTEL,OYO 116 Carawan Plaza Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111458725
OYO 117 AL JABRIYA SUITES,OYO 117 Al Jabriya Suites,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111458726
OYO 118 REVIRA HOTEL,OYO 118 Revira Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111064719
OYO 119 LE VONDOME,OYO 119 Le Vondome,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111458723
OYO 121 RAMIYA PLAZA,OYO 121 Ramiya Plaza,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111458722
OYO 122 MAJESTIC HOTEL,OYO 122 Majestic Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111458727
OYO 123 ORYX TOWER,OYO 123 Oryx Tower,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111458728
ONE PAVILION LUXURY SERVICED APARTMENTS,One Pavilion Luxury Serviced Apartments,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855959
ORANGE SUITES HOTEL,Orange Suites Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997566
ORBIT COMMUNICATIONS COMPANY,Orbit Communications Company,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q3355200
ORIENTAL PALACE HOTEL,Oriental Palace Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855990
"PAKISTAN URDU SCHOOL, BAHRAIN","Pakistan Urdu School, Bahrain",Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q14980525
PANORAMA HOTEL,Panorama Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997565
PARK REGIS LOTUS HOTEL,Park Regis Lotus Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997575
PEARL BAHRAIN SUITES,Pearl Bahrain Suites,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997573
PHOENICIA TOWER HOTEL,Phoenicia Tower Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997585
PROPERTY FINDER,Property Finder,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7250237
PSYCHIATRIC HOSPITAL,Psychiatric Hospital,Health_Wellness,BH,,type_mapped,http://www.wikidata.org/entity/Q30603595
RCSI-BAHRAIN,RCSI-Bahrain,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q12204409
RAMADA HOTEL AND SUITES AMWAJ ISLANDS,Ramada Hotel and Suites Amwaj Islands,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997595
RAMADA BY WYNDHAM BAHRAIN,Ramada by Wyndham Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855965
RAMEE GRAND HOTEL & SPA,Ramee Grand Hotel & Spa,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855999
RAMEE INTERNATIONAL HOTEL,Ramee International Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855963
RAMEE PALACE HOTEL,Ramee Palace Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855983
RAMEE ROSE HOTEL,Ramee Rose Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855978
REEF BOUTIQUE HOTEL,Reef Boutique Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997589
RESIDENCE INN BY MARRIOTT MANAMA JUFFAIR,Residence Inn by Marriott Manama Juffair,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855970
ROTANA HOTELS,Rotana Hotels,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7370229
ROYAL PHOENICIA HOTEL,Royal Phoenicia Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855956
ROYAL UNIVERSITY FOR WOMEN,Royal University for Women,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q7374950
S HOTEL BAHRAIN,S Hotel Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111331536
SEEF MALL,Seef Mall,Shopping_Retail,BH,,type_mapped,http://www.wikidata.org/entity/Q7445722
SHAMIL BANK OF BAHRAIN,Shamil Bank of Bahrain,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7487548
SITRA MALL,Sitra Mall,Shopping_Retail,BH,,type_mapped,http://www.wikidata.org/entity/Q7532007
SOFITEL BAHRAIN ZALLAQ THALASSA SEA & SPA,Sofitel Bahrain Zallaq Thalassa Sea & Spa,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111415797
SOMERSET AL FATEH BAHRAIN,Somerset Al Fateh Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855988
"ST. CHRISTOPHER'S SCHOOL, BAHRAIN","St. Christopher's School, Bahrain",Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q7587548
STC BAHRAIN,Stc Bahrain,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7907093
SWIFTAIR BAHRAIN,Swiftair Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q7656104
SWISS INTERNATIONAL PALACE HOTEL MANAMA,Swiss International Palace Hotel Manama,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111888201
SWISS-BELHOTEL SEEF BAHRAIN,Swiss-Belhotel Seef Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399879
SWISS-BELSUITES ADMIRAL JUFFAIR,Swiss-Belsuites Admiral Juffair,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997561
TAKAUD SAVINGS AND PENSIONS B.S.C.,Takaud Savings and Pensions B.S.C.,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q17070783
TEXEL AIR,Texel Air,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q60776486
THE ART HOTEL & RESORT,The Art Hotel & Resort,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111415796
THE AVENUES,The Avenues,Shopping_Retail,BH,,type_mapped,http://www.wikidata.org/entity/Q28221516
THE BAHRAIN MALL,The Bahrain Mall,Shopping_Retail,BH,,type_mapped,http://www.wikidata.org/entity/Q7715343
THE BENEFIT COMPANY,The Benefit Company,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7716512
THE DIPLOMAT RADISSON BLU HOTEL RESIDENCE & SPA,The Diplomat Radisson Blu Hotel Residence & Spa,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399882
THE DOMAIN BAHRAIN HOTEL AND SPA,The Domain Bahrain Hotel and Spa,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399881
THE GROVE RESORT BAHRAIN,The Grove Resort Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997591
THE JUFFAIR GRAND HOTEL,The Juffair Grand Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855961
THE K HOTEL,The K Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399869
THE MERCHANT HOUSE,The Merchant House,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855995
"THE OLIVE HOTEL, JUFFAIR","The Olive Hotel, Juffair",Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855968
THE PALACE BOUTIQUE HOTEL,The Palace Boutique Hotel,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855957
"THE RITZ-CARLTON, BAHRAIN","The Ritz-Carlton, Bahrain",Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399885
THE SEA LOFT BOUTIQUE CHALETS,The Sea Loft Boutique Chalets,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997594
THE WESTIN CITY CENTRE BAHRAIN,The Westin City Centre Bahrain,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399872
TRADE ARABIA,Trade Arabia,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7831926
TULIP HOTEL & SUITES,Tulip Hotel & Suites,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997579
TYREPLUS,Tyreplus,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q110959120
UNIVERSITY COLLEGE OF BAHRAIN,University College of Bahrain,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q7894645
UNIVERSITY OF BAHRAIN,University of Bahrain,Housing_Education,BH,,type_mapped,http://www.wikidata.org/entity/Q1707779
VICTORIA MEMORIAL HOSPITAL,Victoria Memorial Hospital,Health_Wellness,BH,,type_mapped,http://www.wikidata.org/entity/Q107335311
VITA TOWER - FAMILIES ONLY,Vita Tower - Families Only,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111997572
VITOL BAHRAIN E.C.,Vitol Bahrain E.C.,Others,BH,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q113466682
WYNDHAM GARDEN MANAMA,Wyndham Garden Manama,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111399867
WYNDHAM GRAND MANAMA,Wyndham Grand Manama,Travel,BH,,type_mapped,http://www.wikidata.org/entity/Q111855985
360 MALL,360 Mall,Shopping_Retail,KW,,type_mapped,http://www.wikidata.org/entity/Q16198266
A'TAKAMUL INTERNATIONAL SCHOOL,A'takamul International School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q4646824
ABDULLAH AL SALEM UNIVERSITY,Abdullah Al Salem University,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q131439674
ADAMS HOTEL,Adams Hotel,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997455
ADAN HOSPITAL,Adan Hospital,Health_Wellness,KW,,type_mapped,http://www.wikidata.org/entity/Q17334875
AGILITY LOGISTICS,Agility Logistics,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4692553
AHLI UNITED BANK KUWAIT,Ahli United Bank Kuwait,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q18746437
AL AHLI BANK OF KUWAIT,Al Ahli Bank of Kuwait,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12184633
AL BASTAKI INTERNATIONAL HOTEL,Al Bastaki International Hotel,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997454
AL HAMRA HOTEL KUWAIT,Al Hamra Hotel Kuwait,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997452
AL JAHRA COPTHORNE HOTEL & RESORT,Al Jahra Copthorne Hotel & Resort,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855806
AL KOUT MALL,Al Kout Mall,Shopping_Retail,KW,,type_mapped,http://www.wikidata.org/entity/Q12217376
AL OMOOMA HOSPITAL,Al Omooma Hospital,Health_Wellness,KW,,type_mapped,http://www.wikidata.org/entity/Q30280924
AL-NIBRAS SCHOOL FOR SPECIAL NEEDS,Al-Nibras School For Special Needs,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q4703026
AL-SABAH HOSPITAL,Al-Sabah Hospital,Health_Wellness,KW,,type_mapped,http://www.wikidata.org/entity/Q30254328
AL-SHIFA HOSPITAL,Al-Shifa Hospital,Health_Wellness,KW,,type_mapped,http://www.wikidata.org/entity/Q54874764
AMERICAN BILINGUAL SCHOOL,American Bilingual School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q4743174
AMERICAN CREATIVITY ACADEMY,American Creativity Academy,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q4743561
AMERICAN INTERNATIONAL SCHOOL OF KUWAIT,American International School of Kuwait,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q4744186
AMERICAN SCHOOL OF KUWAIT,American School of Kuwait,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q4744941
AMERICAN UNIVERSITY OF KUWAIT,American University of Kuwait,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q4116094
AMERICAN UNIVERSITY OF THE MIDDLE EAST,American University of the Middle East,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q21190378
AMIRI HOSPITAL,Amiri Hospital,Health_Wellness,KW,,type_mapped,http://www.wikidata.org/entity/Q4746760
AQUAMARINE KUWAIT RESORT(FAMILIES ONLY),Aquamarine Kuwait Resort(Families Only),Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997467
ARGAN AL BIDAA HOTEL AND RESORT,Argan Al Bidaa Hotel and Resort,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997464
ASSIMA MALL,Assima Mall,Shopping_Retail,KW,,type_mapped,http://www.wikidata.org/entity/Q109547477
BEST WESTERN PLUS MAHBOULA,Best Western Plus Mahboula,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855822
BEST WESTERN PLUS SALMIYA,Best Western Plus Salmiya,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855820
BOUDL KUWAIT AL FAHAHIL,Boudl Kuwait Al Fahahil,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997466
BOUSHAHRI CLINIC,Boushahri Clinic,Health_Wellness,KW,,type_mapped,http://www.wikidata.org/entity/Q50036543
CARLTON TOWER HOTEL KUWAIT,Carlton Tower Hotel Kuwait,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997450
CARMEL SCHOOL,Carmel School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q5043323
CHEST DISEASES HOSPITAL,Chest Diseases Hospital,Health_Wellness,KW,,type_mapped,http://www.wikidata.org/entity/Q30279781
CITY TOWER HOTEL,City Tower Hotel,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855815
COMMERCIAL BANK OF KUWAIT,Commercial Bank of Kuwait,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12184638
COMORO GULF HOLDINGS (CGH),Comoro Gulf Holdings (CGH),Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q113904766
COSTA DEL SOL HOTEL BY ARABIAN LINK,Costa Del Sol Hotel by Arabian Link,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855818
COURTYARD BY MARRIOTT KUWAIT CITY,Courtyard by Marriott Kuwait City,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855813
CROWNE PLAZA KUWAIT AL THURAYA CITY,Crowne Plaza Kuwait Al Thuraya City,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855812
DALAL CITY HOTEL,Dalal City Hotel,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997460
DANAFACTORY,DanaFactory,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141411288
DASMAN MODEL SCHOOL,Dasman Model School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q5226797
ENGLISH SCHOOL FAHAHEEL KUWAIT,English School Fahaheel Kuwait,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q16891051
FAHAHEEL AL-WATANIEH INDIAN PRIVATE SCHOOL,Fahaheel Al-Watanieh Indian Private School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q5429505
FARWANIYA HOSPITAL,Farwaniya Hospital,Health_Wellness,KW,,type_mapped,http://www.wikidata.org/entity/Q17334874
FAST TELECOMMUNICATIONS,Fast Telecommunications,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5436994
FOUR POINTS BY SHERATON KUWAIT,Four Points by Sheraton Kuwait,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111399773
FOUR SEASONS HOTEL KUWAIT AT BURJ ALSHAYA,Four Seasons Hotel Kuwait at Burj Alshaya,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855811
GRAND HOTEL,Grand Hotel,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997465
GRAND HYATT KUWAIT,Grand Hyatt Kuwait,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q136100891
GRAND HYATT KUWAIT RESIDENCES,Grand Hyatt Kuwait Residences,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q136468249
GRAND MAJESTIC HOTEL KUWAIT,Grand Majestic Hotel Kuwait,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997451
GRYPHON AIRLINES,Gryphon Airlines,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q5612437
GULF ENGLISH SCHOOL OF KUWAIT,Gulf English School of Kuwait,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q28135048
GULF INDIAN SCHOOL,Gulf Indian School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q17048354
GULF UNIVERSITY FOR SCIENCE AND TECHNOLOGY,Gulf University for Science and Technology,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q1024668
HAMPTON BY HILTON KUWAIT SALMIYA,Hampton by Hilton Kuwait Salmiya,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q131471416
HILTON GARDEN INN KUWAIT,Hilton Garden Inn Kuwait,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q96787014
HILTON KUWAIT RESORT,Hilton Kuwait Resort,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q56478942
HILTON OLYMPIA KUWAIT,Hilton Olympia Kuwait,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q5764674
HOLIDAY INN KUWAIT,Holiday Inn Kuwait,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111399785
HOLIDAY INN KUWAIT AL THURAYA CITY,Holiday Inn Kuwait Al Thuraya City,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111399774
HYATT REGENCY AL KOUT MALL,Hyatt Regency Al Kout Mall,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111399787
IBIS KUWAIT SALMIYA,Ibis Kuwait Salmiya,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111399777
IBN SINA HOSPITAL,Ibn Sina Hospital,Health_Wellness,KW,,type_mapped,http://www.wikidata.org/entity/Q30280070
INDIA INTERNATIONAL SCHOOL,India International School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q6019356
INDIAN CENTRAL SCHOOL,Indian Central School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q6019994
INDIAN COMMUNITY SCHOOL,Indian Community School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q6020060
INDIAN EDUCATIONAL SCHOOL,Indian Educational School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q19599682
INDIAN ENGLISH ACADEMY SCHOOL,Indian English Academy School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q6020264
INN & GO KUWAIT PLAZA HOTEL,Inn & Go Kuwait Plaza Hotel,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855808
INTERCONTINENTAL KUWAIT DOWNTOWN,InterContinental Kuwait Downtown,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q6044865
INTERNATIONAL SCHOOL OF PAKISTAN,International School of Pakistan,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q17064179
JW MARRIOTT KUWAIT CITY,JW Marriott Kuwait City,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q15229082
JABER AL AHMAD HOSPITAL,Jaber al Ahmad hospital,Health_Wellness,KW,,type_mapped,http://www.wikidata.org/entity/Q25450442
JABRIYA INDIAN SCHOOL,Jabriya Indian School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q6110303
JAHRA HOSPITAL,Jahra Hospital,Health_Wellness,KW,,type_mapped,http://www.wikidata.org/entity/Q17334871
JARIR BOOKSTORE,Jarir Bookstore,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6160243
JUMEIRAH MESSILAH BEACH HOTEL & SPA KUWAIT,Jumeirah Messilah Beach Hotel & Spa Kuwait,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111399786
KIRA,KIRA,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140354531
KOUT FOOD GROUP,Kout Food Group,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q16998655
KUWAIT COLLEGE OF SCIENCE AND TECHNOLOGY,Kuwait College of Science and Technology,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q39060049
KUWAIT CONTINENTAL HOTEL,Kuwait Continental Hotel,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997453
KUWAIT ENGLISH SCHOOL,Kuwait English School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q6448832
KUWAIT FINANCE HOUSE,Kuwait Finance House,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q2336459
KUWAIT FUND FOR ARAB ECONOMIC DEVELOPMENT,Kuwait Fund for Arab Economic Development,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4166585
KUWAIT INTERNATIONAL BANK,Kuwait International Bank,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q30595374
KUWAIT NATIONAL CINEMA COMPANY,Kuwait National Cinema Company,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6448856
KUWAIT OIL COMPANY,Kuwait Oil Company,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q3113538
KUWAIT PETROLEUM CORPORATION,Kuwait Petroleum Corporation,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1634762
KUWAIT PETROLEUM INTERNATIONAL,Kuwait Petroleum International,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4119207
KUWAIT TECHNICAL COLLEGE,Kuwait Technical College,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q28136908
KUWAIT UNIVERSITY,Kuwait University,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q3273657
KUWAIT UNIVERSITY AND MATERNITY HOSPITAL,Kuwait University and Maternity Hospital,Health_Wellness,KW,,type_mapped,http://www.wikidata.org/entity/Q103018381
LAGUNA HOTEL SUITES,Laguna Hotel Suites,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997459
LE JAZZ HOTEL,Le Jazz Hotel,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997457
LE ROYAL EXPRESS SALMIYA HOTEL,Le Royal Express Salmiya Hotel,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997462
LE ROYAL HOTEL,Le Royal Hotel,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855817
LYCÉE FRANÇAIS DE KOWEÏT,Lycée Français de Koweït,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q3269102
M.H. ALSHAYA CO.,M.H. Alshaya Co.,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q61071558
MARINA ROYAL HOTEL SUITE,Marina Royal Hotel Suite,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997458
MEZZAN HOLDING,Mezzan Holding,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q136689409
MILLENNIUM CENTRAL KUWAIT DOWNTOWN,Millennium Central Kuwait Downtown,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111399776
MILLENNIUM HOTEL & CONVENTION CENTRE KUWAIT,Millennium Hotel & Convention Centre Kuwait,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855819
MUBARAK AL-KABEER HOSPITAL,Mubarak Al-Kabeer Hospital,Health_Wellness,KW,,type_mapped,http://www.wikidata.org/entity/Q6930826
MUBARAK AL-ABDULLAH JOINT COMMAND AND STAFF COLLEGE,Mubarak al-Abdullah Joint Command and Staff College,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q12236170
MÖVENPICK HOTEL & RESORT AL BIDA'A,Mövenpick Hotel & Resort Al Bida'a,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111399779
MÖVENPICK HOTEL KUWAIT,Mövenpick Hotel Kuwait,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111399772
NATIONAL BANK OF KUWAIT,National Bank of Kuwait,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4045072
NEW ENGLISH SCHOOL,New English School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q17068953
NEW KUWAIT PHILIPPINES INTERNATIONAL SCHOOL,New Kuwait Philippines International School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q23808562
NEW PAKISTAN INTERNATIONAL SCHOOL,New Pakistan International School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q7010893
OASIS HOTEL,Oasis Hotel,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855809
OOREDOO KUWAIT,Ooredoo Kuwait,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q3067960
PAKISTAN SCHOOL AND COLLEGE,Pakistan School and College,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q7125694
PETZONE,Petzone,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q104532444
PHILIPPINE INTERNATIONAL ENGLISH SCHOOL,Philippine International English School,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q25058404
PLAZA ATHENEE HOTEL,Plaza Athenee Hotel,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997456
PRECISION CONSULTANCY,Precision Consultancy,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q137700839
"RADISSON BLU HOTEL, KUWAIT","Radisson Blu Hotel, Kuwait",Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111399783
RAMADA ENCORE BY WYNDHAM KUWAIT DOWNTOWN,Ramada Encore by Wyndham Kuwait Downtown,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855816
RAOUM INN,Raoum Inn,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997463
RIVA FASHION,Riva Fashion,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q55631748
ROTEX,Rotex,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140211051
SAFIR FINTAS HOTEL KUWAIT,Safir Fintas Hotel Kuwait,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855821
SAFIR HOTELS & RESORTS,Safir Hotels & Resorts,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q7398800
SAKHR SOFTWARE COMPANY,Sakhr Software Company,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7402957
SALMIYA SOUQ,Salmiya Souq,Shopping_Retail,KW,,type_mapped,http://www.wikidata.org/entity/Q16887575
SEA OF SINBAD,Sea of Sinbad,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141589665
"SHERATON KUWAIT, A LUXURY COLLECTION HOTEL, KUWAIT CITY","Sheraton Kuwait, a Luxury Collection Hotel, Kuwait City",Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111855807
SYMPHONY STYLE HOTEL KUWAIT,Symphony Style Hotel Kuwait,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111399778
TRUE FOR GENERAL TRADING & CONTRACTING CO.,TRUE For General Trading & Contracting Co.,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140933663
THE BRITISH SCHOOL OF KUWAIT,The British School of Kuwait,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q7720200
THE CONVENTION CENTER & ROYAL SUITES HOTEL,The Convention Center & Royal Suites Hotel,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111997449
"THE ENGLISH SCHOOL, KUWAIT","The English School, Kuwait",Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q7732249
THE KUWAITI DANISH DAIRY COMPANY KCSC,The Kuwaiti Danish Dairy Company KCSC,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q115628904
THE PALMS BEACH HOTEL & SPA,The Palms Beach Hotel & Spa,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111399782
THE PUBLIC AUTHORITY FOR APPLIED EDUCATION AND TRAINING,The Public Authority for Applied Education and Training,Housing_Education,KW,,type_mapped,http://www.wikidata.org/entity/Q7758687
"THE REGENCY HOTEL, KUWAIT","The Regency Hotel, Kuwait",Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q111399781
TOP KITCHENS GENERAL TRADING CO.,Top Kitchens General Trading Co.,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140184374
TRANS ARABIA AIRWAYS,Trans Arabia Airways,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q14628885
UNITED NETWORKS,United Networks,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7888986
WATANIYA AIRWAYS,Wataniya Airways,Travel,KW,,type_mapped,http://www.wikidata.org/entity/Q1060465
X-CITE BY ALGHANIM ELECTRONICS,X-cite by Alghanim Electronics,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q17141425
YPG MOTORSPORT,YPG Motorsport,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140175623
ZAIN GROUP,Zain Group,Others,KW,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q144364
A'SHARQIYAH UNIVERSITY,A'Sharqiyah University,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q22686991
AL ASALA RESORT,Al Asala Resort,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997481
AL AYJAH PLAZA HOTEL,Al Ayjah Plaza Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855833
AL BALEED RESORT SALALAH BY ANANTARA,Al Baleed Resort Salalah by Anantara,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399802
"AL BUSTAN PALACE, A RITZ-CARLTON HOTEL","Al Bustan Palace, A Ritz-Carlton Hotel",Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399794
AL DYAFA HOTEL SUITES,Al Dyafa Hotel Suites,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997490
AL FALAJ HOTEL,Al Falaj Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399792
AL FERDOUS HOTEL APARTMENTS,Al Ferdous Hotel Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997524
AL HAIL WAVES HOTEL,Al Hail Waves Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855867
AL HAJIS PERFUMES OMAN,Al Hajis Perfumes Oman,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141806499
AL HAMRA GUEST HOUSE,Al Hamra Guest House,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997475
AL HUSN HOTEL MUSCAT,Al Husn Hotel Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q141266141
AL JABAL HOTEL,Al Jabal Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997491
AL KARAM HOTEL APARTMENT,Al Karam Hotel Apartment,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997473
AL MISFAH HOSPITALITY INN,Al Misfah Hospitality Inn,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855831
AL MUROOJ GRAND HOTEL,Al Murooj Grand Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997521
AL MUROOJ HOTEL APARTMENTS,Al Murooj Hotel Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997518
AL NAHDA RESORT & SPA,Al Nahda Resort & Spa,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399807
AL NAHDHA HOSPITAL,Al Nahdha Hospital,Health_Wellness,OM,,type_mapped,http://www.wikidata.org/entity/Q30254318
AL NILE HOTEL,Al Nile Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997485
AL QURUM RESORT,Al Qurum Resort,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855889
AL WADI HOTEL,Al Wadi Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855836
ALALI INVESTMENT,Alali Investment,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141674162
ALASHKHARA BEACH RESORT,Alashkhara Beach Resort,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997507
ALILA HINU BAY,Alila Hinu Bay,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q135988643
ALILA JABAL AKHDAR,Alila Jabal Akhdar,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399806
AMARAH HOTEL,Amarah Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997519
AMERICAN BRITISH ACADEMY,American British Academy,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q4743255
ANANTARA AL JABAL AL AKHDAR RESORT,Anantara Al Jabal Al Akhdar Resort,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399805
ANTIQUE INN,Antique Inn,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997474
ARABIAN ORYX CAMP,Arabian Oryx Camp,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855854
ASFAR HOTEL APARTMENTS,Asfar Hotel Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997522
ATANA STAY AL ASHKARA,Atana Stay Al Ashkara,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997508
ATLAS HOTEL APARTMENTS,Atlas Hotel Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997480
BHD GROUP,BHD Group,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141674074
BANGLADESH SCHOOL MUSCAT,Bangladesh School Muscat,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q25345627
BANKMUSCAT,BankMuscat,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q806607
BARCELÓ MUSSANAH RESORT,Barceló Mussanah Resort,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399808
BEACH BAY HOTEL MUSCAT,Beach Bay Hotel Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855888
BEHLYS BOUTIQUE,Behlys Boutique,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997517
BELAD BONT RESORT,Belad Bont Resort,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855846
BEST WESTERN PREMIER MUSCAT,Best Western Premier Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855887
BOWSHAR INTERNATIONAL HOTEL,Bowshar International Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997523
BRITISH SCHOOL – MUSCAT,British School – Muscat,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q4971016
CARNELIAN BY GLORY BOWER HOTELS,Carnelian by Glory Bower Hotels,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997515
CENTARA MUSCAT HOTEL OMAN,Centara Muscat Hotel Oman,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399812
CITY HOTEL DUQM,City Hotel Duqm,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855824
CITY HOTEL SALALAH,City Hotel Salalah,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997486
CITY PARK HOTEL APARTMENTS,City Park Hotel Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997525
CITY SEASONS HOTEL MUSCAT,City Seasons Hotel Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399819
CORAL MUSCAT HOTEL AND APARTMENTS,Coral Muscat Hotel and Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399822
CROWNE PLAZA DUQM,Crowne Plaza Duqm,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855826
CROWNE PLAZA MUSCAT,Crowne Plaza Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399788
CROWNE PLAZA MUSCAT OCEC,Crowne Plaza Muscat Ocec,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855866
CROWNE PLAZA RESORT SALALAH,Crowne Plaza Resort Salalah,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399801
CROWNE PLAZA SOHAR,Crowne Plaza Sohar,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855837
CUPS BY AA,Cups by AA,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141674160
DARBAT HOTEL,Darbat Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997489
DESERT WONDERS CAMP,Desert Wonders Camp,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997505
DHOFAR PHARMACEUTICAL INDUSTRIES CO. LLC,Dhofar Pharmaceutical Industries Co. LLC,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q131590192
DHOFAR UNIVERSITY,Dhofar University,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q1207665
DIWAN AL AMIR,Diwan Al Amir,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855848
DOLPHIN HOTEL,Dolphin Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997526
DOUBLETREE BY HILTON MUSCAT AL WAHA,DoubleTree by Hilton Muscat Al Waha,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q138913951
DUNES BY AL NAHDA,Dunes by Al Nahda,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855856
ESRA HOTEL APARTMENTS,Esra Hotel Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997492
FALAJ DARIS HOTEL,Falaj Daris Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855829
FANAR HOTEL & RESIDENCES,Fanar Hotel & Residences,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399799
FRASER SUITES MUSCAT,Fraser Suites Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855872
GARDEN HOTEL MUSCAT,Garden Hotel Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997528
GATEWAY SALALAH APARTMENTS,Gateway Salalah Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855843
GERMAN UNIVERSITY OF TECHNOLOGY IN OMAN,German University of Technology in Oman,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q1514056
GOLDEN PALM OASIS,Golden Palm Oasis,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997506
GRAND HYATT MUSCAT,Grand Hyatt Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q5594656
GRAND MILLENNIUM MUSCAT,Grand Millennium Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399813
GREEN OASIS HOTEL,Green Oasis Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997479
HAFFA HOUSE HOTEL,Haffa House Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855834
HILTON GARDEN INN MUSCAT AL KHUWAIR,Hilton Garden Inn Muscat Al Khuwair,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399817
HILTON MUSCAT AL BANDAR,Hilton Muscat Al Bandar,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q140333182
HILTON SALALAH RESORT,Hilton Salalah Resort,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399803
HOLIDAY INN ALSEEB MUSCAT,Holiday Inn AlSeeb Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399809
HOTEL AL MADINAH HOLIDAY,Hotel Al Madinah Holiday,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855868
HOTEL DANAT AL KHALEEJ,Hotel Danat Al Khaleej,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997469
HOTEL INDIGO JABAL AKHDAR RESORT & SPA,Hotel Indigo Jabal Akhdar Resort & Spa,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q139683296
HOTEL MUSCAT HOLIDAY,Hotel Muscat Holiday,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855880
HOTEL SUMMERSANDS,Hotel Summersands,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997509
IBIS MUSCAT,Ibis Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399815
IBRA MOTEL,Ibra Motel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997503
INDIAN SCHOOL AL-SEEB,Indian School Al-Seeb,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q6021541
INDIAN SCHOOL MULADHA,Indian School Muladha,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q15228651
"INDIAN SCHOOL, AL WADI AL KABIR","Indian School, Al Wadi Al Kabir",Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q6021517
"INDIAN SCHOOL, AL-GHUBRA","Indian School, Al-Ghubra",Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q6021511
"INDIAN SCHOOL, DARSAIT","Indian School, Darsait",Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q6021523
"INDIAN SCHOOL, MUSCAT","Indian School, Muscat",Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q6021527
"INDIAN SCHOOL, SALALAH","Indian School, Salalah",Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q17056311
"INDIAN SCHOOL, SOHAR","Indian School, Sohar",Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q6021534
INTERCONTINENTAL MUSCAT,InterContinental Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399820
INTERCITYHOTEL NIZWA,IntercityHotel Nizwa,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997471
INTERCITYHOTEL SALALAH,IntercityHotel Salalah,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855841
JABAL AL AKHDAR GRAND HOTEL,Jabal Al Akhdar Grand Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997496
JAWHARET AL KHEIR FURNISHED APARTMENTS,Jawharet Al Kheir Furnished Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997488
KAIRABA MIRBAT RESORT,Kairaba Mirbat Resort,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855838
KEMPINSKI HOTEL MUSCAT,Kempinski Hotel Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399811
KHASAB HOTEL,Khasab Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855847
KHOULA HOSPITAL,Khoula Hospital,Health_Wellness,OM,,type_mapped,http://www.wikidata.org/entity/Q30280382
LEVATIO HOTEL MUSCAT,Levatio Hotel Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855873
MB HOLDING,MB Holding,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q22948493
MAJAN GUEST HOUSE,Majan Guest House,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855828
MANDARIN ORIENTAL MUSCAT,Mandarin Oriental Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q126502789
MASIRA ISLAND RESORT,Masira Island Resort,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855827
MASIRAH BEACH CAMP,Masirah Beach Camp,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997468
MAZOON UNIVERSITY COLLEGE,Mazoon University College,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q100968499
MERCURE SOHAR,Mercure Sohar,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399795
MILLENNIUM EXECUTIVE APARTMENTS MUSCAT,Millennium Executive Apartments Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855876
MILLENNIUM RESORT SALALAH,Millennium Resort Salalah,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855840
MISFAH OLD HOUSE,Misfah Old House,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855830
MUSCAT CITY CENTRE,Muscat City Centre,Shopping_Retail,OM,,type_mapped,http://www.wikidata.org/entity/Q17126690
MUSCAT DUNES HOTEL,Muscat Dunes Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855869
MUSCAT HILLS HOTEL,Muscat Hills Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997511
MUSCAT INN HOTEL,Muscat Inn Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997520
MUSCAT INTERNATIONAL HOTEL PLAZA,Muscat International Hotel Plaza,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997487
MUSCAT UNIVERSITY,Muscat University,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q130671949
MUTRAH HOTEL,Mutrah Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399793
NATIONAL UNIVERSITY OF SCIENCE AND TECHNOLOGY,National University of Science and Technology,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q84654205
NOMADIC DESERT CAMP,Nomadic Desert Camp,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855850
NOOR MAJAN CAMP,Noor Majan Camp,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997470
NOVOTEL MUSCAT AIRPORT,Novotel Muscat Airport,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399810
NUZHA HOTEL APARTMENTS,Nuzha Hotel Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997477
OQ COMPANY,OQ Company,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q2023013
OYO 103 HOTEL GOLDEN OASIS,OYO 103 Hotel Golden Oasis,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855835
OYO 105 STAR HOUSE 05,OYO 105 Star House 05,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111073810
OYO 106 MUSCAT GRAND HOTEL APARTMENT,OYO 106 Muscat Grand Hotel Apartment,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111068081
OYO 107 AL AREEN HOTEL APARTMENTS,OYO 107 Al Areen Hotel Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111057578
OYO 107 RAS AL HADD WAVES HOTEL,OYO 107 Ras Al Hadd Waves Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997483
OYO 108 MARSA AL MASAFAR HOTEL APARTMENT,OYO 108 Marsa Al Masafar Hotel Apartment,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111057575
OYO 109 AL THABIT MODERN HOTEL APARTMENT,OYO 109 Al Thabit Modern Hotel Apartment,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111068080
OYO 111 AL THABIT HOTEL,OYO 111 Al Thabit Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111057576
OYO 117 MAJESTIC HOTEL,OYO 117 Majestic Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111068083
OYO 119 JASMINE HOTEL APARTMENTS,OYO 119 Jasmine Hotel Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111068078
OYO 122 SAVOY INN HOTEL,OYO 122 Savoy Inn Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111068084
OYO 125 MANAM SOHAR HOTEL APARTMENTS,OYO 125 Manam Sohar Hotel Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111057592
OYO 127 BAIT AL MARMAR HOTEL,OYO 127 Bait Al Marmar Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111057593
OYO 129 AL BAYRAHAA HOTEL APARTMENTS,OYO 129 Al Bayrahaa Hotel Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111068082
OYO 130 AL GAZZAZ FURNISHED APARTMENT,OYO 130 Al Gazzaz Furnished Apartment,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111073811
OMAN AVENUES MALL,Oman Avenues Mall,Shopping_Retail,OM,,type_mapped,http://www.wikidata.org/entity/Q20741112
OMAN LNG,Oman LNG,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q3503110
OMAN MUNITION PRODUCTION COMPANY,Oman Munition Production Company,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q56240208
OMAN OIL MARKETING COMPANY,Oman Oil Marketing Company,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7089539
OMAN AVIATION SERVICES,Oman aviation services,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q134882990
OMANTEL,Omantel,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1535581
OMNI DIGITAL EXPERIENCE,Omni Digital Experience,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141437918
OOREDOO OMAN,Ooredoo Oman,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6982964
ORIENTAL NIGHTS REST HOUSE,Oriental Nights Rest House,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855860
PAKISTAN SCHOOL MUSCAT,Pakistan School Muscat,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q7125692
PAKISTAN SCHOOL SALALAH,Pakistan School Salalah,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q7125693
PARK INN BY RADISSON HOTEL AND RESIDENCE DUQM,Park Inn by Radisson Hotel and Residence Duqm,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855825
PARK INN BY RADISSON MUSCAT,Park Inn by Radisson Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399814
PETROLEUM DEVELOPMENT OMAN,Petroleum Development Oman,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1535587
PHILIPPINE SCHOOL SULTANATE OF OMAN,Philippine School Sultanate of Oman,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q28221096
QURUM BEACH HOTEL,Qurum Beach Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855832
RADISSON BLU HOTEL SOHAR,Radisson Blu Hotel Sohar,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399797
"RADISSON BLU HOTEL, MUSCAT","Radisson Blu Hotel, Muscat",Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399816
RAMADA ENCORE BY WYNDHAM MUSCAT AL-GHUBRA,Ramada Encore by Wyndham Muscat Al-Ghubra,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855874
RAMEE DREAM RESORT,Ramee Dream Resort,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997513
RAMEE GUESTLINE HOTEL QURUM,Ramee Guestline Hotel Qurum,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399789
REACHSCREENS,ReachScreens,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141674161
REMAS HOTEL SUITES,Remas Hotel Suites,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855863
ROYAL FLIGHT OF OMAN,Royal Flight of Oman,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q39057932
ROYAL GARDENS HOTEL,Royal Gardens Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855839
ROYAL GUARD OF OMAN TECHNICAL COLLEGE,Royal Guard of Oman Technical College,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q7374240
ROYAL HOSPITAL,Royal Hospital,Health_Wellness,OM,,type_mapped,http://www.wikidata.org/entity/Q30280773
SAJ FARM INN,SAJ Farm Inn,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997501
SAFARI DESERT CAMP,Safari Desert Camp,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855853
SAFARI DUNES CAMP,Safari Dunes Camp,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997500
SAFARI HOTEL,Safari Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997472
SAFEER CONTINENTAL HOTEL,Safeer Continental Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855878
SAFEER HOTEL SUITES,Safeer Hotel Suites,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997531
SAFEER INTERNATIONAL HOTEL,Safeer International Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855877
SAFEER PLAZA HOTEL,Safeer Plaza Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855879
SAHIL AL SEEB INTERNATIONAL LLC,Sahil Al Seeb International LLC,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140204098
SALALAH GARDENS HOTEL,Salalah Gardens Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855842
SALALAH INTERNATIONAL SCHOOL,Salalah International School,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q28221009
SALALAH ROTANA RESORT,Salalah Rotana Resort,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399800
SALAMAIR,SalamAir,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q27926620
SAMA HOTEL JABAL AL AKHDAR,Sama Hotel Jabal Al Akhdar,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855849
SAMA RAS AL JINZ,Sama Ras Al Jinz,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997482
SAMA WAKAN HERITAGE HOME,Sama Wakan Heritage Home,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997499
SAMA AL WASIL DESERT CAMP,Sama al Wasil Desert Camp,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855851
SAMARA HOTEL,Samara Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855884
SAMHARAM TOURIST VILLAGE,Samharam Tourist Village,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855844
SAND DELIGHT DESERT CAMP,Sand Delight Desert Camp,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111117438
SAVOY GRAND HOTEL APARTMENTS,Savoy Grand Hotel Apartments,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997516
"SHANGRI-LA AL HUSN, MUSCAT","Shangri-La Al Husn, Muscat",Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399796
SHANGRI-LA'S BARR AL JISSAH RESORT & SPA,Shangri-La's Barr Al Jissah Resort & Spa,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q7488567
SHARAKAH,Sharakah,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7489393
SHERATON OMAN HOTEL,Sheraton Oman Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399791
SHORFET AL-ALAMIN HOTEL,Shorfet Al-Alamin Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997495
SIFAWY BOUTIQUE HOTEL,Sifawy Boutique Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399790
SIX SENSES ZIGHY BAY,Six Senses Zighy Bay,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399804
SOHAR HOSPITAL,Sohar Hospital,Health_Wellness,OM,,type_mapped,http://www.wikidata.org/entity/Q7554670
SOHAR UNIVERSITY,Sohar University,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q2496166
SOMERSET PANORAMA MUSCAT,Somerset Panorama Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855870
SOULY ECO LODGE,Souly Eco Lodge,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997484
STARWATCHING PRIVATE CAMP,Starwatching Private Camp,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855852
SULTAN QABOOS HOSPITAL SALALAH,Sultan Qaboos Hospital Salalah,Health_Wellness,OM,,type_mapped,http://www.wikidata.org/entity/Q7636726
SULTAN QABOOS UNIVERSITY,Sultan Qaboos University,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q1808326
SULTAN QABOOS UNIVERSITY HOSPITAL,Sultan Qaboos University Hospital,Health_Wellness,OM,,type_mapped,http://www.wikidata.org/entity/Q30254124
SUN CITY HOTEL,Sun City Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997476
SWISS-BELINN MUSCAT,Swiss-Belinn Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997514
THE AMERICAN INTERNATIONAL SCHOOL MUSCAT,The American International School Muscat,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q24765439
THE CHEDI MUSCAT,The Chedi Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q7722278
THE CLIFF GUEST HOUSE,The Cliff Guest House,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997498
THE PLATINUM,The Platinum,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855886
THE SHAKSY GROUP,The Shaksy Group,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7763621
THE SULTAN'S SCHOOL,The Sultan's School,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q7767233
TURTLE BEACH RESORT,Turtle Beach Resort,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399798
UNIVERSITY OF NIZWA,University Of Nizwa,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q2496107
UNIVERSITY OF BURAIMI,University of Buraimi,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q1683947
UNIVERSITY OF TECHNOLOGY AND APPLIED SCIENCES,University of Technology and Applied Sciences,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q12191827
VENUS HOTEL,Venus Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997530
W MUSCAT,W Muscat,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111399821
WAHIBA BEDOUIN RUSTIC CAMP,Wahiba Bedouin Rustic Camp,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111997502
WAVES INTERNATIONAL HOTEL,Waves International Hotel,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855883
WYNDHAM GARDEN MUSCAT AL KHUWAIR,Wyndham Garden Muscat Al Khuwair,Travel,OM,,type_mapped,http://www.wikidata.org/entity/Q111855885
ARABIAN.CEO,arabian.ceo,Others,OM,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141674163
ÉCOLE FRANÇAISE DE MASCATE,École Française de Mascate,Housing_Education,OM,,type_mapped,http://www.wikidata.org/entity/Q19904024
ADGS (QATAR),ADGS (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q56585277
ABRAJ HOTELS & REAL ESTATE,Abraj Hotels & Real Estate,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141945966
ABRAJ SUITES HOTEL,Abraj Suites Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q141946139
ADAGIO DOHA,Adagio Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969542
AL AZIZIYAH BOUTIQUE HOTEL,Al Aziziyah Boutique Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855890
AL BIDDA BOUTIQUE HOTEL,Al Bidda Boutique Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968406
AL EMADI HOSPITAL,Al Emadi Hospital,Health_Wellness,QA,,type_mapped,http://www.wikidata.org/entity/Q59535190
AL HAZM MALL,Al Hazm Mall,Shopping_Retail,QA,,type_mapped,http://www.wikidata.org/entity/Q115858982
AL JASRA BOUTIQUE HOTEL,Al Jasra Boutique Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968257
AL JAZEERA ACADEMY,Al Jazeera Academy,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q4704132
AL JAZEERA MEDIA NETWORK,Al Jazeera Media Network,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4704134
AL JOMROK BOUTIQUE HOTEL,Al Jomrok Boutique Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968410
AL LIWAN SUITES,Al Liwan Suites,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855943
AL MADINA SUITES DOHA,Al Madina Suites Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997548
AL MANSOUR SUITES HOTEL,Al Mansour Suites Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997544
"AL MESSILA, A LUXURY COLLECTION RESORT & SPA, DOHA","Al Messila, a Luxury Collection Resort & Spa, Doha",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399824
AL MUNTAZAH PLAZA HOTEL,Al Muntazah Plaza Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967316
AL NAJADA BOUTIQUE HOTEL,Al Najada Boutique Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967941
AL NAJADA DOHA HOTEL BY TIVOLI,Al Najada Doha Hotel by Tivoli,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399855
AL SEEF HOTEL,Al Seef Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968071
AL SRAIYA HOLDING GROUP (QATAR),Al Sraiya Holding Group (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140352241
AL SULAITEEN AGRICULTURAL & INDUSTRIAL COMPLEX (QATAR),Al Sulaiteen Agricultural & Industrial Complex (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535201
AL SULTAN BEACH RESORT,Al Sultan Beach Resort,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855952
AL WAAB FARM,Al Waab Farm,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q94321135
AL-AHLI HOSPITAL,Al-Ahli Hospital,Health_Wellness,QA,,type_mapped,http://www.wikidata.org/entity/Q30260308
AL-AZHAR UNIVERSITY – DOHA,Al-Azhar University – Doha,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q4702248
AL-NAKHEEL HOTEL,Al-Nakheel Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968069
AL-SADD SUITES HOTEL,Al-Sadd Suites Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967627
AL-WATANIYA CONCRETE (QATAR),Al-Wataniya Concrete (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535203
"ALRAYYAN HOTEL DOHA, CURIO COLLECTION BY HILTON","AlRayyan Hotel Doha, Curio Collection by Hilton",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q78054939
"ALEPH DOHA RESIDENCES, CURIO COLLECTION BY HILTON","Aleph Doha Residences, Curio Collection by Hilton",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855906
ALWADI HOTEL DOHA - MGALLERY,Alwadi Hotel Doha - MGallery,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399850
AMERICAN SCHOOL OF DOHA,American School of Doha,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q4744937
"ANDAZ DOHA, BY HYATT","Andaz Doha, by Hyatt",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969529
ARAB INTERNATIONAL ACADEMY,Arab International Academy,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q51384436
ARUMAILA BOUTIQUE HOTEL,Arumaila Boutique Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967964
ASCOTT DOHA,Ascott Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967944
ASHGHAL,Ashghal,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q16250606
BANANA ISLAND RESORT DOHA BY ANANTARA,Banana Island Resort Doha by Anantara,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968284
BANYAN TREE DOHA AT LA CIGALE MUSHAIREB,Banyan Tree Doha At La Cigale Mushaireb,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855898
BARWA GROUP,Barwa Group,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6743378
BEST WESTERN PLUS DOHA,Best Western Plus Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967319
BLYTH ACADEMY QATAR,Blyth Academy Qatar,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q18346278
CEG INTERNATIONAL (QATAR),CEG International (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535242
CAMBRIDGE INTERNATIONAL SCHOOL FOR GIRLS,Cambridge International School for Girls,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q24965311
"CARNEGIE MELLON UNIVERSITY, QATAR","Carnegie Mellon University, Qatar",Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q890704
CENTARA WEST BAY HOTEL & RESIDENCES DOHA,Centara West Bay Hotel & Residences Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855910
CENTRO CAPITAL DOHA - BY ROTANA,Centro Capital Doha - by Rotana,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399829
CENTURY HOTEL,Century Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968086
CENTURY HOTEL DOHA,Century Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855941
CHAIRMEN HOTEL,Chairmen Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997550
CHEDI KATARA,Chedi Katara,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q125375116
CITY CENTRE ROTANA DOHA,City Centre Rotana Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399849
COMPASS INTERNATIONAL SCHOOL,Compass International School,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q5156093
CONCORDE HOTEL DOHA,Concorde Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399859
CONOCOPHILLIPS (QATAR),ConocoPhillips (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q30338326
CONSTRUCTION DEVELOPMENT (QATAR),Construction Development (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535315
COPTHORNE DOHA,Copthorne Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968244
CORP EXECUTIVE HOTEL - DOHA SUITES,Corp Executive Hotel - Doha Suites,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967251
CROWNE PLAZA DOHA - THE BUSINESS PARK,Crowne Plaza Doha - the Business Park,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399863
CROWNE PLAZA DOHA WEST BAY,Crowne Plaza Doha West Bay,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399847
CUBIC CORPORATION,Cubic Corporation,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5192235
"DPS-MODERN INDIAN SCHOOL, DOHA-QATAR","DPS-Modern Indian School, Doha-Qatar",Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q19458209
DAR AL SHARQ GROUP,Dar Al Sharq Group,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q114068738
DETENTE TECHNOLOGIES LLC,Detente Technologies LLC,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141964531
DOHA BANK,Doha Bank,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q73976396
DOHA BRITISH SCHOOL,Doha British School,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q5288534
DOHA COLLEGE,Doha College,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q5288535
DOHA FESTIVAL CITY,Doha Festival City,Shopping_Retail,QA,,type_mapped,http://www.wikidata.org/entity/Q39086360
DOHA MODERN INDIAN SCHOOL,Doha Modern Indian School,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q5288541
DOUBLETREE BY HILTON DOHA - AL SADD,DoubleTree by Hilton Doha - Al Sadd,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855892
DOUBLETREE BY HILTON DOHA CITY CENTRE,DoubleTree by Hilton Doha City Centre,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969494
DOUBLETREE BY HILTON DOHA OLD TOWN,DoubleTree by Hilton Doha Old Town,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399864
DUKHAN BANK,Dukhan Bank,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q64744409
DUKHAN ENGLISH SCHOOL,Dukhan English School,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q5313206
DUSIT DOHA HOTEL,Dusit Doha Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855902
EXXONMOBIL (QATAR),ExxonMobil (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535219
EZDAN HOTEL DOHA,Ezdan Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855896
"EZDAN HOTEL, RESIDENCES","Ezdan Hotel, Residences",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399831
"EZDAN HOTEL, WEST BAY","Ezdan Hotel, West Bay",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968543
EZDAN PALACE HOTEL,Ezdan Palace Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997533
FADAAT MEDIA,Fadaat Media,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q108541264
FOUR POINTS BY SHERATON DOHA,Four Points by Sheraton Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399838
FOUR SEASONS HOTEL DOHA,Four Seasons Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399856
FRASER SUITES DOHA,Fraser Suites Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399860
"FUWAIRIT KITE BEACH, TAPESTRY COLLECTION BY HILTON","Fuwairit Kite Beach, Tapestry Collection by Hilton",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969534
GENERAL ELECTRIC (QATAR),General Electric (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q30296008
GEORGE II HOTEL,George II Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967304
GERMAN INTERNATIONAL SCHOOL DOHA,German International School Doha,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q19904050
GLORIA HOTEL DOHA,Gloria Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967281
GOKULAM PARK DOHA,Gokulam Park Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968315
GOLDEN OCEAN HOTEL,Golden Ocean Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855933
GOLDEN TULIP DOHA HOTEL,Golden Tulip Doha Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855927
GRAND HYATT DOHA HOTEL & VILLAS,Grand Hyatt Doha Hotel & Villas,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399843
GRAND QATAR PALACE HOTEL,Grand Qatar Palace Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855908
GRAND REGAL HOTEL,Grand Regal Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855925
GULF DRILLING INTERNATIONAL,Gulf Drilling International,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q16841243
GULF ORGANIZATION FOR INDUSTRIAL CONSULTING,Gulf Organization for Industrial Consulting,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q17060381
GULF PARADISE HOTEL,Gulf Paradise Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967254
HALLIBURTON (QATAR),Halliburton (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535268
HAMAD BIN KHALIFA UNIVERSITY,Hamad Bin Khalifa University,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q24911975
HAMAD GENERAL HOSPITAL,Hamad General Hospital,Health_Wellness,QA,,type_mapped,http://www.wikidata.org/entity/Q30254334
HAMAD MEDICAL CORPORATION,Hamad Medical Corporation,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5643945
HAMPTON BY HILTON DOHA OLD TOWN,Hampton by Hilton Doha Old Town,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969508
HASSAD FOOD,Hassad Food,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q23759354
HILTON DOHA,Hilton Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399851
HILTON DOHA THE PEARL,Hilton Doha The Pearl,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q67913420
HILTON SALWA BEACH RESORT & VILLAS,Hilton Salwa Beach Resort & Villas,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969428
HOCHTIEF (QATAR),Hochtief (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535273
HOLIDAY INN - DOHA - THE BUSINESS PARK,Holiday Inn - Doha - the Business Park,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855938
HOLIDAY VILLA HOTEL AND RESIDENCE CITY CENTRE DOHA,Holiday Villa Hotel and Residence City Centre Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997543
HORIZON MANOR HOTEL,Horizon Manor Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855920
HYATT REGENCY ORYX DOHA,Hyatt Regency Oryx Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997553
IBQ,IBQ,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5969219
IKA SOUTH AMERICAN,IKA South American,Food_Dining,QA,,type_mapped,http://www.wikidata.org/entity/Q134988647
IBERDROLA (QATAR),Iberdrola (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535276
IBIS DOHA,Ibis Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969540
INFORMATICA QATAR (QATAR),Informatica Qatar (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535228
INFRASTRUCTURE RESEARCH & DEVELOPMENT (QATAR),Infrastructure Research & Development (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535258
INTERCONTINENTAL DOHA,InterContinental Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969690
INTERCONTINENTAL DOHA RESIDENCES,InterContinental Doha Residences,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968748
INTERCONTINENTAL DOHA THE CITY,InterContinental Doha the City,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399835
JW MARRIOTT MARQUIS CITY CENTER DOHA,JW Marriott Marquis City Center Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399848
JOURI A MURWAB HOTEL,Jouri A Murwab Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855935
KAHRAMAA,Kahramaa,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q3191905
"KATARA HILLS DOHA, LXR HOTELS & RESORTS","Katara Hills Doha, LXR Hotels & Resorts",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q140753887
KATARA HOSPITALITY,Katara Hospitality,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q19961640
"KEMPINSKI RESIDENCES & SUITES, DOHA","Kempinski Residences & Suites, Doha",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399842
KINGSGATE HOTEL DOHA,Kingsgate Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855916
LA CASTLE HOTEL,La Castle Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997538
LA CIGALE HOTEL,La Cigale Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967106
LA VILLA HOTEL,La Villa Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855918
LA VILLA INN HOTEL APARTMENTS,La Villa Inn Hotel Apartments,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967200
LA VILLA PALACE HOTEL,La Villa Palace Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855915
LAMAZANI,Lamazani,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q108747097
LANDMARK MALL,Landmark Mall,Shopping_Retail,QA,,type_mapped,http://www.wikidata.org/entity/Q17067835
LE MERIDIEN CITY CENTER,Le Meridien City Center,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969524
LE MIRAGE EXECUTIVE APARTMENT,Le Mirage Executive Apartment,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968388
LE MIRAGE SUITES,Le Mirage Suites,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968390
LE PARK HOTEL,Le Park Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997535
LE ROYAL MERIDIEN DOHA,Le Royal Meridien Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969510
LEVANTINE,Levantine,Food_Dining,QA,,type_mapped,http://www.wikidata.org/entity/Q82730398
LIBERTY SUITES DOHA,Liberty Suites Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967146
LIBRA TRADING COMPANY (QATAR),Libra Trading Company (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535270
LYCÉE FRANCO-QATARIEN VOLTAIRE,Lycée Franco-Qatarien Voltaire,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q21666072
M GRAND HOTEL DOHA,M Grand Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967371
M.E.S INDIAN SCHOOL,M.E.S Indian school,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q6712175
MODUS (QATAR),MODUS (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535304
MAERSK (QATAR),Maersk (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535597
MAGAZA (QATAR),Magaza (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535278
MALL OF QATAR,Mall of Qatar,Shopping_Retail,QA,,type_mapped,http://www.wikidata.org/entity/Q22948422
"MANDARIN ORIENTAL, DOHA","Mandarin Oriental, Doha",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855903
MARAFEQ (QATAR),Marafeq (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535280
MARRIOTT EXECUTIVE APARTMENTS CITY CENTER DOHA,Marriott Executive Apartments City Center Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997539
MARRIOTT MARQUIS CITY CENTER DOHA HOTEL,Marriott Marquis City Center Doha Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399840
"MARSA MALAZ KEMPINSKI, THE PEARL","Marsa Malaz Kempinski, the Pearl",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399865
MATHEMA PREMIUM APARTHOTEL,Mathema Premium Aparthotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855900
"MAYSAN DOHA, LXR HOTELS & RESORTS","Maysan Doha, LXR Hotels & Resorts",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q131471332
MERCURE GRAND HOTEL DOHA CITY CENTRE,Mercure Grand Hotel Doha City Centre,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399846
MERWEBHOTEL CENTRAL DOHA,Merwebhotel Central Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967203
MILLENNIUM CENTRAL DOHA,Millennium Central Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855931
MILLENNIUM HOTEL DOHA,Millennium Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399827
MILLENNIUM PLAZA DOHA,Millennium Plaza Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855893
MIRQAB MALL,Mirqab Mall,Shopping_Retail,QA,,type_mapped,http://www.wikidata.org/entity/Q116178634
MOEVENPICK HOTEL WEST BAY DOHA,Moevenpick Hotel West Bay Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967055
MONDRIAN DOHA,Mondrian Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399837
MUSHEIREB BOUTIQUE HOTEL,Musheireb Boutique Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967966
MÖVENPICK HOTEL DOHA,Mövenpick Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399862
MÖVENPICK HOTEL WEST BAY DOHA,Mövenpick Hotel West Bay Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399854
"NAJD BOUTIQUE HOTEL, DOHA","Najd Boutique Hotel, Doha",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967939
NAKILAT,Nakilat,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6960637
NATIONAL PLASTIC FACTORY STRETCH FILM MANUFACTURER QATAR,National Plastic Factory Stretch Film Manufacturer Qatar,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q109234491
NEWTON INTERNATIONAL SCHOOL,Newton International School,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q15262202
NORD ANGLIA INTERNATIONAL SCHOOL AL KHOR,Nord Anglia International School Al Khor,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q25045496
NORTHWESTERN UNIVERSITY IN QATAR,Northwestern University in Qatar,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q890759
OCCIDENTAL PETROLEUM (QATAR),Occidental Petroleum (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535289
OODLES WOK,Oodles Wok,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q138026441
ORYX AIRPORT HOTEL -TRANSIT ONLY,Oryx Airport Hotel -Transit Only,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997555
ORYX PUBLISHING AND ADVERTISING (QATAR),Oryx Publishing and Advertising (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535298
PAK SHAMA SCHOOL,Pak Shama School,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q7125377
PARK HOUSE ENGLISH SCHOOL,Park House English School,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q15265458
PARK HYATT DOHA,Park Hyatt Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855904
PHILIPPINE SCHOOL DOHA,Philippine School Doha,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q7185205
PLACE VENDÔME MALL,Place Vendôme Mall,Shopping_Retail,QA,,type_mapped,http://www.wikidata.org/entity/Q116055796
PLAZA INN DOHA,Plaza Inn Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855929
PREMIER INN DOHA AIRPORT,Premier Inn Doha Airport,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969214
PREMIER INN DOHA EDUCATION CITY HOTEL,Premier Inn Doha Education City Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968974
PROJECT RAVEN,Project Raven,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q136103981
PULLMAN DOHA BRIDGE TOWERS,Pullman Doha Bridge Towers,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968776
QNB GROUP,QNB Group,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1136759
QATAR ACADEMY,Qatar Academy,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q6825350
QATAR AMIRI FLIGHT,Qatar Amiri Flight,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q2812546
QATAR DISTRIBUTION COMPANY,Qatar Distribution Company,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q20858957
QATAR EXECUTIVE,Qatar Executive,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q7267100
QATAR FINANCE AND BUSINESS ACADEMY,Qatar Finance and Business Academy,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q7267102
QATAR FUEL,Qatar Fuel,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q56275016
QATAR INTERNATIONAL SCHOOL,Qatar International School,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q16910992
QATAR INVESTMENT AUTHORITY,Qatar Investment Authority,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1571175
QATAR ISLAMIC BANK,Qatar Islamic Bank,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q18346281
QATAR MINING (QATAR),Qatar Mining (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535321
QATAR ORTHOPAEDIC AND SPORTS MEDICINE HOSPITAL,Qatar Orthopaedic and Sports Medicine Hospital,Health_Wellness,QA,,type_mapped,http://www.wikidata.org/entity/Q30280517
QATAR SOLAR TECHNOLOGIES,Qatar Solar Technologies,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q124662533
QATAR SPORTS INVESTMENTS,Qatar Sports Investments,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q28221762
QATAR TURKISH SCHOOL,Qatar Turkish School,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q30692946
QATAR UNIVERSITY,Qatar University,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q1574578
QATARENERGY,QatarEnergy,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1811692
QATARGAS,Qatargas,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q973930
QNITED TRADING COMPANY,Qnited Trading Company,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140735750
QPROPERTIES,Qproperties,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q67570178
RABBAN SUITES WEST BAY DOHA,Rabban Suites West Bay Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399834
RADISSON BLU HOTEL DOHA,Radisson Blu Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399832
RAF PHARMACY,Raf Pharmacy,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q135987550
RAMADA ENCORE BY WYNDHAM DOHA,Ramada Encore by Wyndham Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q56070590
RAMADA BY WYNDHAM DOHA OLD TOWN,Ramada by Wyndham Doha Old Town,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969537
RASGAS,RasGas,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q3419764
RETAJ AL RAYYAN,Retaj Al Rayyan,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399853
RETAJ INN,Retaj Inn,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967838
RETAJ INN MARINA RESIDENCE,Retaj Inn Marina Residence,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969029
RETAJ RESIDENCE - AL CORNICH,Retaj Residence - Al Cornich,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967836
RETAJ RESIDENCE AL SADD,Retaj Residence Al Sadd,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967872
RETAJ ROYALE,Retaj Royale,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967870
RIXOS GULF HOTEL DOHA,Rixos Gulf Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967368
ROYAL QATAR HOTEL,Royal Qatar Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967303
SAFIR DOHA HOTEL,Safir Doha Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967256
SALAM INTERNATIONAL INVESTMENT LIMITED,Salam International Investment Limited,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7403519
SALFORD EDUCATIONAL CONSULTANCY,Salford Educational Consultancy,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141388520
SAPPHIRE PLAZA HOTEL,Sapphire Plaza Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855895
SARAY MUSHEIREB HOTEL,Saray Musheireb Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969096
SARAYA CORNICHE HOTEL,Saraya Corniche Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399857
SCHLUMBERGER (QATAR),Schlumberger (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535318
"SEALINE BEACH, A MURWAB RESORT","Sealine Beach, a Murwab Resort",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855954
SEDRA ARJAAN BY ROTANA,Sedra Arjaan by Rotana,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997551
SHARQ VILLAGE & SPA,Sharq Village & Spa,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115966974
SHELL (QATAR),Shell (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535328
SHERATON DOHA RESORT & CONVENTION HOTEL,Sheraton Doha Resort & Convention Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q7494677
SHERATON GRAND DOHA RESORT & CONV HOTEL,Sheraton Grand Doha Resort & Conv Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967366
SHERBORNE QATAR,Sherborne Qatar,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q22948379
SIDRA MEDICAL AND RESEARCH CENTER,Sidra Medical and Research Center,Health_Wellness,QA,,type_mapped,http://www.wikidata.org/entity/Q12242241
SIEMENS (QATAR),Siemens (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535330
SIMAISMA A MURWAB RESORT,Simaisma A Murwab Resort,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855947
SOHO COFFEE,Soho Coffee,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q135946153
SOMERSET AL MANSOURA DOHA,Somerset Al Mansoura Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969550
SOMERSET WEST BAY DOHA,Somerset West Bay Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115967206
SOUQ AL WAKRA HOTEL QATAR BY TIVOLI,Souq Al Wakra Hotel Qatar by Tivoli,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855949
SOUQ WAQIF BOUTIQUE HOTELS - TIVOLI,Souq Waqif Boutique Hotels - Tivoli,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997546
STAFFORD SRI LANKAN SCHOOL DOHA,Stafford Sri Lankan School Doha,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q28220532
STAYBRIDGE SUITES DOHA LUSAIL,Staybridge Suites Doha Lusail,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997541
STEIGENBERGER HOTEL DOHA,Steigenberger Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969487
STRATO HOTEL BY WARWICK,Strato Hotel by Warwick,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855945
SWISS-BELINN DOHA,Swiss-Belinn Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997536
TIME RAKO HOTEL DOHA,TIME Rako Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969031
TATA CONSULTING ENGINEERS (QATAR),Tata Consulting Engineers (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535337
TEXAS A&M UNIVERSITY AT QATAR,Texas A&M University at Qatar,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q1144951
"THE AVENUE, A MURWAB HOTEL","The Avenue, a Murwab Hotel",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855891
"THE CAMBRIDGE SCHOOL, DOHA, QATAR","The Cambridge School, Doha, Qatar",Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q7721067
THE CURVE HOTEL,The Curve Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855913
THE KITCHEN DOHA,The Kitchen Doha,Food_Dining,QA,,type_mapped,http://www.wikidata.org/entity/Q82692847
THE PEARL INTERNATIONAL HOSPITAL,The Pearl International Hospital,Health_Wellness,QA,,type_mapped,http://www.wikidata.org/entity/Q137765662
"THE PLAZA DOHA, LXR HOTELS & RESORTS","The Plaza Doha, LXR Hotels & Resorts",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q131465007
"THE RITZ-CARLTON, DOHA","The Ritz-Carlton, Doha",Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399852
THE ROYAL RIVIERA HOTEL DOHA,The Royal Riviera Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855923
THE ST. REGIS DOHA,The St. Regis Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399845
THE TORCH DOHA,The Torch Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399823
THE VYRA SUITES NH DOHA,The Vyra Suites Nh Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969440
THE WESTIN DOHA HOTEL & SPA,The Westin Doha Hotel & Spa,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399830
TIME RAKO HOTEL,Time Rako Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997556
TOTAL (QATAR),Total (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535339
UNIVERSITY OF DOHA FOR SCIENCE AND TECHNOLOGY,University of Doha for Science and Technology,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q30296037
VIP HOTEL,VIP Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111997552
VILLAGGIO MALL,Villaggio Mall,Shopping_Retail,QA,,type_mapped,http://www.wikidata.org/entity/Q7930800
VIRGINIA COMMONWEALTH UNIVERSITY - QATAR,Virginia Commonwealth University - Qatar,Housing_Education,QA,,type_mapped,http://www.wikidata.org/entity/Q24896812
VODAFONE QATAR,Vodafone Qatar,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q35587063
W DOHA,W Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399841
WALDORF ASTORIA DOHA LUSAIL,Waldorf Astoria Doha Lusail,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969512
WALDORF ASTORIA DOHA WEST BAY,Waldorf Astoria Doha West Bay,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q131302899
WARWICK DOHA HOTEL,Warwick Doha Hotel,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399828
WYNDHAM DOHA WEST BAY,Wyndham Doha West Bay,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399836
WYNDHAM GRAND DOHA WEST BAY BEACH,Wyndham Grand Doha West Bay Beach,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969531
WYNDHAM GRAND REGENCY DOHA,Wyndham Grand Regency Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111399825
ZUBARAH BOUTIQUE HOTEL DOHA,Zubarah Boutique Hotel Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968624
BEIN MEDIA GROUP,beIN Media Group,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q19650330
DUSITD2 SALWA DOHA,dusitD2 Salwa Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q111855899
DUSITDD2 SALWA DOHA,dusitdD2 Salwa Doha,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115969435
IHORIZONS (QATAR),iHorizons (Qatar),Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q59535282
MYHOLIDAYS,myholidays,Others,QA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q134971875
VOCO DOHA WEST BAY SUITES,voco Doha West Bay Suites,Travel,QA,,type_mapped,http://www.wikidata.org/entity/Q115968836
A. A. TURKI GROUP,A. A. Turki Group,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4647501
AIC TRADING,AIC Trading,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q134986707
ALDREES PETROLEUM AND TRANSPORT SERVICES COMPANY,ALDREES Petroleum and Transport Services Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4652322
ASACO,ASACO,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q4654027
AALI FOR RESIDENTAL UNITS,Aali For Residental Units,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458826
ABDULLA FOUAD GROUP OF COMPANIES,Abdulla Fouad Group of Companies,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q2821435
ABDULLAH ALOTHAIM MARKETS,Abdullah AlOthaim Markets,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12218555
ABRAJ KUDAI,Abraj Kudai,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q20020295
ADHAM GENERAL HOSPITAL,Adham General Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q140673813
AJLAN & BROTHERS,Ajlan & Brothers,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q16960538
AL AMAL HOSPITAL JEDDAH,Al Amal Hospital Jeddah,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30254309
AL ANWA AVIATION,Al Anwa Aviation,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q4703489
AL BAHA UNIVERSITY,Al Baha University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q4703529
AL BALAD DEVELOPMENT COMPANY,Al Balad Development Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q125243487
AL BILAD BANK,Al Bilad Bank,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4166498
AL FAISALIAH HOTEL,Al Faisaliah Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q56612542
AL FOZAN HOLDING,Al Fozan Holding,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q63171091
AL MADINAH HERITAGE,Al Madinah Heritage,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q134392896
AL MAHA AIRWAYS,Al Maha Airways,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q16127512
AL MAJED OUD,Al Majed Oud,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q131919659
AL MAWARID INTERNATIONAL SCHOOL,Al Mawarid International School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q23305652
AL MOAMMAR INFORMATION SYSTEMS CO.,Al Moammar Information Systems Co.,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q85873213
AL NOOR SPECIALIST HOSPITAL,Al Noor Specialist Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q16125077
AL RASHID MALL,Al Rashid Mall,Shopping_Retail,SA,,type_mapped,http://www.wikidata.org/entity/Q4704690
AL SAEDAN REAL ESTATE,Al Saedan Real Estate,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q109321400
AL SHOULA GROUP,Al Shoula Group,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4704810
AL WAFEER AIR,Al Wafeer Air,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q4704932
AL YUSR MIDDLE EAST,Al Yusr Middle East,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140035148
AL-AFAQ INTERNATIONAL SCHOOL,Al-Afaq International School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q24952236
AL-AFDAL AL-MASIYA FOR OPERATION AND MAINTENANCE,Al-Afdal Al-Masiya for Operation and Maintenance,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141623205
AL-BABTAIN POWER & TELECOM CO,Al-Babtain Power & Telecom Co,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12218580
AL-FALAH SCHOOL,Al-Falah School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q6854734
AL-LITH GENERAL HOSPITAL,Al-Lith General Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q140673868
AL-MADINAH COLLEGE OF TECHNOLOGY,Al-Madinah College of Technology,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q80675506
AL-THAGER MODEL SCHOOL,Al-Thager Model School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q4703288
AL-THAGHER GENERAL HOSPITAL,Al-Thagher General Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q140673696
AL-WAHA INTERNATIONAL SCHOOL,Al-Waha International School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q4703317
AL-YAMAMAH PRIVATE UNIVERSITY,Al-Yamamah Private University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q4703347
ALAT,Alat,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q124547892
ALAWWAL BANK,Alawwal Bank,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q2693351
ALBAIK,Albaik,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4703536
ALFAISAL UNIVERSITY,Alfaisal University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q4118882
ALHADAYA CENTER MARKET,Alhadaya Center Market,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q110827007
ALINMA BANK,Alinma Bank,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4120111
ALJAZEERA HOSPITAL,Aljazeera Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q50036463
ALKATHIRI HOLDING,Alkathiri Holding,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q42341471
ALLIANT CO.,Alliant Co.,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141697611
ALMARAI COMPANY,Almarai Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q3535226
ALMOOSA HEALTH GROUP,Almoosa Health Group,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q134514629
ALPHA STAR AVIATION,Alpha Star Aviation,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q20181105
ALRAJHI BANK,Alrajhi Bank,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1761176
ALSALAM AEROSPACE INDUSTRIES,Alsalam Aerospace Industries,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7188614
ALSANIDI CAMPING,Alsanidi Camping,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q108941439
ALSHHBAA COPPERWARE,Alshhbaa Copperware,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141521866
AMERICAN INTERNATIONAL SCHOOL OF JEDDAH,American International School of Jeddah,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q19881923
AMERICAN INTERNATIONAL SCHOOL OF YANBU,American International School of Yanbu,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q137774661
AMERICAN INTERNATIONAL SCHOOL – RIYADH,American International School – Riyadh,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q4744195
AMERICAN SCHOOL DHAHRAN,American School Dhahran,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q108559397
AMLAKIRE,Amlakire,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141572692
ANDALUSIA GROUP,Andalusia group,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q113290059
ARAB NATIONAL BANK,Arab National Bank,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4783214
ARAB OPEN UNIVERSITY SAUDI ARABIA,Arab Open University Saudi Arabia,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q104670131
ARAB SATELLITE COMMUNICATIONS ORGANIZATION,Arab Satellite Communications Organization,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q624426
ARABIAN OUD,Arabian Oud,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q28714640
ARABIAN STANDARD OIL COMPANY,Arabian Standard Oil Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q62735331
ARKAN BY ASWA DEVELOPMENT COMPANY,Arkan By Aswa Development Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5221859
ARMED FORCES HOSPITAL,Armed Forces Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30254314
ASIR CENTRAL HOSPITAL,Asir Central Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30279834
ATLANTIS JEDDAH,Atlantis Jeddah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q136785337
AVILEASE,AviLease,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q112820282
AVIONS SUPERINTELLIGENCE LAB,Avions Superintelligence Lab,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141807544
BAFARAT INDUSTRIAL GROUP,Bafarat Industrial Group,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q134619827
"BANGLADESH INTERNATIONAL SCHOOL, DAMMAM","Bangladesh International School, Dammam",Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q4855317
"BANGLADESH INTERNATIONAL SCHOOL, ENGLISH SECTION, RIYADH","Bangladesh International School, English Section, Riyadh",Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q4855318
BANK ALJAZIRA,Bank Aljazira,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12199341
BANQUE SAUDI FRANSI,Banque Saudi Fransi,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7181252
BANYAN TREE ALULA,Banyan Tree AlUla,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q116938704
BARN'S,Barn's,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q121072061
BASMTAK,Basmtak,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141776006
BATOOK CHEWING GUM INDUSTRIES,Batook Chewing Gum Industries,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q129810151
BAYANAT LABS,Bayanat Labs,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141925151
BILYTICA,Bilytica,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141959521
BIONIXUS,BioNixus,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140188264
BODY MASTERS,Body Masters,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q105713910
"BRITISH INTERNATIONAL SCHOOL, RIYADH","British International School, Riyadh",Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q15204893
BUGSHAN HOSPITAL,Bugshan Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30293449
BUPA ARABIA,Bupa Arabia,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q17005768
CATRION,CATRION,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q54870514
CHUBB ARABIA COOPERATIVE INSURANCE CO.,CHUBB Arabia Cooperative Insurance Co.,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q89837399
CAPITAL O 162 BRZEEN HOTEL,Capital O 162 Brzeen Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067837
CAPITAL O 296 JEDDAH OASIS HOTEL,Capital O 296 Jeddah Oasis Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067400
CAPITAL O 338 ASIAN HOTEL,Capital O 338 Asian Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111064614
CAPITAL O 419 AL SAFEER HOTEL,Capital O 419 Al Safeer Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067838
CAPITAL O 461 MENA PLAZA TAIF,Capital O 461 Mena Plaza Taif,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111073867
CAPITAL O 549 THE BLUE ROSE HOTEL,Capital O 549 The Blue Rose Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458812
CAPITAL O 581 GOLDISH HOTEL,Capital O 581 Goldish Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458824
CAPITAL O 596 GARDEN PALACE HOTEL,Capital O 596 Garden Palace Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458815
CHEMANOL,Chemanol,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12236791
CIVIL AND ELECTRICAL PROJECTS CONTRACTING COMPANY,Civil and Electrical Projects Contracting Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5124637
COLLEGE PREPARATORY CENTER,College Preparatory Center,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q5146524
COLLEGE OF BUSINESS ADMINISTRATION,College of Business Administration,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q5146656
COLLEGE OF DENTISTRY UNIVERSITY OF DAMMAM,College of Dentistry University of Dammam,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q5146675
COLLEGE OF FOOD AND ENVIRONMENT TECHNOLOGY IN BURAYDAH,College of Food and Environment Technology in Buraydah,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q5146719
CONRAD JABAL OMAR MAKKAH,Conrad Jabal Omar Makkah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q30090585
CONRAD RIYADH LAYSEN VALLEY,Conrad Riyadh Laysen Valley,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q142067821
CONSUMER PROTECTION ASSOCIATION,Consumer Protection Association,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q136321795
COPIVO,Copivo,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140073504
CORE COFFEE & ROASTERY,Core Coffee & Roastery,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q113506053
CROWNE PLAZA RIYADH PALACE,Crowne Plaza Riyadh Palace,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q122291341
DPS JEDDAH AL-FALAH INTERNATIONAL SCHOOL,DPS Jeddah Al-Falah International School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q5205962
DALLAH AL-BARAKA,Dallah Al-Baraka,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1157969
DAMMAM CENTRAL HOSPITAL,Dammam Central Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q12242606
DAMMAM COLLEGE OF TECHNOLOGY,Dammam College of Technology,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q83593932
DAR AL SHIFA HOSPITAL,Dar Al Shifa Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q123448908
DAR AL ULOOM UNIVERSITY,Dar Al Uloom University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q12204482
DAR AL-HANDASAH CONSULTANTS SHAIR & PARTNERS COMPANY (SAUDI ARABIA),Dar Al-Handasah Consultants Shair & Partners Company (Saudi Arabia),Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141668823
DAR AL-HEKMA UNIVERSITY,Dar Al-Hekma University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q5221862
DAR AL-ULOOM COLLEGES,Dar Al-Uloom Colleges,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q5221861
DELTA INTERNATIONAL SCHOOL,Delta International School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q5254669
DERAAH,Deraah,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q130044578
DESIGN ZONE,Design Zone,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140518385
DETTAGLIOAUTO,Dettaglioauto,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141708915
DHAHRAN AHLIYYAH SCHOOL,Dhahran Ahliyyah School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q5268695
DIALA FURNISHED APARTMENTS,Diala Furnished Apartments,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458629
"DIYAR AJWA, TAPESTRY COLLECTION BY HILTON","Diyar Ajwa, Tapestry Collection by Hilton",Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q141818046
DLIGHT,Dlight,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140010370
DOMIRA CONTRACTING AND REAL ESTATE DEVELOPMENT,Domira Contracting and Real Estate Development,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141574846
DOUBLETREE BY HILTON HOTEL DHAHRAN,DoubleTree by Hilton Hotel Dhahran,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q30276144
DOUBLETREE BY HILTON JABAL OMAR MAKKAH,DoubleTree by Hilton Jabal Omar Makkah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q140770516
DOUBLETREE BY HILTON JEDDAH AL ANDALUS MALL,DoubleTree by Hilton Jeddah Al Andalus Mall,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q138862814
DOUBLETREE BY HILTON MAKKAH AZIZIYAH,DoubleTree by Hilton Makkah Aziziyah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q139831615
DOUBLETREE BY HILTON RIYADH - AL MUROJ BUSINESS GATE,DoubleTree by Hilton Riyadh - Al Muroj Business Gate,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q115794856
DUSSUR,Dussur,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q54869935
E. A. JUFFALI AND BROTHERS,E. A. Juffali and Brothers,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5321696
EVEU COSMETIC,EVEU Cosmetic,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139414250
EAST JEDDAH HOSPITAL,East Jeddah Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q140615623
EFFAT UNIVERSITY,Effat University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q5347215
EFIGENCE,Efigence,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140916601
EJAZ ELECTRONIC PUBLISHING COMPANY,Ejaz Electronic Publishing Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q106036194
EKUEP,Ekuep,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141645525
EMAAR THE ECONOMIC CITY,Emaar The Economic City,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12182356
EXTEND,Extend,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141668979
FAIRER UNIVERSITY,FAiRER University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q141169080
FAHD BIN SULTAN UNIVERSITY,Fahd Bin Sultan University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q5429530
FILM ALULA,Film AlUla,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q125497300
FINA,Fina,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141551847
FIRST CITY FOR INFORMATION TECHNOLOGY,First City for Information Technology,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q131470883
FITNESSTIME,FitnessTime,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q105710068
FOGALQRN,FogAlqrn,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140247409
FOUR SEASONS HOTEL RIYADH,Four Seasons Hotel Riyadh,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q22930253
GARDEN PLAZA HOTEL,Garden Plaza Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111117489
GERMAN INTERNATIONAL SCHOOL JEDDAH,German International School Jeddah,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q19891560
GERMAN INTERNATIONAL SCHOOL RIYADH,German International School Riyadh,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q19904052
GRANADA CENTER,Granada Center,Shopping_Retail,SA,,type_mapped,http://www.wikidata.org/entity/Q5594094
GRAND HYATT AL KHOBAR HOTEL AND RESIDENCES,Grand Hyatt Al Khobar Hotel and Residences,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q136035841
GRAND HYATT THE RED SEA,Grand Hyatt The Red Sea,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q136503740
GUESTREADY,GuestReady,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q63985151
HSBC SAUDI ARABIA,HSBC Saudi Arabia,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5635879
HA'IL UNIVERSITY,Ha'il University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q12204479
HAIL CEMENT COMANY,Hail Cement Comany,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q20403120
HALACARLY,HalaCarly,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140129305
HALF MILLION,Half Million,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q108537438
HAMPTON BY HILTON JEDDAH SOUQ7,Hampton by Hilton Jeddah Souq7,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q141555938
HAMPTON BY HILTON SHARMA,Hampton by Hilton Sharma,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q130722977
HERA GENERAL HOSPITAL,Hera General Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30279864
HERFY,Herfy,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q5738371
HEXTURE,Hexture,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141687190
HILTON AL KHOBAR KING FAHD CAUSEWAY,Hilton Al Khobar King Fahd Causeway,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q131470854
HILTON GARDEN INN AL KHOBAR KING FAHD CAUSEWAY,Hilton Garden Inn Al Khobar King Fahd Causeway,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q138720459
HILTON GARDEN INN RIYADH OLAYA,Hilton Garden Inn Riyadh Olaya,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q75971164
HILTON GARDEN INN TABUK,Hilton Garden Inn Tabuk,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q139592498
HILTON HOTEL & CONVENTION JABAL OMAR MAKKAH,Hilton Hotel & Convention Jabal Omar Makkah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q66586875
HILTON RIYADH HOTEL & RESIDENCES,Hilton Riyadh Hotel & Residences,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q76513709
HILTON RIYADH OLAYA,Hilton Riyadh Olaya,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q141045229
HILTON SUITES JABAL OMAR MAKKAH,Hilton Suites Jabal Omar Makkah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q91607548
HUNGRY BUNNY,Hungry bunny,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q81533483
HUSSEIN AL-ALI HOSPITAL,Hussein Al-Ali Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q22949094
HYATT HOUSE JEDDAH SARI STREET,Hyatt House Jeddah Sari Street,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q136186018
HYATT PLACE RIYADH AL SULAIMANIA,Hyatt Place Riyadh Al Sulaimania,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q136308947
HYATT REGENCY RIYADH OLAYA,Hyatt Regency Riyadh Olaya,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q136466874
HYUNDAI MOTOR MANUFACTURING MIDDLE EAST,Hyundai Motor Manufacturing Middle East,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q134503180
ISG DAMMAM,ISG Dammam,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q5973885
IMAM ABDULRAHMAN AL FAISAL HOSPITAL,Imam Abdulrahman Al Faisal Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q50036708
IMAM ABDULRAHMAN BIN FAISAL UNIVERSITY,Imam Abdulrahman Bin Faisal University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7895319
IMAM MOHAMMAD IBN SAUD ISLAMIC UNIVERSITY AL MALAZ CAMPUS,Imam Mohammad Ibn Saud Islamic University Al Malaz Campus,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q108084720
IMAM MOHAMMAD IBN SAUD ISLAMIC UNIVERSITY AL NAFAL CAMPUS,Imam Mohammad Ibn Saud Islamic University Al Nafal Campus,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q108899083
INTEGRATED TELECOM COMPANY,Integrated Telecom Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q16965386
INTERNATIONAL INDIAN SCHOOL JEDDAH,International Indian School Jeddah,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q6051062
"INTERNATIONAL INDIAN SCHOOL, AL-JUBAIL","International Indian School, Al-Jubail",Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q6051052
"INTERNATIONAL INDIAN SCHOOL, DAMMAM","International Indian School, Dammam",Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q6051055
"INTERNATIONAL INDIAN SCHOOL, RIYADH","International Indian School, Riyadh",Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q6051058
INTERNATIONAL ISLAMIC TRADE FINANCE CORPORATION,International Islamic Trade Finance Corporation,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6051229
INTERNATIONAL MEDICAL CENTER,International Medical Center,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q4119998
INTERNATIONAL PHILIPPINE SCHOOL IN AL KHOBAR,International Philippine School in Al Khobar,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q15228754
INTERNATIONAL PHILIPPINE SCHOOL IN JEDDAH,International Philippine School in Jeddah,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q21666077
IRQAH HOSPITAL,Irqah Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q12242648
ISLAMIC DEVELOPMENT BANK,Islamic Development Bank,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q41230
ISNAAD,Isnaad,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141007216
JABAL OMAR HYATT REGENCY MAKKAH,Jabal Omar Hyatt Regency Makkah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q136463430
JAVA TIME,Java Time,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12204153
JAZAN UNIVERSITY,Jazan University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q6168054
JEDDAH HILTON,Jeddah Hilton,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q6172690
JEDDAH INTERNATIONAL SCHOOL,Jeddah International School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q6172692
JOHNS HOPKINS ARAMCO HEALTHCARE,Johns Hopkins Aramco Healthcare,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q7427119
JOUF UNIVERSITY,Jouf University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q12204417
JUBAIL TECHNICAL INSTITUTE,Jubail Technical Institute,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q6301702
JĀMIʻAT AL-MALIK KHĀLID,Jāmiʻat al-Malik Khālid,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q20411175
KAYALA AIRLINE,Kayala Airline,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q476681
KING ABDUL AZIZ UNIVERSITY HOSPITAL,King Abdul Aziz University Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30254018
KING ABDULAZIZ HOSPITAL,King Abdulaziz Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30280400
KING ABDULAZIZ MEDICAL CITY,King Abdulaziz Medical City,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q6411203
KING ABDULAZIZ UNIVERSITY,King Abdulaziz University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q1795928
KING ABDULLAH BIN ABDULAZIZ UNIVERSITY HOSPITAL,King Abdullah Bin Abdulaziz University Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q101004450
KING ABDULLAH CITY FOR FEMALE STUDENTS,King Abdullah City for Female Students,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q108919788
KING ABDULLAH MEDICAL CITY,King Abdullah Medical City,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q20423944
KING FAHAD CENTRAL HOSPITAL,King Fahad Central Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q28714524
KING FAHAD HOSPITAL HUFŪF,King Fahad Hospital Hufūf,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30280420
KING FAHAD HOSPITAL JEDDAH,King Fahad Hospital Jeddah,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q12242650
KING FAHAD MEDICAL CITY,King Fahad Medical City,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q6411562
KING FAHAD SPECIALIST HOSPITAL DAMMAM,King Fahad Specialist Hospital Dammam,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q15238519
KING FAHD ARMED FORCES HOSPITAL,King Fahd Armed Forces Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q20424834
KING FAHD UNIVERSITY HOSPITAL,King Fahd University Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q6411563
KING FAHD UNIVERSITY OF PETROLEUM AND MINERALS,King Fahd University of Petroleum and Minerals,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q4116241
KING FAISAL SPECIALIST HOSPITAL AND RESEARCH CENTRE,King Faisal Specialist Hospital and Research Centre,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q6856599
KING FAISAL UNIVERSITY,King Faisal University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q3070702
KING KHALED EYE SPECIALIST HOSPITAL,King Khaled Eye Specialist Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30280432
KING KHALED HOSPITAL,King Khaled Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q28717263
KING KHALED HOSPITAL (ALKHARJ),King Khaled Hospital (AlKharj),Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q61954934
KING KHALID UNIVERSITY,King Khalid University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q6411791
KING KHALID UNIVERSITY HOSPITAL,King Khalid University Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30260367
KING SAUD MEDICAL COMPLEX,King Saud Medical Complex,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q6412025
KING SAUD UNIVERSITY,King Saud University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q1752043
KING SAUD UNIVERSITY COLLEGE OF MEDICINE,King Saud University College of Medicine,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q17067747
KINGDIM HOSPITAL,Kingdim hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30080948
KINGDOM HOLDING COMPANY,Kingdom Holding Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1742118
"KNOWLEDGE ECONOMIC CITY, MEDINA","Knowledge Economic City, Medina",Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6423290
KNOWLEDGE INTERNATIONAL UNIVERSITY,Knowledge International University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q107919929
LAZARD,Lazard,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q637440
LUXURY LAND,Luxury Land,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139567555
MAGRABI,MAGRABi,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q129485375
MBC GROUP,MBC Group,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1543823
"MBS COLLEGE FOR CYBERSECURITY, ARTIFICIAL INTELLIGENCE AND ADVANCED TECHNOLOGIES","MBS College for Cybersecurity, Artificial Intelligence and Advanced Technologies",Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q110442613
MEED TRADING COMPANY,MEED Trading Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q105492269
MAADEN,Maaden,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6721006
MADRASAH AS-SAWLATIYA,Madrasah as-Sawlatiya,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q6728559
MADRASSA RAHMANIA,Madrassa Rahmania,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q63123045
MAESTRO PIZZA,Maestro Pizza,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q121133743
MAHFOOZ AVIATION,Mahfooz Aviation,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q952370
MAJMAAH UNIVERSITY,Majmaah University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q6737968
MAKKAH MILLENNIUM HOTEL,Makkah Millennium Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q28456180
MALL OF ARABIA,Mall of Arabia,Shopping_Retail,SA,,type_mapped,http://www.wikidata.org/entity/Q6743988
MANARAT AL-QASSIM SCHOOL,Manarat Al-Qassim School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q6746952
MANARAT JEDDAH INTERNATIONAL SCHOOL,Manarat Jeddah International School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q55621965
MANTIQI,Mantiqi,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139920260
MATERNITY AND CHILDREN'S HOSPITAL,Maternity and Children's Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30280922
MINISTRY OF NATIONAL GUARD HEALTH AFFAIRS,Ministry of National Guard Health Affairs,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q14956772
MIRAVAL THE RED SEA,Miraval The Red Sea,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q132346337
MOBILY,Mobily,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6887331
MOZN,Mozn,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q119443682
MUHRAQ INSTITUTION FOR STUDENT SERVICES,Muhraq Institution for Student Services,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q136485856
MUMTALAKAT,Mumtalakat,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141900533
MUSTAQBAL UNIVERSITY,Mustaqbal University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q12235841
NEOM GREEN HYDROGEN COMPANY,NEOM Green Hydrogen Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q115195518
NEOM INVESTMENT FUND,NEOM Investment Fund,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q125116344
NADEC,Nadec,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12188937
NAFT COMPANY,Naft Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q105572509
NAHDI MEDICAL COMPANY,Nahdi Medical Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q98582564
NAJD NATIONAL SCHOOLS,Najd National Schools,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q6959941
NAJRAN UNIVERSITY,Najran University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q2913037
NAMA CHEMICALS,Nama Chemicals,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q6961181
NAS-AIR CHARTER,Nas-Air Charter,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q113551237
NASEEJ,Naseej,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12194420
NATIONAL AIR SERVICE,National Air Service,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q1433218
NATIONAL LIGHTING COMPANY,National Lighting Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140032353
NATIONAL SHIPPING COMPANY OF SAUDI ARABIA,National Shipping Company of Saudi Arabia,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12188930
NESMA AIRLINES,Nesma Airlines,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q1572717
"NEW MIDDLE EAST INTERNATIONAL SCHOOL, RIYADH","New Middle East International School, Riyadh",Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7010360
NOBLES INTERNATIONAL SCHOOL,Nobles International School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q48732757
NORTH WEST ARMED FORCES HOSPITAL,North West Armed Forces Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30280907
NORTHERN AREA ARMED FORCES HOSPITAL,Northern Area Armed Forces Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q50037234
NORTHERN BORDERS UNIVERSITY,Northern Borders University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7058167
OSN,OSN,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4118549
OYO 105 TRAINING TEST SAUDI,OYO 105 Training Test Saudi,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458821
OYO 167 DAR AL RAIES HOTEL,OYO 167 Dar Al Raies Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111052724
OYO 176 HOTEL SAFARI AL HADA,OYO 176 Hotel Safari Al Hada,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111073866
OYO 197 SAFWAT ALBAYT,OYO 197 Safwat Albayt,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111052732
OYO 212 ZAHRAT AL JAL,OYO 212 Zahrat Al Jal,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111073865
OYO 234 HAYAT AL SALAM HOTEL APARTMENT,OYO 234 Hayat Al Salam Hotel Apartment,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111054342
OYO 236 AL WETHENANI APARTMENT,OYO 236 Al Wethenani Apartment,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111073864
OYO 242 AL AHLAM RESORT AL LEITH,OYO 242 Al Ahlam Resort Al Leith,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067404
OYO 246 HOTEL HADEEL AL MOTAMAYEZAH,OYO 246 Hotel Hadeel Al Motamayezah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067405
OYO 273 STAR YANBU HOTEL SUITES,OYO 273 Star Yanbu Hotel Suites,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111054340
OYO 279 AL JAWAHARA,OYO 279 Al Jawahara,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111073863
OYO 288 DIAFATI RESIDENTIAL UNITS,OYO 288 Diafati Residential Units,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067433
OYO 301 ASFRINE HOTEL APARTMENT,OYO 301 Asfrine Hotel Apartment,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111054343
OYO 302 MAAMOURA,OYO 302 Maamoura,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067836
OYO 315 RAMZ ABHA HOTEL,OYO 315 Ramz Abha Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067584
OYO 324 GREEN HOUSE HOTEL ABHA,OYO 324 Green House Hotel Abha,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067576
OYO 333 DHEYOF AL WATTAN FOR HOTEL SUITES,OYO 333 Dheyof Al Wattan For Hotel Suites,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067985
OYO 344 ALMIBKHARA ALTHAHBIA,OYO 344 Almibkhara Althahbia,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067409
OYO 350 DAR ALMADINAH,OYO 350 Dar Almadinah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067406
OYO 357 BLUE DIAMOND HOTEL,OYO 357 Blue Diamond Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111053086
OYO 369 ARWA ALQOSOR,OYO 369 Arwa Alqosor,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067579
OYO 372 NAWAZI WATHEER HOTEL,OYO 372 Nawazi Watheer Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111052727
OYO 373 DEYAR AL RASHED HOTEL APARTMENTS,OYO 373 Deyar Al Rashed Hotel Apartments,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111052728
OYO 375 DEYAR ALRAWADA HOTEL,OYO 375 Deyar Alrawada Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111052731
OYO 384 ZUMORDAT TAHA,OYO 384 Zumordat Taha,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458515
OYO 385 QAMAR RESIDENTIAL UNITS,OYO 385 Qamar Residential Units,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458516
OYO 386 BUHR,OYO 386 Buhr,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111071610
OYO 388 AL DANA AL KHALIJIA,OYO 388 Al Dana Al khalijia,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067429
OYO 389 DIAR RAWSHAN,OYO 389 Diar Rawshan,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111071611
OYO 391 ASDAF AL JUBAIL FURNISHED APARTMENTS,OYO 391 Asdaf Al Jubail Furnished Apartments,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111064615
OYO 393 SHOROF ABHA,OYO 393 Shorof Abha,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067578
OYO 395 AL HAFOF HOTEL,OYO 395 Al Hafof Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067407
OYO 396 ALAM AL SALA AL KOBRA TOWERS,OYO 396 Alam Al Sala Al Kobra Towers,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067408
OYO 401 AL ZAIDAN FOR FURNISHED UNITS,OYO 401 Al Zaidan For Furnished Units,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067986
OYO 402 JAWHRAT ASFARI HOTEL,OYO 402 Jawhrat Asfari Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067432
OYO 403 HIDAYA TOWERS HOTEL,OYO 403 Hidaya Towers Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111052726
OYO 405 NUJOM AL-JAZERAH,OYO 405 Nujom Al-jazerah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111054341
OYO 411 MOON HOTEL,OYO 411 Moon Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111071613
OYO 416 BONAIS HOTEL,OYO 416 Bonais Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111054339
OYO 418 HOTEL MANAZIL AL HOUR 2,OYO 418 Hotel Manazil Al Hour 2,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111052725
OYO 421 HYATT JUBAIL HOTEL,OYO 421 Hyatt Jubail Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111052729
OYO 422 BARAKAT TIBA2,OYO 422 Barakat Tiba2,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111053078
OYO 423 REHAB AL MARWA HOTEL 3,OYO 423 Rehab Al Marwa Hotel 3,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458517
OYO 424 REHAB AL MARWA HOTEL 2,OYO 424 Rehab Al Marwa Hotel 2,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458518
OYO 425 HOTEL MANAZIL ALFOUZ,OYO 425 Hotel Manazil Alfouz,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458519
OYO 426 ROYAL AL KHALEEJ FURNISHED APARTMENTS,OYO 426 Royal Al Khaleej Furnished Apartments,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111071614
OYO 427 NUJOOM AL SHARQIA 2,OYO 427 Nujoom Al Sharqia 2,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111071609
OYO 429 HAMSAT TAIBA HOTEL,OYO 429 Hamsat Taiba Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458553
OYO 430 AL JAWAD UNITS,OYO 430 Al Jawad Units,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111053079
OYO 431 MARINA TAIBA HOTEL,OYO 431 Marina Taiba Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111053080
OYO 434 ABDULHAMEED SHAFI,OYO 434 Abdulhameed Shafi,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458523
OYO 439 DORAT AL BELAAD,OYO 439 Dorat Al Belaad,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458524
OYO 441 AL FALAH AL RAQI,OYO 441 Al Falah Al Raqi,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458520
OYO 442 NELIOFIR AL RAED APARTMENTS UNITS,OYO 442 Neliofir Al Raed Apartments Units,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458816
OYO 445 AJYAD BAKKAK HOTEL,OYO 445 Ajyad Bakkak Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458521
OYO 447 RETAJ AL FEDY UNITS,OYO 447 Retaj Al Fedy Units,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111053081
OYO 448 ESKAN 8 HOTEL,OYO 448 Eskan 8 Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458525
OYO 449 LULUAT BAKKAK,OYO 449 Luluat Bakkak,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458526
OYO 450 MAWASIM AJYAD AL SUDD,OYO 450 Mawasim Ajyad Al Sudd,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458522
OYO 451 ESKAN 5 HOTEL,OYO 451 Eskan 5 Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458527
OYO 452 ESKAN 7 HOTEL,OYO 452 Eskan 7 Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458528
OYO 457 DIAFATI 2,OYO 457 Diafati 2,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067434
OYO 459 BARKAT TAIBA 1,OYO 459 Barkat Taiba 1,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458554
OYO 463 MAWADA ALAZIZIYA,OYO 463 Mawada Alaziziya,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458555
OYO 465 MANAZIL AL HOUR 1,OYO 465 Manazil Al Hour 1,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458529
OYO 466 WARDAT AL MASHAER HOTEL,OYO 466 Wardat Al Mashaer Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458530
OYO 467 AL DAHYA HOTEL,OYO 467 Al Dahya Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067577
OYO 473 RASIYAT AL SAFA HOTEL,OYO 473 Rasiyat Al Safa Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458531
OYO 474 ALYOUSR ROYAL HOTEL,OYO 474 Alyousr Royal Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458532
OYO 475 AL RAFIDIEN ALMASI HOTEL,OYO 475 Al Rafidien Almasi Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458533
OYO 476 HOTEL BAKKAH AL SALAH,OYO 476 Hotel Bakkah Al Salah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458534
OYO 477 MANAR AL EIMAN,OYO 477 Manar Al Eiman,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458535
OYO 478 DORAT AL TAQWA HOTEL,OYO 478 Dorat Al Taqwa Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458536
OYO 479 JAWHART AL TAQWA HOTEL,OYO 479 Jawhart Al Taqwa Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458537
OYO 484 AHLA MASAA 1,OYO 484 Ahla Masaa 1,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458628
OYO 486 WAQF AL JEHANI AL AZIZIYAH,OYO 486 Waqf Al Jehani Al Aziziyah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458538
OYO 487 WAQF AL JEHANI SHISHA,OYO 487 Waqf Al Jehani Shisha,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458539
OYO 492 ROSE PLAZA FOR HOUSING UNITS,OYO 492 Rose Plaza For Housing Units,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067581
OYO 493 JAWHART KUDAI HOTEL,OYO 493 Jawhart Kudai Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458540
OYO 494 SAMA AJYAD HOTEL,OYO 494 Sama Ajyad Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458541
OYO 495 DURAT AL EWA,OYO 495 Durat Al Ewa,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458542
OYO 498 AL RASHDOON HOTEL,OYO 498 Al Rashdoon Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458543
OYO 501 ROSE AL MUZEN HOTEL,OYO 501 Rose Al Muzen Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458544
OYO 502 SANAM HOTEL SUITES - RIYADH,OYO 502 Sanam Hotel Suites - Riyadh,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458834
OYO 506 ESKAN 9 HOTEL,OYO 506 Eskan 9 Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458545
OYO 507 ASHBILIA SUITES,OYO 507 Ashbilia Suites,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458823
OYO 508 MARASI AL HASHMYA,OYO 508 Marasi Al Hashmya,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458546
OYO 509 MANART AL MUNA,OYO 509 Manart Al Muna,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458547
OYO 515 JEWAR AL MEDINA HOTEL,OYO 515 Jewar Al Medina Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458556
OYO 516 AL MEDINA SAKANI HOTEL,OYO 516 Al Medina Sakani Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111053085
OYO 519 RANAN HOTEL APARTMENTS,OYO 519 Ranan Hotel Apartments,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458562
OYO 524 ZAHRAT ALWAZIRIYA FURNISHED APARTMENTS,OYO 524 Zahrat Alwaziriya Furnished Apartments,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458817
OYO 525 ROSE PLAZA1,OYO 525 Rose Plaza1,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067574
OYO 526 SADEEM ABBA,OYO 526 Sadeem Abba,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067582
OYO 528 MASAYA FURNISHED APARTMENTS,OYO 528 Masaya Furnished Apartments,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067430
OYO 529 MASAYA FURNISHED APARTMENTS 2,OYO 529 Masaya Furnished Apartments 2,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458822
OYO 531 ESKAN4 HOTEL,OYO 531 Eskan4 Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458548
OYO 532 SHOAA AL SHAAB,OYO 532 Shoaa Al Shaab,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458549
OYO 533 ESKAN6 HOTEL,OYO 533 Eskan6 Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458550
OYO 534 ASSILAH HOTEL,OYO 534 Assilah Hotel,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111053083
OYO 535 ZOHRAT AL SALAH,OYO 535 Zohrat Al Salah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458551
OYO 537 DAHTHAM FURNISHED UNITS,OYO 537 Dahtham Furnished Units,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067583
OYO 540 ABHA ALSHOGAG,OYO 540 Abha Alshogag,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067580
OYO 542 ADWA'A AL WADI,OYO 542 Adwa'a Al Wadi,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111073868
OYO 545 GOLDEN GALAXIES FURNISHED UNITS,OYO 545 Golden Galaxies Furnished Units,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111073610
OYO 553 ARQA AL QOSOR,OYO 553 Arqa Al Qosor,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067401
OYO 559 AL EAIRY APARTMENT TAIF,OYO 559 Al Eairy Apartment Taif,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458995
OYO 560 AL EAIRY APARTMENT DAMMAM 4,OYO 560 Al Eairy Apartment Dammam 4,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111071615
OYO 562 AL EAIRY APARTMENT RIYADH 3,OYO 562 Al Eairy Apartment Riyadh 3,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458835
OYO 563 AL EAIRY APARTMENT JEDDAH 6,OYO 563 Al Eairy Apartment Jeddah 6,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067410
OYO 564 AL EAIRY FURNISHED SUITS 4,OYO 564 Al Eairy Furnished Suits 4,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458818
OYO 565 AL EAIRY APARTMENT TABUK 6,OYO 565 Al Eairy Apartment Tabuk 6,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458563
OYO 566 AL EAIRY APARTMENT TABUK 5,OYO 566 Al Eairy Apartment Tabuk 5,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458564
OYO 567 AL EAIRY APARTMENT TABUK 2,OYO 567 Al Eairy Apartment Tabuk 2,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458565
OYO 568 AL EAIRY APARTMENT MADINAH 3,OYO 568 Al Eairy Apartment Madinah 3,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111053084
OYO 575 MASSAYA HOTEL APARTMENTS,OYO 575 Massaya Hotel Apartments,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067402
OYO 576 SHROOQ ALBAHA,OYO 576 Shrooq Albaha,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458982
OYO 577 SAIDA VILLAS,OYO 577 Saida Villas,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458827
OYO 578 RABAT HOTEL FURNISHED APARTEMENTS,OYO 578 Rabat Hotel Furnished Apartements,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111067435
OYO 580 MANAR JEDDAH UNITS,OYO 580 Manar Jeddah Units,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458819
OYO 583 AL ANBAR PALACE,OYO 583 Al Anbar Palace,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458833
OYO 584 AL WATHENANI RESORT,OYO 584 Al Wathenani Resort,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458996
OYO 588 SHO’AB JEDDAH SUITES,OYO 588 Sho’ab Jeddah Suites,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458814
OYO 589 LAVINA HOUSE,OYO 589 Lavina House,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458820
OYO 594 TAJ LAMAR FURNISHED APARTMENTS,OYO 594 Taj Lamar Furnished Apartments,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458813
OYO 599 BEAUTAT RESORT,OYO 599 Beautat Resort,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458825
OYO 600 ALHAMRA FOR RESIDENTIAL UNITS,OYO 600 Alhamra For Residential Units,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458627
OYO 601 IBS FOR RESIDENTIAL UNITS,OYO 601 Ibs For Residential Units,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q111458630
OGER SYSTEMS,Oger Systems,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q137552972
OHUD HOSPITAL,Ohud Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q7081166
PAKISTAN INTERNATIONAL SCHOOL BURAYDAH,Pakistan International School Buraydah,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7125609
"PAKISTAN INTERNATIONAL SCHOOL, AL-KHOBAR","Pakistan International School, Al-Khobar",Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7125607
"PAKISTAN INTERNATIONAL SCHOOL, RIYADH","Pakistan International School, Riyadh",Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7125608
PANDA RETAIL COMPANY,Panda Retail Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4832749
PARK HYATT JEDDAH MARINA CLUB AND SPA,Park Hyatt Jeddah Marina Club and Spa,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q136436367
PETRO RABIGH,Petro Rabigh,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7178875
PETROMIN,Petromin,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7179006
PIONEERS HEALTH RESEARCH,Pioneers Health Research,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141490446
PRINCE MOHAMMAD BIN FAHD UNIVERSITY,Prince Mohammad bin Fahd University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7244166
PRINCE MOHAMMED BIN ABDULAZIZ MEDICAL CITY,Prince Mohammed Bin Abdulaziz Medical City,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q28714506
PRINCE MOHAMMED BIN ABDULAZIZ HOSPITAL,Prince Mohammed bin Abdulaziz Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30293468
PRINCE MOHAMMED BIN SALMAN COLLEGE OF BUSINESS AND ENTREPRENEURSHIP,Prince Mohammed bin Salman College of Business and Entrepreneurship,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q60775836
PRINCE MUHAMMAD BIN FAHD GENERAL HOSPITAL AND HEREDITARY BLOOD DISEASES,Prince Muhammad Bin Fahd General Hospital and Hereditary Blood Diseases,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q85875023
PRINCE SATTAM BIN ABDULAZIZ UNIVERSITY,Prince Sattam bin Abdulaziz University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q12204394
PRINCE SULTAN AVIATION ACADEMY,Prince Sultan Aviation Academy,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7244251
PRINCE SULTAN UNIVERSITY,Prince Sultan University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7244255
PRINCES' SCHOOL,Princes' School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7244432
PRINCESS NORA BINT ABDUL RAHMAN UNIVERSITY,Princess Nora bint Abdul Rahman University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q4118886
PROCARE RIAYA HOSPITAL,Procare Riaya Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q50036990
QADIPRO,QadiPro,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140169375
QASSIM CEMENT COMPANY,Qassim Cement Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12218559
QASSIM UNIVERSITY,Qassim University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7267062
QATIF CENTRAL HOSPITAL,Qatif Central Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q6856592
QIDDIYA INVESTMENT COMPANY,Qiddiya Investment Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q135677349
QUAD AXIS GLOBAL,Quad Axis Global,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141773714
QUARA HOLDING,Quara Holding,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q102206559
RIYMAR,RIYMAR,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141946732
RUA ALHARAM ALMAKKI CO,RUA AlHaram AlMakki Co,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q136505542
RAQTAN,Raqtan,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141654586
RASEEL,Raseel,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140227263
RASMALA ALDUWALIYA COMPANY FOR TRADING,Rasmala Alduwaliya Company for Trading,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141605359
RED SEA MALL,Red Sea Mall,Shopping_Retail,SA,,type_mapped,http://www.wikidata.org/entity/Q7305003
REZA FOOD SERVICES,Reza Food Services,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q134989860
RIYAD BANK,Riyad Bank,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q3433985
RIYADH AIR,Riyadh Air,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q115802741
RIYADH GALLERY MALL,Riyadh Gallery Mall,Shopping_Retail,SA,,type_mapped,http://www.wikidata.org/entity/Q111726423
RIYADH MILITARY HOSPITAL,Riyadh Military Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q16123520
RIYADH PARK,Riyadh Park,Shopping_Retail,SA,,type_mapped,http://www.wikidata.org/entity/Q107260098
RIYADH UNIVERSITY OF ARTS,Riyadh University of Arts,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q136399586
ROTANA CINEMA,Rotana Cinema,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12213826
ROYAL SECONDARY INDUSTRIAL INSTITUTE,Royal Secondary Industrial Institute,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q131598453
RUWAD MOWAFAK,Ruwad Mowafak,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141493883
SABIC,SABIC,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q903219
SACO HARDWARE,SACO Hardware,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q20401398
SILQ,SILQ,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141551830
SMSA EXPRESS,SMSA Express,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q97813574
SNAS AVIATION,SNAS Aviation,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q7391800
SOOB,SOOB,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141807064
SAAD NATIONAL SCHOOLS,Saad National Schools,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7395561
SAAD SPECIALIST HOSPITAL,Saad Specialist Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q7395567
SAHARA MALL,Sahara Mall,Shopping_Retail,SA,,type_mapped,http://www.wikidata.org/entity/Q7399501
SAHTEIN RESTAURANT,Sahtein Restaurant,Food_Dining,SA,,type_mapped,http://www.wikidata.org/entity/Q131714528
SALINE WATER CONVERSION CORPORATION,Saline Water Conversion Corporation,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q25062991
SAMA,Sama,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q977140
SAMBA FINANCIAL GROUP,Samba Financial Group,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7408955
SARY,Sary,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141551833
SAUDI ADVANCED INDUSTRIES COMPANY,Saudi Advanced Industries Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7427079
SAUDI AIR AMBULANCE,Saudi Air Ambulance,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q17148539
SAUDI ARABIAN FERTILIZER COMPANY,Saudi Arabian Fertilizer Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q19720632
SAUDI ARABIAN GRAND PRIX,Saudi Arabian Grand Prix,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q101206065
SAUDI ARABIAN MILITARY INDUSTRIES,Saudi Arabian Military Industries,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q48805494
SAUDI ARAMCO,Saudi Aramco,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q679322
SAUDI AWWAL BANK,Saudi Awwal Bank,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q4166519
SAUDI ELECTRICITY COMPANY,Saudi Electricity Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12188903
SAUDI ELECTRONIC UNIVERSITY,Saudi Electronic University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7427134
SAUDI GERMAN HOSPITALS,Saudi German Hospitals,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q104843594
SAUDI INTERNATIONAL PETROCHEMICAL COMPANY,Saudi International Petrochemical Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q3817700
SAUDI INVESTMENT BANK,Saudi Investment Bank,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12184641
SAUDI OGER,Saudi Oger,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q848754
SAUDI RESEARCH AND MEDIA GROUP,Saudi Research and Media Group,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7427161
SAUDI TELECOM COMPANY,Saudi Telecom Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1535171
SAUDISOFT CO.,SaudiSoft Co.,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141043367
SAUDIGULF,Saudigulf,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q16127507
SAVOLA GROUP,Savola Group,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7762363
SAVVY GAMES GROUP,Savvy Games Group,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q110695495
SCHLUMBERGER MIDDLE EAST SA (SAUDI ARABIA),Schlumberger Middle East SA (Saudi Arabia),Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q133812268
SECURITY FORCES HOSPITAL,Security Forces Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q22929148
SEERA GROUP HOLDING,Seera Group Holding,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12239121
SERAFI MEGA MALL,Serafi Mega Mall,Shopping_Retail,SA,,type_mapped,http://www.wikidata.org/entity/Q7452608
SERVICE COMPANION PRIVATE LIMITED,Service Companion Private Limited,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141548293
SHAQRA UNIVERSITY,Shaqra University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q12204502
SHOLA SHOPPING CENTER,Shola Shopping Center,Shopping_Retail,SA,,type_mapped,http://www.wikidata.org/entity/Q106936047
SINOPEC TECH MIDDLE EAST LLC (SAUDI ARABIA),Sinopec Tech Middle East LLC (Saudi Arabia),Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q137943493
SKY PRIME AVIATION,Sky Prime Aviation,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q55394424
SMART ADVANCED TECHNICAL SERVICES,Smart Advanced Technical Services,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141893191
SOLIMAN FAKEEH HOSPITAL,Soliman Fakeeh Hospital,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q30280770
SOLVAIT,Solvait,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141833942
SPARK BY HILTON MAKKAH AZIZIYAH,Spark by Hilton Makkah Aziziyah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q140264285
SULTAN BIN ABDULAZIZ HUMANITARIAN CITY,Sultan Bin Abdulaziz Humanitarian City,Health_Wellness,SA,,type_mapped,http://www.wikidata.org/entity/Q12241862
SWISSÔTEL MAKKAH,Swissôtel Makkah,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q20388886
TAW,TAW,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q137534844
TAIBA INVESTMENTS COMPANY,Taiba Investments company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12218673
TAIBAH UNIVERSITY,Taibah University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7675882
TAIF UNIVERSITY,Taif University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7675938
TAMIMI GROUP,Tamimi Group,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7681456
TAMIMI MARKETS,Tamimi Markets,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q111042647
TANFETH,Tanfeth,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141301588
TEAM FALCONS,Team Falcons,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q126595365
TECHNICAL TRAINERS COLLEGE,Technical Trainers College,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q16123522
"THE HOTEL GALLERIA JEDDAH, CURIO COLLECTION BY HILTON","The Hotel Galleria Jeddah, Curio Collection by Hilton",Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q130716903
"THE RITZ-CARLTON, RIYADH","The Ritz-Carlton, Riyadh",Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q47412709
THE SAUDI NATIONAL BANK,The Saudi National Bank,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q1518238
THEDAR.AI,TheDar.AI,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141592133
TIHAMA,Tihama,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q7801745
TUTIA KIDS OPTICAL,Tutia Kids Optical,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140198897
TWISTED MINDS,Twisted Minds,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q136032297
UMM AL QURA FOR DEVELOPMENT AND CONSTRUCTION,Umm Al Qura for Development and Construction,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q110589695
UMM AL-QURA UNIVERSITY,Umm al-Qura University,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q3133606
UNITED ELECTRONICS COMPANY,United Electronics Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q20401447
UNITED PHARMACY,United pharmacy,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q120444093
UNIVERSITY OF BISHA,University of Bisha,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q22929373
UNIVERSITY OF BUSINESS AND TECHNOLOGY,University of Business and Technology,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q12235851
UNIVERSITY OF HAFR ALBATIN,University of Hafr Albatin,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q27156930
UNIVERSITY OF JEDDAH,University of Jeddah,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q20411232
UNIVERSITY OF PRINCE MUGRIN,University of Prince Mugrin,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q42170247
UNIVERSITY OF TABUK,University of Tabuk,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q7896400
WALADLY,WALADLY,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141733705
WADANA GO,Wadana Go,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q140912566
WADDAH AI,Waddah AI,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141541667
WALDORF ASTORIA JEDDAH - QASR AL SHARQ,Waldorf Astoria Jeddah - Qasr Al Sharq,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q27048574
WHEEKEEP,WheeKeep,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141533938
WIDEBOT,WideBot,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q142033842
"WIRGAN AL NOOR, TAPESTRY COLLECTION BY HILTON","Wirgan Al Noor, Tapestry Collection by Hilton",Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q139068537
XENEL,Xenel,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q8043465
YALLA ENGLISH,Yalla English,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q141142219
YANBU INTERNATIONAL SCHOOL,Yanbu International School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q8048277
YANBU NATIONAL PETROCHEMICAL COMPANY,Yanbu National Petrochemical Company,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q3817709
YANBU UNIVERSITY COLLEGE,Yanbu University College,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q8048282
YARA INTERNATIONAL SCHOOL,Yara International School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q110664415
YUSR INTERNATIONAL SCHOOL,Yusr International School,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q8061907
ZAIN SAUDI ARABIA,Zain Saudi Arabia,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12218575
ZAMIL INDUSTRIAL,Zamil Industrial,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q12218607
ALGHAD COLLEGES FOR APPLIED MEDICAL SCIENCE,alghad Colleges for applied medical science,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q17003495
ALMATAR,almatar,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q64577321
DR.CAFE COFFEE,dr.cafe Coffee,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q105714225
FLYADEAL,flyadeal,Travel,SA,,type_mapped,http://www.wikidata.org/entity/Q24035331
HUMAIN,humain,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q134444212
IGARAGE,iGarage,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q122974634
TATEER EDUCATIONAL TECHNOLOGIES,tateer educational technologies,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q134604230
THEOCTOPUS-AI.COM,theoctopus-ai.com,Others,SA,,unreviewed_business_excluded,http://www.wikidata.org/entity/Q139741426
ÉCOLE FRANÇAISE INTERNATIONALE DE RIYAD,École Française Internationale de Riyad,Housing_Education,SA,,type_mapped,http://www.wikidata.org/entity/Q21674517
```
