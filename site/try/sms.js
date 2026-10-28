/* Ledger — raw bank SMS pipeline + expense categoriser, ported from the project notebooks.
   sms_transactions_pipeline.ipynb : parse_message, split_merchant, clean_name, expense flags
   expense_categoriser_train_test.ipynb : make_text, rules tier, TF-IDF + logistic regression, calibration, cascade
   Rule tables live in ledger-rules.js (generated from the notebook source, not retyped).
   Pure functions, no network access. Loadable in Node for tests (globalThis.LedgerSMS). */
(function (root) {
  'use strict';
  const T = root.LedgerRules;
  if (!T) throw new Error('ledger-rules.js must load before sms.js');

  // ------------------------------------------------------------ parser (cell 8)
  const rx = (src, f) => new RegExp(src, f || '');
  const COMMON = T.COMMON_RULES.map(([t, s, f]) => [t, rx(s, f)]);
  const BANKS = Object.fromEntries(Object.entries(T.BANK_RULES).map(([b, l]) => [b, l.map(([t, s, f]) => [t, rx(s, f)])]));
  const BALANCE = rx(T.BALANCE_RX[0], T.BALANCE_RX[1]);
  const BANK_NAMES = Object.keys(BANKS);

  function num(s) {
    if (s == null) return NaN;
    s = String(s).replace(/,/g, '').trim().replace(/\.+$/, '');
    if (!/^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$/.test(s)) return NaN;   // Python float() is strict
    return parseFloat(s);
  }

  function parseMessage(msg, bank) {
    const text = String(msg).replace(/\n/g, ' ').trim();
    const rules = COMMON.concat(BANKS[bank] || [], [['notice', /.*/s]]);
    for (const [type, re] of rules) {
      const m = re.exec(text);
      if (!m) continue;
      const g = m.groups || {};
      let balance = num(g.balance);
      if (isNaN(balance) && !['otp', 'declined', 'notice'].includes(type)) {
        const b = BALANCE.exec(text);
        balance = b ? num(b.groups.balance) : NaN;
      }
      const merchant = (g.merchant_raw || '').trim();
      return {
        txn_type: type, amount: num(g.amount), currency: (g.currency || '').toUpperCase() || null,
        card_last4: g.card || null, merchant_raw: merchant || null, balance_after: balance
      };
    }
  }

  // ------------------------------------------------------------ cleaning (cell 14)
  const UAE = T.UAE_CITIES;
  const stripChars = (s, chars) => { let a = 0, b = s.length; while (a < b && chars.includes(s[a])) a++; while (b > a && chars.includes(s[b - 1])) b--; return s.slice(a, b); };

  function splitMerchant(raw, bank) {
    if (typeof raw !== 'string' || !raw.trim()) return [null, null, null];
    const s = raw.replace(/\s+/g, ' ').trim();
    let m;
    if (bank === 'ADCB') {
      if ((m = /^(.*),\s*(.*?)-\s*([A-Z]{2})$/.exec(s))) return [m[1].trim(), m[2].trim() || null, m[3]];
      return [s, null, null];
    }
    if (bank === 'Liv') {
      const k = s.lastIndexOf(', ');
      if (k >= 0) return [s.slice(0, k).trim(), s.slice(k + 2).trim(), null];
      return [s, null, null];
    }
    if (bank === 'FAB') {
      m = /^(.*?)\s+([A-Z]{2})$/.exec(s);
      const [name, cc] = m ? [m[1].trim(), m[2]] : [s, null];
      const loc = /\s+((?:ABU ?DHABI|DUBAI|SHARJAH|AJMAN|AL AIN|RAS AL KHAIMAH|FUJAIRAH|RIYADH|JEDDAH|KARACHI|LAHORE|LONDON|CAIRO|[A-Z][a-z]+))$/i.exec(name);
      if (loc && loc.index > 2) return [name.slice(0, loc.index).trim(), loc[1], cc];
      return [name, null, cc];
    }
    if (bank === 'ADIB') {
      if ((m = /^(.*?) in (.*?), ?(UNITED ARAB EMI|UNITED STATES|.*)$/.exec(s)))
        return [m[1].trim(), m[2].trim() || null, m[3].includes('ARAB') ? 'AE' : null];
      if ((m = /^(.*), ?(UAE|UNITED STATES|IRELAND|.*)$/.exec(s)))
        return [m[1].trim(), null, m[2] === 'UAE' ? 'AE' : null];
      if ((m = new RegExp(`^(.*?)\\s+${UAE}?\\s*([A-Z]{2})$`).exec(s))) {
        const loc = new RegExp(`${UAE}\\s*[A-Z]{2}$`).exec(s);
        return [m[1].trim(), loc ? loc[0].slice(0, -2).trim() : null, m[2]];
      }
      return [s, null, null];
    }
    return [s, null, null];   // Mashreq: no location
  }

  const BRANDS = T.BRANDS.map(([s, n]) => [rx(s, 'i'), n]);
  const FUEL = new Set(T.FUEL_BRANDS);
  const FOOD_AT_STATION = rx(T.FOOD_AT_STATION, 'i');
  const TRANSFER_MERCHANTS = rx(T.TRANSFER_MERCHANTS, 'i');
  const BNPL_MERCHANTS = rx(T.BNPL_MERCHANTS, 'i');

  function cleanName(name) {
    if (typeof name !== 'string' || !name.trim()) return null;
    for (const [re, canon] of BRANDS) {
      if (re.test(name)) {
        if (FUEL.has(canon) && FOOD_AT_STATION.test(name)) continue;
        return canon;
      }
    }
    let s = name.replace(/^(?:SP|FAT|WL|TAP|MYF|SQ|SUMUP|NOMOD)\s*\*\s*/i, '');
    s = s.replace(/\+?\d[\d -]{5,}/g, ' ');
    s = s.replace(/\b\d+\b/g, ' ');
    s = s.replace(/[*#/]+/g, ' ');
    s = stripChars(s.replace(/\s+/g, ' '), ' -,.');
    return s.toUpperCase() || null;
  }

  const DEBIT = new Set(['purchase', 'bill_payment', 'cash_withdrawal', 'bank_fee', 'transfer_out', 'card_repayment', 'loan_repayment', 'internal_out', 'other_debit']);
  const CREDIT = new Set(['refund', 'transfer_in', 'income', 'internal_in', 'card_payment_received']);

  /* rows: [{date:'YYYY-MM-DD HH:MM', message, bank}] -> enriched rows (same columns as the notebook's df) */
  function processMessages(rows) {
    const out = rows.map((r, i) => {
      const p = parseMessage(r.message, r.bank);
      const [merchant, location, country] = splitMerchant(p.merchant_raw, r.bank);
      let merchant_clean = cleanName(merchant);
      let txn_type = p.txn_type;
      if ((txn_type === 'purchase' || txn_type === 'bill_payment') && merchant_clean == null) merchant_clean = 'UNKNOWN MERCHANT';
      if (txn_type === 'purchase' && TRANSFER_MERCHANTS.test(p.merchant_raw || '')) txn_type = 'transfer_out';
      const is_bnpl = txn_type === 'purchase' && BNPL_MERCHANTS.test(p.merchant_raw || '');
      const rate = p.currency != null ? T.AED_PER_UNIT[p.currency] : undefined;
      const amount_aed = rate != null && !isNaN(p.amount) ? p.amount * rate : NaN;
      const is_foreign = p.currency != null && (p.currency !== 'AED' || (country != null && country !== 'AE'));
      const direction = DEBIT.has(txn_type) ? 'debit' : CREDIT.has(txn_type) ? 'credit' : 'none';
      return { ...r, ...p, txn_type, merchant, location, country, merchant_clean, is_bnpl, amount_aed, is_foreign, direction, _i: i };
    });
    // duplicates: identical message from the same bank (first copy kept), in date order like the notebook
    out.sort((a, b) => (a.bank < b.bank ? -1 : a.bank > b.bank ? 1 : 0) || (a.date < b.date ? -1 : a.date > b.date ? 1 : 0) || a._i - b._i);
    const seen = new Set();
    for (const r of out) {
      const k = r.bank + '\u0001' + r.message;
      r.is_duplicate = seen.has(k); seen.add(k);
      r.is_expense = (r.txn_type === 'purchase' || r.txn_type === 'bill_payment') && !r.is_duplicate;
      r.is_borderline = ['refund', 'cash_withdrawal', 'bank_fee'].includes(r.txn_type) && !r.is_duplicate;
    }
    return out;
  }

  // Guess the bank of a batch of messages: the bank whose own rules (not OTP/notice) match most messages.
  function detectBank(messages) {
    const sample = messages.slice(0, 400);
    const score = {};
    for (const b of BANK_NAMES) {
      score[b] = 0;
      for (const m of sample) {
        const text = String(m).replace(/\n/g, ' ').trim();
        if (BANKS[b].some(([t, re]) => t !== 'notice' && re.test(text))) score[b]++;
      }
    }
    const best = BANK_NAMES.slice().sort((a, b) => score[b] - score[a])[0];
    return { bank: score[best] > 0 ? best : null, score };
  }
  const SENDER_BANK = [[/adcb/i, 'ADCB'], [/^liv\b|liv\.?$|\bliv\b/i, 'Liv'], [/mashreq|neo/i, 'Mashreq'], [/\bfab\b|fabbank|first ?abu/i, 'FAB'], [/adib/i, 'ADIB']];
  function bankFromSender(addr) { for (const [re, b] of SENDER_BANK) if (re.test(String(addr || ''))) return b; return null; }

  // ------------------------------------------------------------ categoriser (expense_categoriser_train_test.ipynb)
  function makeText(merchant) {
    let t = String(merchant == null ? '' : merchant).toUpperCase();
    t = t.replace(/\+?\d[\d -]{4,}/g, ' ');
    t = t.replace(/[^A-Z& ]/g, ' ');
    return t.replace(/\s+/g, ' ').trim();
  }

  // rules.py suggest()
  const KEYWORDS = T.KEYWORDS.map(([c, s]) => [c, rx(s, 'i')]);
  const CITY = rx(T.CITY, 'gi');
  const AMBIG = new Set(T.AMBIGUOUS);
  function suggest(merchantClean, raw) {
    if (Object.prototype.hasOwnProperty.call(T.OVERRIDES, merchantClean)) return [T.OVERRIDES[merchantClean], 'manual', 'high'];
    if (merchantClean === 'UNKNOWN MERCHANT') return ['Others', 'rule', 'low'];
    if (Object.prototype.hasOwnProperty.call(T.BRAND, merchantClean)) return [T.BRAND[merchantClean], 'brand', AMBIG.has(merchantClean) ? 'medium' : 'high'];
    const text = `${merchantClean} ${raw == null ? '' : raw}`.replace(CITY, ' ');
    for (const [cat, re] of KEYWORDS) if (re.test(text)) return [cat, 'keyword', 'medium'];
    return [null, null, null];
  }

  // TF-IDF (sklearn TfidfVectorizer: lowercase, sublinear_tf, l2) + StandardScaler + LogisticRegression
  function charWbGrams(doc, lo, hi) {
    const out = [];
    for (const w0 of doc.toLowerCase().replace(/\s\s+/g, ' ').split(/\s+/).filter(Boolean)) {
      const w = ' ' + w0 + ' ', L = w.length;
      for (let n = lo; n <= hi; n++) {
        let off = 0;
        out.push(w.slice(off, off + n));
        while (off + n < L) { off++; out.push(w.slice(off, off + n)); }
        if (off === 0) break;
      }
    }
    return out;
  }
  function wordGrams(doc, lo, hi) {
    const toks = doc.toLowerCase().match(/\b\w\w+\b/g) || [];
    const out = [];
    for (let n = lo; n <= hi; n++) for (let i = 0; i + n <= toks.length; i++) out.push(toks.slice(i, i + n).join(' '));
    return out;
  }
  function tfidf(grams, vec) {
    const counts = new Map();
    for (const g of grams) { const j = vec.index.get(g); if (j !== undefined) counts.set(j, (counts.get(j) || 0) + 1); }
    let norm = 0; const feats = [];
    for (const [j, c] of counts) { const v = (1 + Math.log(c)) * vec.idf[j]; feats.push([j, v]); norm += v * v; }
    norm = Math.sqrt(norm) || 1;
    return feats.map(([j, v]) => [j, v / norm]);
  }

  function loadModel(json) {
    const M = JSON.parse(typeof json === 'string' ? json : JSON.stringify(json));
    for (const k of ['char', 'word']) M[k].index = new Map(M[k].vocab.map((t, i) => [t, i]));
    M.nFeat = M.char.vocab.length + M.word.vocab.length + 1;
    M.order = M.categories.map(c => M.classes.indexOf(c));   // model class order -> CATS order
    return M;
  }

  // Probabilities in M.categories order.
  function predictProba(M, text, amountAed) {
    const xc = tfidf(charWbGrams(text, M.char.ngram[0], M.char.ngram[1]), M.char);
    const xw = tfidf(wordGrams(text, M.word.ngram[0], M.word.ngram[1]), M.word);
    const off = M.char.vocab.length;
    const la = Math.log1p(Math.max(0, isFinite(amountAed) ? amountAed : 0));
    const amt = (la - M.amount.mean) / M.amount.scale;
    const K = M.classes.length, z = new Array(K);
    for (let k = 0; k < K; k++) {
      const W = M.coef[k];
      let s = M.intercept[k] + W[M.nFeat - 1] * amt;
      for (const [j, v] of xc) s += W[j] * v;
      for (const [j, v] of xw) s += W[off + j] * v;
      z[k] = s;
    }
    let p;
    if (M.calibration) {           // sklearn _SigmoidCalibration per class, then normalise (CalibratedClassifierCV)
      p = z.map((f, k) => 1 / (1 + Math.exp(M.calibration.a[k] * f + M.calibration.b[k])));
      const s = p.reduce((a, b) => a + b, 0);
      p = s > 0 ? p.map(v => v / s) : p.map(() => 1 / K);
    } else {                       // plain multinomial softmax
      const mx = Math.max(...z); const e = z.map(v => Math.exp(v - mx)); const s = e.reduce((a, b) => a + b, 0);
      p = e.map(v => v / s);
    }
    return M.order.map(i => p[i]);
  }

  function spread(cats, cat, conf, base) {
    const k = cats.indexOf(cat);
    const other = base.slice(); other[k] = 0;
    const s = other.reduce((a, b) => a + b, 0);
    const out = s > 0 ? other.map(v => v / s * (1 - conf)) : other.map(() => (1 - conf) / (cats.length - 1));
    out[k] = conf;
    return out;
  }

  /* categorise_new(): lookup (your own corrections) -> rules -> calibrated model. First tier whose top score clears
     the threshold decides; otherwise the best guess is returned with needs_review = true. */
  function categorise(M, merchant, amountAed, lookup, threshold) {
    const cats = M.categories;
    const text = makeText(merchant);
    const model = predictProba(M, text, amountAed);
    const tiers = [];
    if (lookup && lookup.has(text)) { const [cat, c] = lookup.get(text); tiers.push(['your corrections', spread(cats, cat, c, model)]); }
    const [cat, src, rc] = suggest(text, merchant);
    if (cat) {
      const c = !(src === 'brand' && rc === 'medium') ? (T.RULE_CONF[src] ?? 0.8) : 0.70;
      tiers.push(['rules', spread(cats, cat, c, model)]);
    }
    tiers.push(['model', model]);
    const thr = threshold ?? M.review_threshold;
    let chosen = tiers.find(([, p]) => Math.max(...p) >= thr);
    const needs_review = !chosen;
    if (!chosen) chosen = tiers.reduce((a, t) => Math.max(...t[1]) > Math.max(...a[1]) ? t : a);
    const [by, p] = chosen;
    const idx = p.map((v, i) => i).sort((a, b) => p[b] - p[a]);
    return { text, category: cats[idx[0]], confidence: p[idx[0]], decided_by: by, needs_review,
      runner_up: cats[idx[1]], runner_up_conf: p[idx[1]], scores: p };
  }

  // ------------------------------------------------------------ readers
  // Excel/CSV rows -> [{date, message, sender}]; looks for the notebook's Date / Message (or SMS) columns.
  function rowsFromTable(header, rows) {
    const H = header.map(h => String(h || '').trim().toLowerCase());
    const di = H.findIndex(h => h.startsWith('date'));
    const mi = H.findIndex(h => h === 'message' || h === 'sms' || h === 'body' || h === 'text');
    const si = H.findIndex(h => ['sender', 'address', 'from', 'bank'].includes(h));
    if (di < 0 || mi < 0) return null;
    return rows.map(r => ({ date: r[di], message: String(r[mi] ?? '').trim(), sender: si >= 0 ? r[si] : null }))
      .filter(r => r.message && r.message !== 'nan');
  }
  // "SMS Backup & Restore" XML: <sms address="ADCB" date="1690000000000" body="..." type="1" .../>
  function rowsFromSmsXml(xmlText, DOMParserImpl) {
    const doc = new (DOMParserImpl || root.DOMParser)().parseFromString(xmlText, 'text/xml');
    return [...doc.getElementsByTagName('sms')].filter(n => n.getAttribute('type') !== '2')
      .map(n => ({ date: new Date(+n.getAttribute('date')), message: (n.getAttribute('body') || '').trim(), sender: n.getAttribute('address') }))
      .filter(r => r.message);
  }

  function toISO(d) {
    if (d instanceof Date && !isNaN(d)) {
      const p = n => String(n).padStart(2, '0');
      return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())} ${p(d.getHours())}:${p(d.getMinutes())}`;
    }
    if (typeof d === 'number' && d > 30000 && d < 60000) {     // Excel serial
      const t = new Date(Date.UTC(1899, 11, 30) + Math.round(d * 864e5));
      return t.toISOString().slice(0, 16).replace('T', ' ');
    }
    const s = String(d || '').trim();
    let m;
    if ((m = s.match(/^(\d{4})-(\d{2})-(\d{2})(?:[ T](\d{1,2}):(\d{2}))?/))) return `${m[1]}-${m[2]}-${m[3]} ${(m[4] || '00').padStart(2, '0')}:${m[5] || '00'}`;
    if ((m = s.match(/^(\d{1,2})[/.-](\d{1,2})[/.-](\d{4})(?:[ ,]+(\d{1,2}):(\d{2}))?/))) {   // day first (UAE)
      const p = n => String(n).padStart(2, '0');
      return `${m[3]}-${p(m[2])}-${p(m[1])} ${p(m[4] || 0)}:${m[5] || '00'}`;
    }
    const t = new Date(s);
    return isNaN(t) ? null : toISO(t);
  }

  // Mask long digit runs (cards, accounts, references) for display only; the parser already ran on the original.
  function maskForDisplay(msg) {
    return String(msg).replace(/\b(\d{2})\d{4,}(\d{2})\b/g, '$1••••$2').replace(/\b[\w.+-]+@[\w-]+\.[\w.]+\b/g, '•••@•••');
  }

  root.LedgerSMS = { BANK_NAMES, parseMessage, splitMerchant, cleanName, processMessages, detectBank, bankFromSender,
    makeText, suggest, charWbGrams, wordGrams, loadModel, predictProba, categorise, rowsFromTable, rowsFromSmsXml, toISO,
    maskForDisplay, CATEGORY_DESCRIPTIONS: T.CATEGORIES };
})(typeof window !== 'undefined' ? window : globalThis);
