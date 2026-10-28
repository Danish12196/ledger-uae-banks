"""Shared helpers for the expense categoriser notebooks.

Kept in one place so the train/test notebook and the spending-assistant notebook
build features and models in exactly the same way.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.preprocessing import StandardScaler

FEATURES = ['text', 'log_amount']


def make_text(df):
    """Merchant text as the bank wrote it, minus phone/reference numbers and punctuation."""
    t = df.merchant.fillna('').astype(str).str.upper()
    t = t.str.replace(r'\+?\d[\d -]{4,}', ' ', regex=True)   # phone / reference numbers
    t = t.str.replace(r'[^A-Z& ]', ' ', regex=True)            # keep letters only
    return t.str.replace(r'\s+', ' ', regex=True).str.strip()


def add_features(df):
    df = df.copy()
    df['text'] = make_text(df)
    df['log_amount'] = np.log1p(df.amount_aed.fillna(df.amount).clip(lower=0))
    return df


def tfidf_logreg():
    """TF-IDF character 2-5 grams + word 1-2 grams, plus log-amount, into balanced logistic regression."""
    text = FeatureUnion([
        ('char', TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 5), sublinear_tf=True)),
        ('word', TfidfVectorizer(analyzer='word', ngram_range=(1, 2), sublinear_tf=True)),
    ])
    pre = ColumnTransformer([('text', text, 'text'), ('amount', StandardScaler(), ['log_amount'])])
    return Pipeline([('features', pre),
                     ('clf', LogisticRegression(max_iter=3000, C=10, class_weight='balanced'))])


def load_labelled(transactions_dir='outputs', labels_file='merchant_labels.xlsx'):
    """Personal and Khalifa expenses with the merchant label attached (row overrides applied)."""
    transactions_dir, labels_file = Path(transactions_dir), Path(labels_file)
    merchants = pd.read_excel(labels_file, sheet_name='Merchants')
    cats = [c for c in pd.read_excel(labels_file, sheet_name='Categories').category if c != 'Total']
    label_map = dict(zip(merchants.merchant, merchants.final_category))
    ov = pd.read_excel(labels_file, sheet_name='Ambiguous rows')
    ov = {k: v for k, v in zip(ov.txn_id, ov.row_override) if isinstance(v, str)}
    out = []
    for name in ['personal', 'khalifa']:
        d = pd.read_csv(transactions_dir / f'{name}_transactions_expenses.csv', parse_dates=['date'])
        d['label'] = d.merchant_clean.map(label_map)
        d.loc[d.txn_id.isin(ov), 'label'] = d.loc[d.txn_id.isin(ov), 'txn_id'].map(ov)
        assert d.label.notna().all(), f'{name}: unlabelled merchants - update merchant_labels.xlsx'
        out.append(add_features(d))
    return out[0], out[1], cats
