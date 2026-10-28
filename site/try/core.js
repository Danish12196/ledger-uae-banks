/* Ledger — "Try it with your data": core logic.
   Pure functions only (no DOM). Runs entirely in the browser; nothing here makes a network request.
   Also loadable in Node for tests: everything is attached to globalThis.LedgerCore. */
(function (root) {
  'use strict';

  // ---------------------------------------------------------------- categories
  const CATS = ['Food_Dining', 'Groceries', 'Transport_Auto', 'Shopping_Retail', 'Utilities_Telecom',
    'Health_Wellness', 'Travel', 'Entertainment', 'Government_Fees', 'Housing_Education',
    'Digital_Subscriptions', 'Others'];
  const CAT_LABEL = {
    Food_Dining: 'Food & dining', Groceries: 'Groceries', Transport_Auto: 'Transport & auto',
    Shopping_Retail: 'Shopping', Utilities_Telecom: 'Utilities & telecom', Health_Wellness: 'Health & wellness',
    Travel: 'Travel', Entertainment: 'Entertainment', Government_Fees: 'Government fees',
    Housing_Education: 'Housing & education', Digital_Subscriptions: 'Digital & subscriptions', Others: 'Others'
  };
  const DISCRETIONARY = new Set(['Food_Dining', 'Shopping_Retail', 'Entertainment', 'Travel', 'Digital_Subscriptions']);

  // Ordered merchant rules: first match wins. name = canonical merchant name (optional).
  // Specific brands come before generic words ("noon food" before "noon", "amazon prime" before "amazon").
  const R = (kws, cat, name) => ({ kws, cat, name });
  const RULES = [
    // transfers / non-spend first
    R(['transfer to own', 'own account transfer', 'internal transfer', 'credit card payment', 'card payment received',
      'cc payment', 'payment - thank you', 'payment thank you', 'transfer between'], '__TRANSFER__'),
    // digital subscriptions
    R(['netflix'], 'Digital_Subscriptions', 'Netflix'), R(['spotify'], 'Digital_Subscriptions', 'Spotify'),
    R(['anghami'], 'Digital_Subscriptions', 'Anghami'), R(['shahid'], 'Digital_Subscriptions', 'Shahid'),
    R(['osn'], 'Digital_Subscriptions', 'OSN+'), R(['starzplay', 'starz play'], 'Digital_Subscriptions', 'STARZPLAY'),
    R(['disney'], 'Digital_Subscriptions', 'Disney+'), R(['youtube'], 'Digital_Subscriptions', 'YouTube'),
    R(['amazon prime', 'prime video', 'primevideo'], 'Digital_Subscriptions', 'Amazon Prime'),
    R(['apple.com/bill', 'apple.com', 'itunes', 'icloud'], 'Digital_Subscriptions', 'Apple Services'),
    R(['google one', 'google storage', 'google play', 'google *'], 'Digital_Subscriptions', 'Google'),
    R(['chatgpt', 'openai'], 'Digital_Subscriptions', 'OpenAI'), R(['anthropic', 'claude.ai'], 'Digital_Subscriptions', 'Anthropic'),
    R(['microsoft', 'msft'], 'Digital_Subscriptions', 'Microsoft'), R(['adobe'], 'Digital_Subscriptions', 'Adobe'),
    R(['dropbox'], 'Digital_Subscriptions', 'Dropbox'), R(['github'], 'Digital_Subscriptions', 'GitHub'),
    R(['vercel'], 'Digital_Subscriptions', 'Vercel'), R(['notion'], 'Digital_Subscriptions', 'Notion'),
    R(['canva'], 'Digital_Subscriptions', 'Canva'), R(['game pass'], 'Digital_Subscriptions', 'Xbox Game Pass'),
    // food delivery & dining
    R(['talabat'], 'Food_Dining', 'Talabat'), R(['deliveroo'], 'Food_Dining', 'Deliveroo'),
    R(['noon food', 'noonfood'], 'Food_Dining', 'noon Food'), R(['careem food', 'careem now'], 'Food_Dining', 'Careem Food'),
    R(['zomato'], 'Food_Dining', 'Zomato'), R(['eat easy', 'eateasy'], 'Food_Dining', 'EatEasy'),
    R(['starbucks'], 'Food_Dining', 'Starbucks'), R(['tim hortons'], 'Food_Dining', 'Tim Hortons'),
    R(['costa coffee', 'costa'], 'Food_Dining', 'Costa Coffee'), R(['mcdonald'], 'Food_Dining', "McDonald's"),
    R(['kfc'], 'Food_Dining', 'KFC'), R(['shake shack'], 'Food_Dining', 'Shake Shack'), R(['subway'], 'Food_Dining', 'Subway'),
    R(['domino'], 'Food_Dining', "Domino's"), R(['papa john'], 'Food_Dining', "Papa John's"), R(['hardee'], 'Food_Dining', "Hardee's"),
    R(['popeyes'], 'Food_Dining', 'Popeyes'), R(['five guys'], 'Food_Dining', 'Five Guys'), R(['pizza hut'], 'Food_Dining', 'Pizza Hut'),
    R(['restaurant', 'resturant', 'cafe', 'café', 'coffee', 'bakery', 'grill', 'kitchen', 'shawarma', 'burger', 'pizza',
      'sushi', 'bistro', 'eatery', 'diner', 'karak', 'cafeteria', 'food court', 'falafel', 'biryani', 'zaatar', 'manousheh',
      'pf chang', 'steakhouse', 'tea house', 'juice'], 'Food_Dining'),
    // groceries
    R(['carrefour'], 'Groceries', 'Carrefour'), R(['spinneys'], 'Groceries', 'Spinneys'), R(['lulu'], 'Groceries', 'LuLu'),
    R(['waitrose'], 'Groceries', 'Waitrose'), R(['union coop', 'union co-op', 'unioncoop'], 'Groceries', 'Union Coop'),
    R(['choithram'], 'Groceries', 'Choithrams'), R(['viva'], 'Groceries', 'Viva'), R(['nesto'], 'Groceries', 'Nesto'),
    R(['grandiose'], 'Groceries', 'Grandiose'), R(['al maya', 'almaya'], 'Groceries', 'Al Maya'),
    R(['kibsons'], 'Groceries', 'Kibsons'), R(['instashop'], 'Groceries', 'InstaShop'),
    R(['noon minutes', 'noon minute'], 'Groceries', 'noon Minutes'), R(['west zone'], 'Groceries', 'West Zone'),
    R(['supermarket', 'hypermarket', 'grocery', 'groceries', 'baqala', 'mini mart', 'minimart', 'butcher'], 'Groceries'),
    // transport
    R(['enoc'], 'Transport_Auto', 'ENOC'), R(['adnoc'], 'Transport_Auto', 'ADNOC'), R(['emarat'], 'Transport_Auto', 'Emarat'),
    R(['eppco'], 'Transport_Auto', 'EPPCO'), R(['salik'], 'Transport_Auto', 'Salik'), R(['darb'], 'Transport_Auto', 'Darb'),
    R(['parkin', 'mawaqif', 'parking'], 'Transport_Auto', 'Parking'), R(['nol '], 'Transport_Auto', 'nol'),
    R(['careem'], 'Transport_Auto', 'Careem'), R(['uber'], 'Transport_Auto', 'Uber'), R(['hala taxi', 'hala'], 'Transport_Auto', 'Hala'),
    R(['taxi', 'petrol', 'fuel', 'car wash', 'tyre', 'tire', 'autopro', 'garage', 'rent a car', 'car rental'], 'Transport_Auto'),
    // government (before RTA so fines land here)
    R(['dubai police', 'traffic fine', 'rta fine', 'fines'], 'Government_Fees', 'Traffic fines'),
    R(['icp', 'gdrfa', 'amer', 'tasheel', 'tawjeeh', 'mohre', 'emirates id', 'visa fee', 'visa renewal'], 'Government_Fees'),
    R(['dubai municipality', 'municipality', 'dld', 'dubai land', 'court', 'typing', 'dubai now', 'tamm', 'government'], 'Government_Fees'),
    R(['rta'], 'Transport_Auto', 'RTA'),
    // utilities & telecom
    R(['dewa'], 'Utilities_Telecom', 'DEWA'), R(['sewa'], 'Utilities_Telecom', 'SEWA'), R(['addc'], 'Utilities_Telecom', 'ADDC'),
    R(['fewa', 'etihad water'], 'Utilities_Telecom', 'Etihad WE'), R(['empower'], 'Utilities_Telecom', 'Empower'),
    R(['etisalat', 'e&', 'eand'], 'Utilities_Telecom', 'e&'), R(['du', 'emirates integrated'], 'Utilities_Telecom', 'du'),
    R(['virgin mobile'], 'Utilities_Telecom', 'Virgin Mobile'), R(['lootah gas', 'gas cylinder'], 'Utilities_Telecom'),
    R(['recharge', 'internet', 'telecom', 'utility', 'electricity', 'water bill', 'chiller'], 'Utilities_Telecom'),
    // health
    R(['life pharmacy'], 'Health_Wellness', 'Life Pharmacy'), R(['boots'], 'Health_Wellness', 'Boots'),
    R(['aster'], 'Health_Wellness', 'Aster'), R(['bin sina'], 'Health_Wellness', 'BinSina'), R(['supercare'], 'Health_Wellness', 'Supercare'),
    R(['mediclinic'], 'Health_Wellness', 'Mediclinic'), R(['gymnation'], 'Health_Wellness', 'GymNation'),
    R(['fitness first'], 'Health_Wellness', 'Fitness First'),
    R(['pharmacy', 'hospital', 'clinic', 'medical', 'dental', 'gym', 'fitness', 'optic', 'healthcare', 'physio', 'lab '], 'Health_Wellness'),
    // travel
    R(['flydubai'], 'Travel', 'flydubai'), R(['air arabia'], 'Travel', 'Air Arabia'), R(['etihad airways'], 'Travel', 'Etihad Airways'),
    R(['emirates airline', 'emirates.com', 'emirates air'], 'Travel', 'Emirates'), R(['booking.com'], 'Travel', 'Booking.com'),
    R(['agoda'], 'Travel', 'Agoda'), R(['expedia'], 'Travel', 'Expedia'), R(['airbnb'], 'Travel', 'Airbnb'),
    R(['hotel', 'marriott', 'hilton', 'rotana', 'jumeirah', 'airport', 'dnata', 'airline', 'airways', 'holiday', 'trip.com'], 'Travel'),
    // entertainment
    R(['vox'], 'Entertainment', 'VOX Cinemas'), R(['reel cinema'], 'Entertainment', 'Reel Cinemas'), R(['novo cinema'], 'Entertainment', 'Novo Cinemas'),
    R(['playstation', 'psn'], 'Entertainment', 'PlayStation'), R(['steam'], 'Entertainment', 'Steam'), R(['nintendo'], 'Entertainment', 'Nintendo'),
    R(['platinumlist'], 'Entertainment', 'Platinumlist'), R(['ticketmaster'], 'Entertainment', 'Ticketmaster'),
    R(['cinema', 'bowling', 'magic planet', 'img worlds', 'ski dubai', 'aquaventure', 'wild wadi', 'theme park', 'concert'], 'Entertainment'),
    // housing & education
    R(['uowd', 'university', 'school', 'tuition', 'gems ', 'taaleem', 'nursery', 'academy', 'coursera', 'udemy'], 'Housing_Education'),
    R(['ejari', 'rent', 'landlord', 'real estate', 'properties', 'service charge', 'chq', 'cheque'], 'Housing_Education'),
    // shopping
    R(['amazon'], 'Shopping_Retail', 'Amazon'), R(['noon'], 'Shopping_Retail', 'noon'), R(['namshi'], 'Shopping_Retail', 'Namshi'),
    R(['ikea'], 'Shopping_Retail', 'IKEA'), R(['home centre'], 'Shopping_Retail', 'Home Centre'), R(['centrepoint'], 'Shopping_Retail', 'Centrepoint'),
    R(['sharaf dg'], 'Shopping_Retail', 'Sharaf DG'), R(['jumbo'], 'Shopping_Retail', 'Jumbo'), R(['virgin megastore'], 'Shopping_Retail', 'Virgin Megastore'),
    R(['ace hardware'], 'Shopping_Retail', 'ACE'), R(['daiso'], 'Shopping_Retail', 'Daiso'), R(['decathlon'], 'Shopping_Retail', 'Decathlon'),
    R(['h&m'], 'Shopping_Retail', 'H&M'), R(['zara'], 'Shopping_Retail', 'Zara'), R(['max fashion'], 'Shopping_Retail', 'Max'),
    R(['apple store'], 'Shopping_Retail', 'Apple Store'),
    R(['mall', 'electronics', 'fashion', 'store', 'shop', 'trading', 'market'], 'Shopping_Retail'),
    // cash
    R(['atm', 'cash withdrawal'], 'Others', 'ATM withdrawal')
  ].map(r => ({ ...r, res: r.kws.map(kwRegex) }));

  function kwRegex(kw) {
    const k = kw.toLowerCase().trim();
    const esc = k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    return new RegExp('(?:^|[^a-z0-9])' + esc + (/[a-z0-9]$/.test(k) ? '(?=$|[^a-z0-9])' : ''), 'i');
  }

  function matchRule(desc) {
    const s = ' ' + String(desc || '').toLowerCase().replace(/\s+/g, ' ') + ' ';
    for (const r of RULES) if (r.res.some(re => re.test(s))) return r;
    return null;
  }

  // ---------------------------------------------------------------- merchant cleaning
  function titleCase(s) {
    return s.toLowerCase().replace(/(^|[\s\-/&(])([a-z])/g, (m, a, b) => a + b.toUpperCase());
  }
  function cleanMerchant(desc) {
    let s = String(desc || '').toUpperCase();
    s = s.replace(/\d*X{2,}\d*/g, ' ').replace(/\*{2,}\d*/g, ' ');
    s = s.replace(/\b(POS|PURCHASES?|PURCHASED|PAYMENT|TXN|TRANSACTION|DEBIT|CREDIT|CARD|ECOM|E-COM|ONLINE|APPLE ?PAY|GOOGLE ?PAY|SAMSUNG ?PAY|CONTACTLESS|REF|AUTH|AT|FROM|VIA|INTL|INTERNATIONAL|DR|CR|CHQ|CHEQUE|CHECK|NO)\b/g, ' ');
    s = s.replace(/\b\d{3,}\b|\b[A-Z]*\d{4,}[A-Z0-9]*\b/g, ' ');
    s = s.replace(/\b(DUBAI|DXB|ABU ?DHABI|AUH|SHARJAH|SHJ|AJMAN|AL AIN|RAS AL KHAIMAH|RAK|FUJAIRAH|UAE|AE|ARE|UNITED ARAB EMIRATES|LLC|L\.L\.C|FZ-?LLC|FZE|FZCO|BR|BRANCH)\b\.?/g, ' ');
    s = s.replace(/[^A-Z0-9&'.\- ]/g, ' ').replace(/\s+/g, ' ').replace(/^[\s.\-]+|[\s.\-]+$/g, '').trim();
    if (!s) s = String(desc || '').trim().slice(0, 40) || 'Unknown';
    return titleCase(s).slice(0, 48);
  }

  // Map a user-supplied category name onto Ledger's 12 (used for discretionary detection and the lexicon toggle).
  const CAT_SYNONYMS = [
    [/food|dining|restaurant|eat|takeaway|delivery|coffee|cafe/i, 'Food_Dining'],
    [/grocer|supermarket/i, 'Groceries'],
    [/transport|auto|car|fuel|petrol|taxi|travel.?local|parking|salik/i, 'Transport_Auto'],
    [/shop|retail|cloth|electronic|household/i, 'Shopping_Retail'],
    [/utilit|telecom|phone|mobile|internet|bill|dewa|electric|water/i, 'Utilities_Telecom'],
    [/health|medical|pharm|fitness|gym|wellness|doctor/i, 'Health_Wellness'],
    [/travel|flight|hotel|holiday|vacation/i, 'Travel'],
    [/entertain|cinema|movie|game|fun|leisure|hobby/i, 'Entertainment'],
    [/gov|fee|fine|visa|tax/i, 'Government_Fees'],
    [/hous|rent|home|education|school|tuition|universit/i, 'Housing_Education'],
    [/subscri|digital|stream|software|app/i, 'Digital_Subscriptions']
  ];
  function mapUserCategory(c) {
    const s = String(c || '');
    if (CATS.includes(s)) return s;
    for (const [re, cat] of CAT_SYNONYMS) if (re.test(s)) return cat;
    return 'Others';
  }

  // ---------------------------------------------------------------- CSV
  function detectDelimiter(text) {
    const lines = text.split(/\r?\n/).filter(l => l.trim()).slice(0, 10);
    let best = ',', bestScore = -1;
    for (const d of [',', ';', '\t', '|']) {
      const counts = lines.map(l => splitCSVLine(l, d).length);
      const mode = counts.sort((a, b) => counts.filter(x => x === b).length - counts.filter(x => x === a).length)[0];
      const score = mode > 1 ? counts.filter(c => c === mode).length * 10 + mode : 0;
      if (score > bestScore) { bestScore = score; best = d; }
    }
    return best;
  }
  function splitCSVLine(line, d) { return parseCSV(line, d)[0] || []; }
  function parseCSV(text, d) {
    text = String(text).replace(/^﻿/, '');
    if (!d) d = detectDelimiter(text);
    const rows = []; let row = [], f = '', q = false;
    for (let i = 0; i < text.length; i++) {
      const c = text[i];
      if (q) {
        if (c === '"') { if (text[i + 1] === '"') { f += '"'; i++; } else q = false; }
        else f += c;
      } else if (c === '"' && f === '') q = true;
      else if (c === d) { row.push(f); f = ''; }
      else if (c === '\n' || c === '\r') {
        if (c === '\r' && text[i + 1] === '\n') i++;
        row.push(f); f = '';
        if (row.some(x => x.trim() !== '')) rows.push(row);
        row = [];
      } else f += c;
    }
    row.push(f); if (row.some(x => x.trim() !== '')) rows.push(row);
    return rows;
  }

  // ---------------------------------------------------------------- dates & amounts
  const MON = { jan: 1, feb: 2, mar: 3, apr: 4, may: 5, jun: 6, jul: 7, aug: 8, sep: 9, sept: 9, oct: 10, nov: 11, dec: 12 };
  const MONTH_NAMES = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  const pad = n => String(n).padStart(2, '0');
  function ymd(y, m, d) {
    if (y < 100) y += 2000;
    if (!(m >= 1 && m <= 12 && d >= 1 && d <= 31 && y > 1990 && y < 2100)) return null;
    const dt = new Date(Date.UTC(y, m - 1, d));
    if (dt.getUTCMonth() !== m - 1) return null;
    return `${y}-${pad(m)}-${pad(d)}`;
  }
  function monKey(s) { return MON[String(s).toLowerCase().slice(0, 4)] || MON[String(s).toLowerCase().slice(0, 3)]; }
  function parseDate(v, order) {
    if (v == null) return null;
    let s = String(v).trim(); if (!s) return null;
    let m;
    if ((m = s.match(/^(\d{4})[-/.](\d{1,2})[-/.](\d{1,2})/))) return ymd(+m[1], +m[2], +m[3]);
    if ((m = s.match(/^(\d{1,2})[-/.](\d{1,2})[-/.](\d{2,4})\b/))) {
      let a = +m[1], b = +m[2];
      return order === 'MDY' ? ymd(+m[3], a, b) : ymd(+m[3], b, a);
    }
    if ((m = s.match(/^(\d{1,2})[-\s/]+([A-Za-z]{3,9})[-\s/,]+(\d{2,4})/))) { const mm = monKey(m[2]); return mm ? ymd(+m[3], mm, +m[1]) : null; }
    if ((m = s.match(/^([A-Za-z]{3,9})[-\s/]+(\d{1,2}),?[-\s/]+(\d{2,4})/))) { const mm = monKey(m[1]); return mm ? ymd(+m[3], mm, +m[2]) : null; }
    if (/^\d{5}(\.\d+)?$/.test(s)) { // Excel serial
      const n = Math.floor(+s); if (n > 30000 && n < 60000) { const d = new Date(Date.UTC(1899, 11, 30) + n * 864e5); return d.toISOString().slice(0, 10); }
    }
    return null;
  }
  function detectDateOrder(values) {
    let dmy = 0, mdy = 0;
    for (const v of values) {
      const m = String(v || '').trim().match(/^(\d{1,2})[-/.](\d{1,2})[-/.]\d{2,4}/);
      if (!m) continue;
      if (+m[1] > 12) dmy++; if (+m[2] > 12) mdy++;
    }
    return mdy > dmy ? 'MDY' : 'DMY'; // UAE default is day-first
  }
  function parseAmount(v) {
    if (v == null) return null;
    if (typeof v === 'number') return isFinite(v) ? v : null;
    let s = String(v).trim(); if (!s) return null;
    let neg = /^\(.*\)$/.test(s) || /\bDR\b/i.test(s) || /-\s*[\d.,]/.test(s) || /[\d.]\s*-$/.test(s);
    if (/\bCR\b/i.test(s)) neg = false;
    let num = s.replace(/[^0-9.,]/g, '');
    if (!/\d/.test(num)) return null;
    if (/,\d{2}$/.test(num) && !/\./.test(num)) num = num.replace(/\./g, '').replace(',', '.'); // 1.234,56
    num = parseFloat(num.replace(/,/g, ''));
    if (!isFinite(num)) return null;
    return neg ? -num : num;
  }

  // ---------------------------------------------------------------- column detection
  const HEAD = {
    date: /(^|\b)(date|posted|posting|txn date|transaction date|value date|booking date|تاريخ)/i,
    desc: /(payee|merchant|description|narration|details|particulars|memo|beneficiary|name|transaction|بيان|وصف|التفاصيل)/i,
    amount: /(^amount|amount \(|^aed|^value$|^sum$|amount$|مبلغ|المبلغ)/i,
    debit: /(debit|withdraw|money out|paid out|^dr$|outflow|مدين)/i,
    credit: /(credit|deposit|money in|paid in|^cr$|inflow|دائن)/i,
    category: /(categor|فئة|التصنيف)/i,
    account: /(^account$|account name|^bank$|^card$|^source$|^wallet$)/i
  };
  function guessColumns(header, rows) {
    const H = header.map(h => String(h || '').trim());
    const find = (re, not) => H.findIndex((h, i) => re.test(h) && !(not || []).includes(i));
    const sample = rows.slice(0, 60);
    const colScore = (i, f) => sample.filter(r => f(r[i])).length / Math.max(1, sample.length);
    let date = find(HEAD.date);
    if (date < 0) { let b = -1, bs = 0; H.forEach((_, i) => { const s = colScore(i, v => parseDate(v, 'DMY')); if (s > bs) { bs = s; b = i; } }); if (bs > .6) date = b; }
    let debit = find(HEAD.debit), credit = find(HEAD.credit, [debit]);
    let amount = find(HEAD.amount, [date, debit, credit]);
    if (amount < 0 && (debit < 0 || credit < 0)) {
      let b = -1, bs = 0; H.forEach((h, i) => { if (i === date || /balance/i.test(h)) return; const s = colScore(i, v => parseAmount(v) != null && !parseDate(v, 'DMY')); if (s > bs) { bs = s; b = i; } });
      if (bs > .6) amount = b;
    }
    let category = find(HEAD.category);
    let desc = -1;
    for (const re of [/(payee|merchant)/i, /(description|narration|details|particulars|بيان|وصف)/i, HEAD.desc]) {
      desc = H.findIndex((h, i) => re.test(h) && ![date, amount, debit, credit, category].includes(i)); if (desc >= 0) break;
    }
    if (desc < 0) { // longest average text column
      let b = -1, bl = 0; H.forEach((_, i) => { if ([date, amount, debit, credit, category].includes(i)) return; const l = sample.reduce((a, r) => a + String(r[i] || '').length, 0); if (l > bl) { bl = l; b = i; } }); desc = b;
    }
    const account = find(HEAD.account, [desc, category]);
    const useSplit = amount < 0 && debit >= 0 && credit >= 0;
    return { date, desc, amount: useSplit ? -1 : amount, debit: useSplit ? debit : -1, credit: useSplit ? credit : -1, category, account };
  }

  // ---------------------------------------------------------------- build transactions
  /* opts: {map:{date,desc,amount,debit,credit,category,account}, dateOrder, signMode:'auto'|'negExpense'|'posExpense', catSource:'auto'|'file'} */
  function buildTransactions(header, rows, opts) {
    const m = opts.map, dateOrder = opts.dateOrder || detectDateOrder(rows.map(r => r[m.date]));
    const out = [], skipped = [];
    const raw = rows.map((r, i) => {
      const date = parseDate(r[m.date], dateOrder);
      let val = null;
      if (m.amount >= 0) val = parseAmount(r[m.amount]);
      else {
        const d = parseAmount(r[m.debit]), c = parseAmount(r[m.credit]);
        if (d) val = -Math.abs(d); else if (c) val = Math.abs(c);
      }
      return { i, date, val, desc: String(r[m.desc] ?? '').trim(), cat: m.category >= 0 ? String(r[m.category] ?? '').trim() : '', account: m.account >= 0 ? String(r[m.account] ?? '').trim() : '' };
    });
    const valid = raw.filter(x => x.date && x.val != null && x.val !== 0);
    let signMode = opts.signMode || 'auto';
    if (signMode === 'auto') {
      if (m.amount < 0) signMode = 'negExpense';
      else { const neg = valid.filter(x => x.val < 0).length; signMode = neg >= valid.length - neg ? 'negExpense' : 'posExpense'; }
    }
    let catSource = opts.catSource || (m.category >= 0 ? 'file' : 'auto');
    let id = 0, transfers = 0;
    for (const x of raw) {
      if (!x.date || x.val == null || x.val === 0) { skipped.push(x.i); continue; }
      const isExpense = signMode === 'negExpense' ? x.val < 0 : x.val > 0;
      const rule = matchRule(x.desc + ' ' + x.cat);
      let direction = isExpense ? 'expense' : 'income';
      if ((rule && rule.cat === '__TRANSFER__') || /^\s*transfer\s*[:\-]/i.test(x.desc)) { direction = 'transfer'; transfers++; }
      else if (!isExpense && /\b(refund|reversal|reversed|cashback|cash back|chargeback)\b/i.test(x.desc)) direction = 'refund';
      else if (catSource === 'file' && /transfer|credit card pay/i.test(x.cat)) { direction = 'transfer'; transfers++; }
      const merchant = rule && rule.name ? rule.name : cleanMerchant(x.desc);
      let category;
      if (direction === 'income') category = 'Income';
      else if (direction === 'transfer') category = 'Transfer';
      else if (direction === 'refund') category = 'Refund';
      else if (catSource === 'file' && x.cat) category = x.cat;
      else category = rule && rule.cat !== '__TRANSFER__' ? rule.cat : 'Others';
      out.push({ id: ++id, date: x.date, month: x.date.slice(0, 7), year: +x.date.slice(0, 4), description: x.desc, merchant, category,
        amount: Math.round(Math.abs(x.val) * 100) / 100, direction, account: x.account || '' , catGuessed: !(catSource === 'file' && x.cat) && direction === 'expense' && !(rule && rule.cat !== '__TRANSFER__')});
    }
    return { tx: out, skipped, signMode, dateOrder, catSource, transfers };
  }

  // ---------------------------------------------------------------- database
  const SCHEMA = `CREATE TABLE tx(
  id INTEGER PRIMARY KEY,
  date TEXT,        -- 'YYYY-MM-DD'
  month TEXT,       -- 'YYYY-MM'
  year INTEGER,
  description TEXT, -- raw bank text
  merchant TEXT,    -- cleaned merchant name
  category TEXT,
  amount REAL,      -- always positive, AED
  direction TEXT,   -- 'expense' | 'income' | 'transfer' | 'refund'
  account TEXT
);`;
  function buildDB(SQL, tx) {
    const db = new SQL.Database();
    db.run(SCHEMA);
    db.run('BEGIN');
    const st = db.prepare('INSERT INTO tx VALUES (?,?,?,?,?,?,?,?,?,?)');
    for (const t of tx) st.run([t.id, t.date, t.month, t.year, t.description, t.merchant, t.category, t.amount, t.direction, t.account]);
    st.free(); db.run('COMMIT');
    db.run('CREATE INDEX ix_date ON tx(date); CREATE INDEX ix_cat ON tx(category); CREATE INDEX ix_mer ON tx(merchant);');
    return db;
  }
  function query(db, sql, params) {
    const res = db.exec(sql, params || []);
    if (!res.length) return { cols: [], rows: [] };
    return { cols: res[0].columns, rows: res[0].values };
  }
  function scalar(db, sql, params) { const r = query(db, sql, params); return r.rows.length ? r.rows[0][0] : null; }

  // ---------------------------------------------------------------- dates helpers
  function addMonths(ym, k) { let [y, m] = ym.split('-').map(Number); m += k; y += Math.floor((m - 1) / 12); m = ((m - 1) % 12 + 12) % 12 + 1; return `${y}-${pad(m)}`; }
  function monthEnd(ym) { const [y, m] = ym.split('-').map(Number); return `${ym}-${pad(new Date(Date.UTC(y, m, 0)).getUTCDate())}`; }
  function monthLabel(ym) { const [y, m] = ym.split('-').map(Number); return `${MONTH_NAMES[m - 1]} ${y}`; }
  function monthShort(ym) { const [y, m] = ym.split('-').map(Number); return `${MONTH_NAMES[m - 1].slice(0, 3)} ${String(y).slice(2)}`; }
  function monthsBetween(a, b) { const [y1, m1] = a.split('-').map(Number), [y2, m2] = b.split('-').map(Number); return (y2 - y1) * 12 + (m2 - m1); }
  function addDays(d, k) { const t = new Date(d + 'T00:00:00Z'); t.setUTCDate(t.getUTCDate() + k); return t.toISOString().slice(0, 10); }
  function fmtDate(d) { const [y, m, dd] = d.split('-').map(Number); return `${dd} ${MONTH_NAMES[m - 1].slice(0, 3)} ${y}`; }

  // ---------------------------------------------------------------- formatting
  function aed(n) {
    if (n == null || !isFinite(n)) return 'AED 0';
    const a = Math.abs(n), d = a >= 1000 ? 0 : 2;
    return (n < 0 ? '−' : '') + 'AED ' + a.toLocaleString('en-US', { minimumFractionDigits: d, maximumFractionDigits: d });
  }
  function catName(c) { return CAT_LABEL[c] || c; }

  // ---------------------------------------------------------------- analytics
  function dataRange(db) {
    const r = query(db, "SELECT MIN(date), MAX(date), COUNT(*) FROM tx WHERE direction='expense'").rows[0];
    return { min: r[0], max: r[1], n: r[2] };
  }
  function overview(db) {
    const rng = dataRange(db);
    if (!rng.min) return null;
    const spent = scalar(db, "SELECT SUM(amount) FROM tx WHERE direction='expense'") || 0;
    const income = scalar(db, "SELECT SUM(amount) FROM tx WHERE direction='income'") || 0;
    const nMonths = monthsBetween(rng.min.slice(0, 7), rng.max.slice(0, 7)) + 1;
    const transfers = scalar(db, "SELECT COUNT(*) FROM tx WHERE direction='transfer'") || 0;
    return { ...rng, spent, income, nMonths, avgMonth: spent / nMonths, transfers, merchants: scalar(db, "SELECT COUNT(DISTINCT merchant) FROM tx WHERE direction='expense'") };
  }
  function monthlyByCategory(db) {
    const r = query(db, "SELECT month, category, SUM(amount) FROM tx WHERE direction='expense' GROUP BY month, category ORDER BY month");
    const months = [...new Set(r.rows.map(x => x[0]))];
    if (months.length) { // fill gaps
      const all = []; for (let m = months[0]; m <= months[months.length - 1]; m = addMonths(m, 1)) all.push(m);
      months.splice(0, months.length, ...all);
    }
    const cats = [...new Set(r.rows.map(x => x[1]))];
    const tot = {}; r.rows.forEach(([, c, v]) => tot[c] = (tot[c] || 0) + v);
    cats.sort((a, b) => tot[b] - tot[a]);
    const series = cats.map(c => ({ cat: c, values: months.map(m => { const x = r.rows.find(y => y[0] === m && y[1] === c); return x ? Math.round(x[2] * 100) / 100 : 0; }) }));
    return { months, series };
  }
  function categoryTotals(db) {
    return query(db, "SELECT category, ROUND(SUM(amount),2) total, COUNT(*) n FROM tx WHERE direction='expense' GROUP BY category ORDER BY total DESC").rows;
  }
  function topMerchants(db, n) {
    return query(db, "SELECT merchant, category, ROUND(SUM(amount),2) total, COUNT(*) n FROM tx WHERE direction='expense' GROUP BY merchant ORDER BY total DESC LIMIT ?", [n || 10]).rows;
  }
  function median(a) { const s = [...a].sort((x, y) => x - y), k = s.length >> 1; return s.length ? (s.length % 2 ? s[k] : (s[k - 1] + s[k]) / 2) : 0; }

  function recurring(db) {
    const anchor = dataRange(db).max; if (!anchor) return [];
    const rows = query(db, "SELECT merchant, category, month, SUM(amount), COUNT(*), MAX(date) FROM tx WHERE direction='expense' GROUP BY merchant, month").rows;
    const by = {};
    rows.forEach(([mer, cat, mon, amt, cnt, last]) => { (by[mer] = by[mer] || { mer, cat, months: [] }).months.push({ mon, amt, cnt, last }); });
    const out = [];
    for (const o of Object.values(by)) {
      if (o.months.length < 3 || /\b(atm|cash)\b/i.test(o.mer)) continue;
      const ms = o.months.map(x => x.mon).sort();
      const span = monthsBetween(ms[0], ms[ms.length - 1]) + 1;
      const coverage = o.months.length / span;
      const perTxn = o.months.every(x => x.cnt <= 2);
      const amts = o.months.map(x => x.amt), med = median(amts);
      const mad = median(amts.map(a => Math.abs(a - med))) / (med || 1);
      if (coverage < .7 || !perTxn || mad > .15) continue;
      const last = o.months.reduce((a, x) => x.last > a ? x.last : a, '');
      const active = last >= addDays(anchor, -45);
      out.push({ merchant: o.mer, category: o.cat, typical: med, months: o.months.length, since: ms[0], last, active, yearly: med * 12 });
    }
    return out.sort((a, b) => (b.active - a.active) || (b.typical - a.typical));
  }

  // "Where could I cut": recent 3 complete months vs median of the 6 months before, discretionary categories only.
  function cutSuggestions(db, discretionaryOf) {
    const anchor = dataRange(db).max; if (!anchor) return { items: [], window: null };
    const isDisc = discretionaryOf || (c => DISCRETIONARY.has(mapUserCategory(c)));
    let lastFull = anchor.slice(0, 7);
    if (anchor < addDays(monthEnd(lastFull), -3)) lastFull = addMonths(lastFull, -1); // anchor month still in progress
    const recent = [addMonths(lastFull, -2), addMonths(lastFull, -1), lastFull];
    const base = []; for (let k = 3; k <= 8; k++) base.push(addMonths(lastFull, -k));
    const rows = query(db, "SELECT category, month, SUM(amount) FROM tx WHERE direction='expense' AND month BETWEEN ? AND ? GROUP BY category, month", [base[5], lastFull]).rows;
    const firstMonth = dataRange(db).min.slice(0, 7);
    const baseAvail = base.filter(m => m >= firstMonth);
    if (baseAvail.length < 2) return { items: [], window: { recent, base: baseAvail }, note: 'Needs at least 5 months of data.' };
    const cats = [...new Set(rows.map(r => r[0]))].filter(isDisc);
    const val = (c, m) => { const r = rows.find(x => x[0] === c && x[1] === m); return r ? r[2] : 0; };
    const items = cats.map(c => {
      const rec = recent.reduce((a, m) => a + val(c, m), 0) / 3;
      const usual = median(baseAvail.map(m => val(c, m)));
      const steady = recent.filter(m => val(c, m) > usual * 1.1).length >= 2; // a rise in 2 of 3 months, not a one-off
      return { category: c, recent: rec, usual, saving: rec - usual, steady };
    }).filter(x => x.steady && x.saving >= 50 && x.recent > x.usual * 1.1).sort((a, b) => b.saving - a.saving);
    // top merchants driving each category's rise
    for (const it of items) {
      const mr = query(db, `SELECT merchant,
          SUM(CASE WHEN month BETWEEN ? AND ? THEN amount ELSE 0 END)/3.0 rec,
          SUM(CASE WHEN month BETWEEN ? AND ? THEN amount ELSE 0 END)/? base
        FROM tx WHERE direction='expense' AND category=? GROUP BY merchant ORDER BY rec-base DESC LIMIT 2`,
        [recent[0], recent[2], baseAvail[baseAvail.length - 1], baseAvail[0], baseAvail.length, it.category]).rows;
      it.drivers = mr.filter(r => r[1] - r[2] > 20).map(r => ({ merchant: r[0], recent: r[1], usual: r[2] }));
    }
    return { items, window: { recent, base: baseAvail } };
  }

  // ---------------------------------------------------------------- question answering (rules → SQL)
  const NUMWORDS = { one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9, ten: 10, twelve: 12 };
  const CAT_Q = [
    [/\b(eating out|eat out|restaurants?|dining|dine|food|takeaway|take-away|cafes?|coffee)\b|أكل|اكل|مطاعم|مطعم|قهوة/, 'Food_Dining'],
    [/\b(groceries|grocery|supermarkets?)\b|بقالة|سوبرماركت|مقاضي/, 'Groceries'],
    [/\b(transport|transportation|commute|car|cars|auto|driving)\b|مواصلات|سيارة/, 'Transport_Auto'],
    [/\b(shopping|shop|retail|clothes|electronics)\b|تسوق/, 'Shopping_Retail'],
    [/\b(utilities|utility|bills?|telecom|phone|mobile|internet|electricity|water)\b|فواتير|كهرباء/, 'Utilities_Telecom'],
    [/\b(health|healthcare|medical|pharmacy|pharmacies|doctors?|gym|fitness|wellness)\b|صيدلية|صحة/, 'Health_Wellness'],
    [/\b(travel|travelling|traveling|trips?|flights?|hotels?|holidays?|vacations?)\b|سفر/, 'Travel'],
    [/\b(entertainment|fun|cinema|movies?|games?|gaming|leisure)\b|ترفيه|سينما/, 'Entertainment'],
    [/\b(government|govt|fees|fines?|visas?)\b|رسوم|مخالفات/, 'Government_Fees'],
    [/\b(housing|rent|education|school|tuition|university)\b|إيجار|ايجار|مدرسة/, 'Housing_Education'],
    [/\b(subscriptions?|digital|streaming|apps?|software)\b|اشتراكات|اشتراك/, 'Digital_Subscriptions'],
    [/\b(others?|misc|miscellaneous)\b/, 'Others']
  ];
  const GROUPS = [
    [/\b(food delivery|delivery apps?|deliveries|delivery|ordering in|order(ed)? in)\b|توصيل/, 'food delivery', ['talabat', 'deliveroo', 'noon food', 'careem food', 'zomato', 'eateasy', 'eat easy', 'smiles']],
    [/\b(taxis?|cabs?|rides?|ride-hailing|ride hailing)\b|تاكسي/, 'taxis & rides', ['careem', 'uber', 'hala', 'taxi', 'cab']],
    [/\b(fuel|petrol|gas station)\b|بنزين/, 'fuel', ['enoc', 'adnoc', 'emarat', 'eppco', 'petrol', 'fuel']],
    [/\b(tolls?|salik)\b/, 'Salik tolls', ['salik', 'darb']],
    [/\b(coffee|coffees)\b/, 'coffee', ['starbucks', 'costa', 'tim hortons', 'coffee', 'cafe']]
  ];
  const MONTH_RE = '(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sept|sep|oct|nov|dec)';

  function extractPeriods(q, anchor) {
    const A = anchor.slice(0, 7), Ay = +anchor.slice(0, 4);
    const found = [];
    const add = (re, f) => { q = q.replace(re, (...m) => { const p = f(...m); if (p) found.push({ ...p, at: m[m.length - 2] }); return ' '.repeat(m[0].length); }); };
    const month = ym => ({ start: ym + '-01', end: monthEnd(ym), label: monthLabel(ym), kind: 'month', ym });
    const year = y => ({ start: `${y}-01-01`, end: `${y}-12-31`, label: String(y), kind: 'year', y });
    add(/\b(this|current) month\b|الشهر (ده|هذا|الحالي)/g, () => month(A));
    add(/\b(last|previous|past|prior) month\b|الشهر (اللي|الي) (طاف|فات)|الشهر الماضي/g, () => month(addMonths(A, -1)));
    add(/\b(the )?month before( last)?\b/g, () => month(addMonths(A, -2)));
    add(/\b(so far )?this year\b|\byear to date\b|\bytd\b|هذه السنة|السنة دي/g, () => ({ start: `${Ay}-01-01`, end: anchor, label: `${Ay} so far`, kind: 'ytd', y: Ay }));
    add(/\b(last|previous|past) year\b|السنة (اللي|الي) (طافت|فاتت)|السنة الماضية/g, () => year(Ay - 1));
    add(/\b(?:in the |over the |during the )?(last|past|previous) (\d+|one|two|three|four|five|six|seven|eight|nine|ten|twelve) months\b/g, (_, __, n) => {
      const k = NUMWORDS[n] || +n; const s = addMonths(A, -(k - 1));
      return { start: s + '-01', end: anchor, label: `the last ${k} months (${monthShort(s)} – ${monthShort(A)})`, kind: 'range', months: k };
    });
    add(/\b(last|past) (\d+|one|two|three|four|five|six|seven|eight|nine|ten) weeks\b/g, (_, __, n) => { const k = NUMWORDS[n] || +n; return { start: addDays(anchor, -7 * k + 1), end: anchor, label: `the last ${k} weeks`, kind: 'range' }; });
    add(/\b(last|past|this) week\b/g, () => ({ start: addDays(anchor, -6), end: anchor, label: 'the last 7 days', kind: 'range' }));
    add(/\b(last|past) (\d+) days\b/g, (_, __, n) => ({ start: addDays(anchor, -(+n) + 1), end: anchor, label: `the last ${n} days`, kind: 'range' }));
    add(/\bsince (?:the start of |the beginning of )?(\d{4})\b/g, (_, y) => ({ start: `${y}-01-01`, end: anchor, label: `since ${y}`, kind: 'range' }));
    add(new RegExp(`\\bsince ${MONTH_RE}(?:\\s+(\\d{4}))?\\b`, 'g'), (_, mn, y) => {
      const mm = monKey(mn); let yy = y ? +y : Ay; if (!y && `${yy}-${pad(mm)}` > A) yy--;
      return { start: `${yy}-${pad(mm)}-01`, end: anchor, label: `since ${monthLabel(`${yy}-${pad(mm)}`)}`, kind: 'range' };
    });
    add(new RegExp(`\\b${MONTH_RE}(?:\\s+(\\d{4}))?\\b`, 'g'), (w, mn, y) => {
      if (mn === 'may' && !y && !/\b(in|of|during|for|vs|versus|and|than|from) may\b/.test(q)) return null; // "may" as a verb
      const mm = monKey(mn); let yy = y ? +y : Ay; if (!y && `${yy}-${pad(mm)}` > A) yy--;
      return month(`${yy}-${pad(mm)}`);
    });
    add(/\b(?:in |during |for )?(20[1-3]\d)\b/g, (_, y) => year(+y));
    found.sort((a, b) => a.at - b.at);
    return { periods: found, rest: q };
  }

  function findMerchant(q, merchants) {
    const ql = ' ' + q.toLowerCase().replace(/[^\p{L}\p{N}&.' ]+/gu, ' ') + ' ';
    const sorted = [...merchants].sort((a, b) => b.length - a.length);
    for (const m of sorted) {
      const ml = m.toLowerCase(); if (ml.length < 3) continue;
      if (ql.includes(' ' + ml + ' ') || ql.includes(' ' + ml + "'s ") || ql.includes(' ' + ml + 's ')) return m;
    }
    const STOP = new Set(['payment', 'transfer', 'store', 'online', 'services', 'service', 'market', 'trading', 'restaurant', 'cafe', 'coffee', 'food', 'the', 'and', 'company', 'group', 'center', 'centre', 'shop', 'unknown', 'others', 'month', 'months', 'spend', 'spent']);
    const firstTok = {};
    for (const m of merchants) { const t = m.toLowerCase().split(/\s+/)[0]; if (t.length >= 5 && !STOP.has(t)) (firstTok[t] = firstTok[t] || []).push(m); }
    for (const [t, ms] of Object.entries(firstTok)) if (ms.length === 1 && ql.includes(' ' + t + ' ')) return ms[0];
    return null;
  }

  function parseQuestion(question, ctx) {
    const raw = String(question || '').trim();
    let q = ' ' + raw.toLowerCase().replace(/[?؟!]/g, ' ').replace(/\s+/g, ' ') + ' ';
    const { periods, rest } = extractPeriods(q, ctx.anchor);
    q = rest;
    const has = re => re.test(q);
    const nMatch = q.match(/\btop (\d+|one|two|three|four|five|six|seven|eight|nine|ten)\b|\b(\d+|three|four|five|six|seven|eight|nine|ten) (places|merchants|shops|stores|purchases|transactions|biggest|largest|things)\b/);
    const topN = nMatch ? (NUMWORDS[nMatch[1] || nMatch[2]] || +(nMatch[1] || nMatch[2])) : null;

    // target filter
    let merchant = findMerchant(q, ctx.merchants || []);
    let group = null, category = null, userCat = null;
    if (!merchant) for (const [re, name, kws] of GROUPS) if (re.test(q)) { group = { name, kws }; break; }
    if (!merchant && !group) {
      // user's own category names first (file categories)
      for (const c of (ctx.categories || [])) { const cl = c.toLowerCase().replace(/_/g, ' '); if (cl.length > 2 && q.includes(' ' + cl + ' ')) { userCat = c; break; } }
      if (!userCat) for (const [re, c] of CAT_Q) if (re.test(q)) { category = c; break; }
      if (category && ctx.categories && !ctx.categories.includes(category)) { // file uses its own names: find closest
        const alt = ctx.categories.find(c => mapUserCategory(c) === category); if (alt) userCat = alt; category = null;
        if (!alt) category = null;
      }
    }
    const filter = { merchant, group, category: userCat || category };

    // intent
    let intent = 'total';
    const ql = ' ' + raw.toLowerCase() + ' ';
    const goal = ql.match(/\bsave\s+(?:aed\s*)?([\d,.]+)\s*(k|thousand)?\s*(?:aed|dirhams?|dhs)?/) || ql.match(/\b(?:aed\s*)?([\d,.]+)\s*(k|thousand)?\s*(?:aed|dirhams?|dhs)?\s+(?:saved|in savings)/);
    if (goal || has(/\bsavings? goal\b/)) intent = 'goal';
    else if (has(/\b(subscriptions|recurring|every month|monthly payments|regular payments|direct debits?|standing orders?|paying for)\b|اشتراكاتي|بدفع كل شهر/) && !has(/\bhow much\b.*\bon subscriptions\b/)) intent = 'recurring';
    else if (has(/\b(compare|comparison|vs|versus|difference|more than|less than|why did i spend|why is my|why was my|increase|went up|go up|change)\b/) || periods.length >= 2) intent = 'compare';
    else if (has(/\b(biggest|largest|most expensive|highest|top) (purchases?|transactions?|expenses?|payments?|spends?|items?)\b|\bbiggest purchase\b/)) intent = 'topTx';
    else if (has(/\b(spen[dt]|spending) (the )?most( money)? on\b|\bbiggest (spending )?categor/) && !filter.merchant && !filter.group && !filter.category) intent = 'byCategory';
    else if (has(/\b(top|most|where do i spend|where did i spend|which (merchants?|places|shops|stores)|favourite|favorite|biggest merchants?)\b/) && !filter.merchant) intent = 'topMerchants';
    else if (has(/\b(how many times|how often|how many (orders|transactions|purchases|visits))\b|كم مرة/)) intent = 'count';
    else if (has(/\b(per (order|purchase|transaction|visit)|each time|average (order|purchase|transaction|ticket|basket))\b/) || (has(/\b(average|avg|typical)\b/) && has(/\b(order|purchase|transaction|visit|basket|ticket|bill|ride|trip)\b/))) intent = 'avgTx';
    else if (has(/\b(spen[dt]|spending) (the )?most( money)? on\b|\bbiggest (spending )?categor/) && !filter.merchant && !filter.group && !filter.category) intent = 'byCategory';
    else if (has(/\b(average|avg|on average|typical|typically|usually|normally|per month|a month|each month|monthly)\b|متوسط|في الشهر/)) intent = (has(/\b(by month|each month|month by month|per month breakdown|monthly breakdown|every month)\b/) && !has(/\baverage\b/)) ? 'byMonth' : 'avgMonth';
    else if (has(/\b(breakdown|by category|categories|what did i spend (money )?on|what do i spend (money )?on|split)\b/) && !filter.category && !filter.merchant && !filter.group) intent = 'byCategory';
    else if (has(/\b(by month|each month|month by month|trend|over time)\b/)) intent = 'byMonth';
    else if (has(/\b(income|earn|earned|salary|received|got paid|paid in)\b|راتب|دخل/)) intent = 'income';
    else if (has(/\b(balance|net|left over|saved|savings)\b/)) intent = 'net';
    else if (has(/\b(how much|spend|spent|spending|cost|pay|paid|total|expenses?)\b|كم|صرفت|دفعت/) || filter.merchant || filter.group || filter.category) intent = 'total';
    else intent = 'unknown';

    let goalAmt = null, goalBy = null;
    if (intent === 'goal' && goal) {
      goalAmt = parseFloat(goal[1].replace(/,/g, '')) * (goal[2] ? 1000 : 1);
      const by = (' ' + raw.toLowerCase() + ' ').match(new RegExp(`\\b(?:by|before|until|in) (?:end of |the end of )?${MONTH_RE}(?:\\s+(\\d{4}))?\\b`));
      if (by) { const mm = monKey(by[1]); let yy = by[2] ? +by[2] : +ctx.anchor.slice(0, 4); if (!by[2] && `${yy}-${pad(mm)}` <= ctx.anchor.slice(0, 7)) yy++; goalBy = `${yy}-${pad(mm)}`; }
      const inN = raw.toLowerCase().match(/\bin (\d+|one|two|three|four|five|six|seven|eight|nine|ten|twelve) months\b/);
      if (!goalBy && inN) goalBy = addMonths(ctx.anchor.slice(0, 7), NUMWORDS[inN[1]] || +inN[1]);
      if (!goalBy && periods.length) goalBy = periods[periods.length - 1].end.slice(0, 7);
    }
    return { intent, periods, filter, topN, goalAmt, goalBy };
  }

  function filterSQL(filter, period) {
    const w = ["direction='expense'"], p = [];
    if (period) { w.push('date BETWEEN ? AND ?'); p.push(period.start, period.end); }
    if (filter.merchant) { w.push('merchant = ?'); p.push(filter.merchant); }
    else if (filter.group) { w.push('(' + filter.group.kws.map(() => "lower(merchant || ' ' || description) LIKE ?").join(' OR ') + ')'); filter.group.kws.forEach(k => p.push('%' + k + '%')); }
    else if (filter.category) { w.push('category = ?'); p.push(filter.category); }
    return { where: w.join(' AND '), params: p };
  }
  function filterLabel(filter) {
    if (filter.merchant) return 'at ' + filter.merchant;
    if (filter.group) return 'on ' + filter.group.name;
    if (filter.category) return 'on ' + catName(filter.category);
    return '';
  }
  function inlineSQL(sql, params) {
    let i = 0; return sql.replace(/\?/g, () => { const v = params[i++]; return typeof v === 'number' ? String(v) : "'" + String(v).replace(/'/g, "''") + "'"; })
      .replace(/\s+\n/g, '\n');
  }
  function periodText(p) { return p ? (p.kind === 'month' || p.kind === 'year' ? 'in ' + p.label : p.label.startsWith('the ') || p.label.startsWith('since') ? (p.label.startsWith('since') ? p.label : 'in ' + p.label) : 'in ' + p.label) : 'across all your data'; }
  function prevPeriod(p, anchor) {
    if (p.kind === 'month') { const ym = addMonths(p.ym, -1); return { start: ym + '-01', end: monthEnd(ym), label: monthLabel(ym), kind: 'month', ym }; }
    if (p.kind === 'year' || p.kind === 'ytd') { const y = (p.y || +p.start.slice(0, 4)) - 1; return p.kind === 'ytd' ? { start: `${y}-01-01`, end: `${y}${anchor.slice(4)}`, label: `${y} to the same date`, kind: 'range' } : { start: `${y}-01-01`, end: `${y}-12-31`, label: String(y), kind: 'year', y }; }
    const days = Math.round((new Date(p.end) - new Date(p.start)) / 864e5) + 1;
    return { start: addDays(p.start, -days), end: addDays(p.start, -1), label: `the ${days} days before`, kind: 'range' };
  }
  function partialNote(p, anchor, firstDate) {
    const notes = [];
    if (p && p.end > anchor && p.start <= anchor) notes.push(`your data stops on ${fmtDate(anchor)}, so ${p.label} is incomplete`);
    if (p && p.start < firstDate && p.end >= firstDate) notes.push(`your data starts on ${fmtDate(firstDate)}`);
    if (p && (p.end < firstDate || p.start > anchor)) notes.push(`there is no data for ${p.label}`);
    return notes;
  }

  function answer(db, question, ctx) {
    const P = parseQuestion(question, ctx);
    const { filter } = P; const flabel = filterLabel(filter);
    const per = P.periods[0] || null;
    const out = { parsed: P, steps: [] };
    const run = (sql, params) => { out.steps.push(inlineSQL(sql, params)); return query(db, sql, params); };
    const notes = per ? partialNote(per, ctx.anchor, ctx.first) : [];
    const finish = (text, table) => ({ ...out, text, table, notes, sql: out.steps.join(';\n\n') + (out.steps.length ? ';' : '') });

    switch (P.intent) {
      case 'total': {
        const f = filterSQL(filter, per);
        const r = run(`SELECT ROUND(SUM(amount),2) AS total, COUNT(*) AS transactions FROM tx WHERE ${f.where}`, f.params).rows[0];
        const tot = r[0] || 0, n = r[1];
        if (!n) return finish(`I found no spending ${flabel} ${periodText(per)}.`.replace(/\s+/g, ' '));
        return finish(`You spent **${aed(tot)}** ${flabel} ${periodText(per)} (${n} transaction${n === 1 ? '' : 's'}).`.replace(/\s+/g, ' '));
      }
      case 'count': {
        const f = filterSQL(filter, per);
        const r = run(`SELECT COUNT(*) AS transactions, ROUND(SUM(amount),2) AS total FROM tx WHERE ${f.where}`, f.params).rows[0];
        return finish(`${r[0]} transaction${r[0] === 1 ? '' : 's'} ${flabel} ${periodText(per)}, totalling ${aed(r[1] || 0)}.`.replace(/\s+/g, ' '));
      }
      case 'avgTx': {
        const f = filterSQL(filter, per);
        const r = run(`SELECT ROUND(AVG(amount),2) AS avg_per_transaction, COUNT(*) AS transactions FROM tx WHERE ${f.where}`, f.params).rows[0];
        if (!r[1]) return finish(`I found no spending ${flabel} ${periodText(per)}.`);
        return finish(`Each transaction ${flabel} averages **${aed(r[0])}** ${periodText(per)} (${r[1]} transactions).`.replace(/\s+/g, ' '));
      }
      case 'avgMonth': {
        const p = per || { start: ctx.first, end: ctx.anchor, label: 'all your data', kind: 'all' };
        const s = p.start < ctx.first ? ctx.first : p.start, e = p.end > ctx.anchor ? ctx.anchor : p.end;
        const nM = Math.max(1, monthsBetween(s.slice(0, 7), e.slice(0, 7)) + 1);
        const f = filterSQL(filter, { start: s, end: e });
        const r = run(`SELECT ROUND(SUM(amount)/${nM}.0,2) AS avg_per_month, ROUND(SUM(amount),2) AS total, COUNT(*) AS transactions FROM tx WHERE ${f.where}`, f.params).rows[0];
        return finish(`On average you spend **${aed(r[0] || 0)} a month** ${flabel} — ${aed(r[1] || 0)} over ${nM} month${nM === 1 ? '' : 's'} (${monthShort(s.slice(0, 7))} – ${monthShort(e.slice(0, 7))}). Months with no spending count as zero.`.replace(/\s+/g, ' '));
      }
      case 'byMonth': {
        const f = filterSQL(filter, per);
        const t = run(`SELECT month, ROUND(SUM(amount),2) AS total, COUNT(*) AS transactions FROM tx WHERE ${f.where} GROUP BY month ORDER BY month`, f.params);
        if (!t.rows.length) return finish(`I found no spending ${flabel} ${periodText(per)}.`);
        const hi = t.rows.reduce((a, r) => r[1] > a[1] ? r : a), lo = t.rows.reduce((a, r) => r[1] < a[1] ? r : a);
        return finish(`Month by month ${flabel}: highest was ${monthLabel(hi[0])} (${aed(hi[1])}), lowest ${monthLabel(lo[0])} (${aed(lo[1])}).`.replace(/\s+/g, ' '), t);
      }
      case 'byCategory': {
        const f = filterSQL(filter, per);
        const t = run(`SELECT category, ROUND(SUM(amount),2) AS total, COUNT(*) AS transactions FROM tx WHERE ${f.where} GROUP BY category ORDER BY total DESC`, f.params);
        const tot = t.rows.reduce((a, r) => a + r[1], 0);
        if (!t.rows.length) return finish(`I found no spending ${periodText(per)}.`);
        t.rows = t.rows.map(r => [catName(r[0]), r[1], r[2]]);
        return finish(`You spent ${aed(tot)} ${periodText(per)}. The biggest category was ${t.rows[0][0]} at ${aed(t.rows[0][1])} (${Math.round(100 * t.rows[0][1] / tot)}%).`, t);
      }
      case 'topMerchants': {
        const n = P.topN || 5; const f = filterSQL(filter, per);
        const t = run(`SELECT merchant, ROUND(SUM(amount),2) AS total, COUNT(*) AS transactions FROM tx WHERE ${f.where} GROUP BY merchant ORDER BY total DESC LIMIT ${n}`, f.params);
        if (!t.rows.length) return finish(`I found no spending ${flabel} ${periodText(per)}.`);
        return finish(`Your top ${t.rows.length} merchant${t.rows.length === 1 ? '' : 's'} ${flabel} ${periodText(per)}: ${t.rows.map(r => `${r[0]} (${aed(r[1])})`).join(', ')}.`.replace(/\s+/g, ' '), t);
      }
      case 'topTx': {
        const n = P.topN || 5; const f = filterSQL(filter, per);
        const t = run(`SELECT date, merchant, category, amount FROM tx WHERE ${f.where} ORDER BY amount DESC LIMIT ${n}`, f.params);
        if (!t.rows.length) return finish(`I found no spending ${flabel} ${periodText(per)}.`);
        t.rows = t.rows.map(r => [r[0], r[1], catName(r[2]), r[3]]);
        return finish(`Your biggest purchase ${flabel} ${periodText(per)} was **${aed(t.rows[0][3])}** at ${t.rows[0][1]} on ${fmtDate(t.rows[0][0])}.`.replace(/\s+/g, ' '), t);
      }
      case 'income': {
        const w = ["direction='income'"], p = []; if (per) { w.push('date BETWEEN ? AND ?'); p.push(per.start, per.end); }
        const r = run(`SELECT ROUND(SUM(amount),2) AS income, COUNT(*) AS transactions FROM tx WHERE ${w.join(' AND ')}`, p).rows[0];
        if (!r[1]) return finish(`Your file has no money coming in ${periodText(per)}, so I can't answer questions about income.`);
        return finish(`Money received ${periodText(per)}: **${aed(r[0])}** (${r[1]} credits).`);
      }
      case 'net': {
        const w = [], p = []; if (per) { w.push('date BETWEEN ? AND ?'); p.push(per.start, per.end); }
        const r = run(`SELECT ROUND(SUM(CASE WHEN direction='income' THEN amount ELSE 0 END),2) AS money_in, ROUND(SUM(CASE WHEN direction='expense' THEN amount ELSE 0 END),2) AS money_out FROM tx ${w.length ? 'WHERE ' + w.join(' AND ') : ''}`, p).rows[0];
        if (!r[0]) return finish(`Your file has no money coming in, so I can only tell you what went out: ${aed(r[1] || 0)} ${periodText(per)}.`);
        return finish(`${periodText(per)[0].toUpperCase() + periodText(per).slice(1)}: ${aed(r[0])} in, ${aed(r[1])} out — net **${aed(r[0] - r[1])}**.`);
      }
      case 'recurring': {
        const rec = recurring(db).filter(x => x.active);
        out.steps.push(`-- recurring = same merchant in ≥3 months, at most 2 charges a month, amounts within ±15% of the median, seen in the last 45 days
SELECT merchant, category, month, SUM(amount) AS total, COUNT(*) AS charges, MAX(date) AS last_charge
FROM tx WHERE direction='expense' GROUP BY merchant, month`);
        if (!rec.length) return finish(`I couldn't find any active recurring payments (same merchant, similar amount, most months).`);
        const t = { cols: ['merchant', 'category', 'typical / month', 'months seen', 'last charge'], rows: rec.map(x => [x.merchant, catName(x.category), Math.round(x.typical * 100) / 100, x.months, x.last]) };
        const sum = rec.reduce((a, x) => a + x.typical, 0);
        return finish(`You have **${rec.length} active recurring payments** adding up to about ${aed(sum)} a month (${aed(sum * 12)} a year).`, t);
      }
      case 'compare': {
        let a, b;
        if (P.periods.length >= 2) { [a, b] = [P.periods[0], P.periods[1]]; if (a.start > b.start) [a, b] = [b, a]; }
        else if (P.periods.length === 1) { b = P.periods[0]; a = prevPeriod(b, ctx.anchor); }
        else { const lm = addMonths(ctx.anchor.slice(0, 7), -1); b = { start: lm + '-01', end: monthEnd(lm), label: monthLabel(lm), kind: 'month', ym: lm }; a = prevPeriod(b, ctx.anchor); }
        const fa = filterSQL(filter, a), fb = filterSQL(filter, b);
        const ta = run(`SELECT ROUND(SUM(amount),2) FROM tx WHERE ${fa.where}`, fa.params).rows[0][0] || 0;
        const tb = run(`SELECT ROUND(SUM(amount),2) FROM tx WHERE ${fb.where}`, fb.params).rows[0][0] || 0;
        const groupCol = filter.merchant ? null : (filter.category || filter.group ? 'merchant' : 'category');
        let t = null, drivers = '';
        if (groupCol) {
          const f0 = filterSQL(filter, null);
          const sql = `SELECT ${groupCol},
  ROUND(SUM(CASE WHEN date BETWEEN ? AND ? THEN amount ELSE 0 END),2) AS before,
  ROUND(SUM(CASE WHEN date BETWEEN ? AND ? THEN amount ELSE 0 END),2) AS after,
  ROUND(SUM(CASE WHEN date BETWEEN ? AND ? THEN amount ELSE 0 END) - SUM(CASE WHEN date BETWEEN ? AND ? THEN amount ELSE 0 END),2) AS change
FROM tx WHERE ${f0.where} GROUP BY ${groupCol} HAVING before > 0 OR after > 0 ORDER BY ABS(change) DESC LIMIT 6`;
          t = run(sql, [a.start, a.end, b.start, b.end, b.start, b.end, a.start, a.end, ...f0.params]);
          t.cols = [groupCol, a.label, b.label, 'change'];
          const diff = tb - ta;
          const movers = t.rows.filter(r => Math.sign(r[3]) === Math.sign(diff) && Math.abs(r[3]) > 0).slice(0, 3);
          if (groupCol === 'category') t.rows = t.rows.map(r => [catName(r[0]), r[1], r[2], r[3]]);
          if (movers.length && Math.abs(diff) > 0) drivers = ` The biggest ${diff > 0 ? 'increases' : 'drops'}: ${movers.map(r => `${groupCol === 'category' ? catName(r[0]) : r[0]} (${r[3] > 0 ? '+' : ''}${aed(r[3])})`).join(', ')}.`;
        }
        const diff = tb - ta, pct = ta ? Math.round(100 * diff / ta) : null;
        notes.push(...partialNote(a, ctx.anchor, ctx.first), ...partialNote(b, ctx.anchor, ctx.first));
        const dir = diff > 0 ? 'more' : 'less';
        return finish(`You spent ${aed(tb)} ${flabel} in ${b.label} vs ${aed(ta)} in ${a.label}: **${aed(Math.abs(diff))} ${dir}**${pct != null ? ` (${diff > 0 ? '+' : ''}${pct}%)` : ''}.${drivers}`.replace(/\s+/g, ' '), t);
      }
      case 'goal': {
        if (!P.goalAmt) return finish('Tell me the amount and the date, e.g. "If I want to save AED 20,000 by June, how much do I need to cut?"');
        const startYM = ctx.anchor.slice(0, 7);
        const target = P.goalBy || addMonths(startYM, 6);
        const nM = Math.max(1, monthsBetween(startYM, target));
        const need = P.goalAmt / nM;
        const s6 = addMonths(startYM, -6) + '-01';
        const r = run(`SELECT ROUND(SUM(CASE WHEN direction='income' THEN amount ELSE 0 END)/6.0,2) AS income_per_month,
  ROUND(SUM(CASE WHEN direction='expense' THEN amount ELSE 0 END)/6.0,2) AS spend_per_month
FROM tx WHERE date >= ? AND date < ?`, [s6, startYM + '-01']).rows[0];
        const disc = run(`SELECT category, ROUND(SUM(amount)/6.0,2) AS per_month FROM tx WHERE direction='expense' AND date >= ? AND date < ? GROUP BY category ORDER BY per_month DESC`, [s6, startYM + '-01']);
        const discRows = disc.rows.filter(x => DISCRETIONARY.has(mapUserCategory(x[0])));
        const discTotal = discRows.reduce((a, x) => a + x[1], 0);
        const inc = r[0] || 0, spend = r[1] || 0, surplus = inc - spend;
        let text = `To save ${aed(P.goalAmt)} by the end of ${monthLabel(addMonths(target, 0))} you need to put aside **${aed(need)} a month** for ${nM} month${nM === 1 ? '' : 's'}. `;
        if (inc > 0) {
          if (surplus >= need) text += `Over the last 6 months you had ${aed(surplus)} a month left after spending (${aed(inc)} in, ${aed(spend)} out), so you're on track without cutting anything.`;
          else { const gap = need - Math.max(0, surplus); text += `Over the last 6 months you had ${aed(Math.max(0, surplus))} a month left over (${aed(inc)} in, ${aed(spend)} out), so you need to cut about **${aed(gap)} a month**` + (discTotal > 0 ? ` — that's ${Math.round(100 * gap / discTotal)}% of your ${aed(discTotal)}/month discretionary spending.` : '.'); }
        } else {
          text += `Your file has no income rows, so I can't see what's left over each month. Your discretionary spending averages ${aed(discTotal)} a month` + (discTotal ? `; covering the goal from that alone would mean cutting ${Math.round(100 * need / discTotal)}% of it.` : '.');
        }
        const t = { cols: ['discretionary category', 'avg / month (last 6 mo)', `cut needed (same % each)`], rows: [] };
        const gap = inc > 0 ? Math.max(0, need - Math.max(0, surplus)) : need;
        if (discTotal > 0 && gap > 0) t.rows = discRows.map(x => [catName(x[0]), x[1], Math.round(100 * Math.min(x[1], x[1] * gap / discTotal)) / 100]);
        return finish(text, t.rows.length ? t : null);
      }
      default:
        return finish(null);
    }
  }

  // ---------------------------------------------------------------- LLM text-to-SQL helpers
  function guardSQL(sql) {
    let s = String(sql || '').trim().replace(/;+\s*$/, '');
    if (!s) throw new Error('The model returned no SQL.');
    if (/;/.test(s.replace(/'[^']*'/g, ''))) throw new Error('Only one statement is allowed.');
    if (!/^(select|with)\b/i.test(s)) throw new Error('Only SELECT queries are allowed.');
    if (/\b(insert|update|delete|drop|alter|create|attach|detach|pragma|replace|vacuum|reindex|load_extension)\b/i.test(s.replace(/'[^']*'/g, ''))) throw new Error('That query tries to change the data, so it was blocked.');
    return s;
  }
  function extractSQL(text) {
    const t = String(text || '');
    let m = t.match(/```(?:sql|sqlite)?\s*([\s\S]*?)```/i);
    let s = m ? m[1] : t;
    const k = s.search(/\b(with|select)\b/i); if (k > 0) s = s.slice(k);
    const semi = s.indexOf(';'); if (semi >= 0) s = s.slice(0, semi);
    return s.trim();
  }
  function llmPrompt(ctx) {
    const cats = ctx.categories.join(', ');
    const mer = (ctx.topMerchantNames || []).slice(0, 40).join(', ');
    return `You write ONE SQLite query that answers a question about the user's bank transactions.

Table:
${SCHEMA}

Rules:
- Spending means direction='expense'. Money received means direction='income'. Ignore 'transfer' and 'refund' rows.
- amount is always positive (AED). Never invent numbers; compute them in SQL.
- Today is ${ctx.anchor} (the last date in the data). "This month" = strftime('%Y-%m', date) = '${ctx.anchor.slice(0, 7)}'. "Last month" = '${addMonths(ctx.anchor.slice(0, 7), -1)}'.
- Use the month column for month filters and the date column for ranges.
- category values are exactly: ${cats}.
- Filter merchants with merchant LIKE '%name%' (case-insensitive). Known merchants include: ${mer}.
- Average per month = SUM(amount) / number of months, not AVG(amount).
- Return only the SQL, no explanation.`;
  }
  const LLM_SHOTS = [
    ['How much did I spend on groceries last month?', a => `SELECT ROUND(SUM(amount),2) AS total FROM tx WHERE direction='expense' AND category='Groceries' AND month='${addMonths(a.slice(0, 7), -1)}'`],
    ['Top 3 merchants this year', a => `SELECT merchant, ROUND(SUM(amount),2) AS total FROM tx WHERE direction='expense' AND year=${a.slice(0, 4)} GROUP BY merchant ORDER BY total DESC LIMIT 3`],
    ['How many times did I use Careem in the last 3 months?', a => `SELECT COUNT(*) AS times FROM tx WHERE direction='expense' AND merchant LIKE '%careem%' AND month >= '${addMonths(a.slice(0, 7), -2)}'`]
  ];

  // ---------------------------------------------------------------- synthetic sample household
  function mulberry32(a) { return function () { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
  function sampleCSV() {
    const rnd = mulberry32(20261028);
    const ri = (a, b) => a + Math.floor(rnd() * (b - a + 1));
    const rf = (a, b) => Math.round((a + rnd() * (b - a)) * 100) / 100;
    const pick = a => a[Math.floor(rnd() * a.length)];
    const card = () => `${ri(4000, 4999)}XXXXXXXX${ri(1000, 9999)}`;
    const rows = [];
    const add = (y, m, d, desc, amt, acct) => rows.push([`${pad(d)}/${pad(m)}/${y}`, desc, amt.toFixed(2), acct || 'Current account']);
    const months = []; for (let k = 0; k < 12; k++) { const ym = addMonths('2025-10', k); months.push(ym.split('-').map(Number)); }
    const rest = ['ZAATAR W ZEIT', 'OPERATION FALAFEL', 'PF CHANGS', 'RAVI RESTAURANT', 'BIRYANI POT', 'THE BUTCHER SHOP AND GRILL', 'MAMA TANI CAFE', 'AL MALLAH CAFETERIA', 'SALT BURGER'];
    months.forEach(([y, m], k) => {
      const dim = new Date(Date.UTC(y, m, 0)).getUTCDate();
      const d = () => ri(1, dim), late = k >= 9; // last 3 months: more delivery
      add(y, m, 1, 'SALARY CREDIT ACME TECHNOLOGIES LLC', 21500);
      if ([10, 1, 4, 7].includes(m)) add(y, m, 2, 'CHQ 000' + ri(100, 999) + ' RENT PAYMENT AL BARSHA PROPERTIES', -24000);
      add(y, m, 3, 'TRANSFER TO OWN ACCOUNT SAVINGS', -2000);
      add(y, m, 8, 'DEWA BILL PAYMENT ' + ri(100000, 999999), -rf([6, 7, 8, 9].includes(m) ? 850 : 420, [6, 7, 8, 9].includes(m) ? 1150 : 560));
      add(y, m, 5, 'DU POSTPAID BILL PAYMENT', -349);
      add(y, m, 12, 'ETISALAT HOME INTERNET', -389);
      add(y, m, 14, `POS ${card()} NETFLIX.COM AMSTERDAM`, -56.99, 'Credit card');
      add(y, m, 17, `POS ${card()} SPOTIFY AB STOCKHOLM`, -21.99, 'Credit card');
      add(y, m, 19, `POS ${card()} APPLE.COM/BILL ITUNES.COM`, -11.99, 'Credit card');
      if (k >= 5) add(y, m, 21, `POS ${card()} OSN PLUS DUBAI AE`, -35, 'Credit card');
      add(y, m, 22, `POS ${card()} OPENAI *CHATGPT SUBSCR`, -73.45, 'Credit card');
      add(y, m, 4, 'GYMNATION AL QUOZ DUBAI', -199, 'Credit card');
      add(y, m, 20, 'CREDIT CARD PAYMENT - THANK YOU', -ri(3000, 6000));
      for (let i = 0; i < ri(1, 2); i++) add(y, m, d(), 'SALIK RECHARGE ONLINE', -100);
      for (let i = 0; i < ri(2, 4); i++) add(y, m, d(), `POS ${card()} ENOC ${pick(['1012', '1047', '2201'])} DUBAI AE`, -rf(110, 210), 'Credit card');
      for (let i = 0; i < ri(3, 8); i++) add(y, m, d(), `APPLE PAY CAREEM HALA RIDE DUBAI ARE`, -rf(16, 62), 'Credit card');
      for (let i = 0; i < ri(4, 6); i++) add(y, m, d(), `POS ${card()} CARREFOUR ${pick(['MOE', 'CITY CENTRE DEIRA', 'AL BARSHA'])} DUBAI`, -rf(140, 460), 'Credit card');
      for (let i = 0; i < ri(1, 3); i++) add(y, m, d(), `POS ${card()} SPINNEYS ${pick(['JUMEIRAH', 'MARINA'])} DUBAI AE`, -rf(70, 260), 'Credit card');
      if (rnd() < .6) add(y, m, d(), `LULU HYPERMARKET AL BARSHA`, -rf(90, 320), 'Credit card');
      for (let i = 0; i < ri(late ? 12 : 6, late ? 18 : 10); i++) add(y, m, d(), `POS ${card()} TALABAT.COM DUBAI AE`, -rf(35, 125), 'Credit card');
      for (let i = 0; i < ri(0, 3); i++) add(y, m, d(), `DELIVEROO DUBAI ARE ${ri(10000, 99999)}`, -rf(40, 110), 'Credit card');
      for (let i = 0; i < ri(0, 2); i++) add(y, m, d(), `NOON FOOD ${ri(1000000, 9999999)}`, -rf(30, 95), 'Credit card');
      for (let i = 0; i < ri(4, 8); i++) add(y, m, d(), `APPLE PAY STARBUCKS ${pick(['JBR', 'MOE', 'DIFC', 'DXB T3'])} DUBAI`, -rf(18, 38), 'Credit card');
      for (let i = 0; i < ri(2, 4); i++) add(y, m, d(), `POS ${card()} ${pick(rest)} DUBAI AE`, -rf(85, 420), 'Credit card');
      for (let i = 0; i < ri(2, 4); i++) add(y, m, d(), `POS ${card()} AMAZON.AE ${pick(['MARKETPLACE', 'RETAIL'])}`, -rf(45, 420), 'Credit card');
      for (let i = 0; i < ri(0, 2); i++) add(y, m, d(), `POS ${card()} NOON.COM DUBAI`, -rf(40, 380), 'Credit card');
      if (rnd() < .35) add(y, m, d(), `IKEA FESTIVAL CITY DUBAI`, -rf(150, 900), 'Credit card');
      if (m === 11) add(y, m, 27, `POS ${card()} SHARAF DG MALL OF EMIRATES`, -3299, 'Credit card');
      for (let i = 0; i < ri(1, 2); i++) add(y, m, d(), `LIFE PHARMACY ${ri(100, 999)} DUBAI AE`, -rf(25, 140), 'Credit card');
      if (rnd() < .2) add(y, m, d(), `ASTER CLINIC AL BARSHA`, -rf(250, 450), 'Credit card');
      for (let i = 0; i < ri(0, 2); i++) add(y, m, d(), `VOX CINEMAS MALL OF EMIRATES`, -rf(70, 160), 'Credit card');
      if (rnd() < .3) add(y, m, d(), `PLAYSTATION NETWORK`, -rf(60, 280), 'Credit card');
      if (rnd() < .4) add(y, m, d(), `ATM CASH WITHDRAWAL ${ri(1000, 9999)} DUBAI`, -500);
      if (rnd() < .25) add(y, m, d(), `DUBAI POLICE TRAFFIC FINE`, -pick([300, 400, 600]));
      if (m === 12) { add(y, m, 6, `POS ${card()} FLYDUBAI ONLINE`, -1850, 'Credit card'); add(y, m, 7, `POS ${card()} BOOKING.COM HOTEL`, -940, 'Credit card'); }
      if (m === 7) { add(y, m, 3, `POS ${card()} EMIRATES AIRLINE EMIRATES.COM`, -4250, 'Credit card'); add(y, m, 4, `AIRBNB * HM${ri(1000, 9999)}`, -2100, 'Credit card'); }
      if (m === 3) add(y, m, 18, `AMER CENTRE VISA RENEWAL FEES`, -1120);
      if (m === 10) add(y, m, 4, `EJARI REGISTRATION DLD`, -220);
      if (m === 2 || m === 9) add(y, m, 10, `UOWD TUITION FEE PAYMENT`, -14800);
      if (rnd() < .3) add(y, m, d(), `REFUND AMAZON.AE`, rf(40, 200), 'Credit card');
    });
    rows.sort((a, b) => a[0].split('/').reverse().join('').localeCompare(b[0].split('/').reverse().join('')));
    const esc = v => /[",\n]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v;
    return ['Date,Description,Amount,Account', ...rows.map(r => r.map(esc).join(','))].join('\n');
  }

  root.LedgerCore = {
    CATS, CAT_LABEL, DISCRETIONARY, SCHEMA, RULES, matchRule, cleanMerchant, mapUserCategory, parseCSV, detectDelimiter,
    parseDate, detectDateOrder, parseAmount, guessColumns, buildTransactions, buildDB, query, scalar, overview, monthlyByCategory,
    categoryTotals, topMerchants, recurring, cutSuggestions, parseQuestion, answer, guardSQL, extractSQL, llmPrompt, LLM_SHOTS,
    sampleCSV, aed, catName, monthLabel, monthShort, addMonths, fmtDate, inlineSQL, dataRange
  };
})(typeof window !== 'undefined' ? window : globalThis);
