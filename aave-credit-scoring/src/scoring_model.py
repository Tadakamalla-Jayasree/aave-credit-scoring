
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def compute_scores(df_feat):
    df = df_feat.copy()
    df.fillna(0, inplace=True)
    df['score'] = (
        df['deposit_amount'] * 0.4 +
        df['repay_amount'] * 0.3 -
        df['liquidationcall_count'] * 50 +
        df['active_days'] * 10
    )
    scaler = MinMaxScaler(feature_range=(0, 1000))
    df['credit_score'] = scaler.fit_transform(df[['score']])
    return df[['wallet', 'credit_score']]
