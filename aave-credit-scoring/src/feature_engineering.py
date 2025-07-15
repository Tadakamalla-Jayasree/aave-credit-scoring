
import pandas as pd

def build_features(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    grouped = df.groupby('wallet')
    features = []

    for wallet, data in grouped:
        wallet_feat = {}
        wallet_feat['wallet'] = wallet
        wallet_feat['txn_count'] = len(data)
        wallet_feat['active_days'] = data['timestamp'].dt.date.nunique()

        for action in ['deposit', 'borrow', 'repay', 'redeemunderlying', 'liquidationcall']:
            action_df = data[data['action'] == action]
            wallet_feat[f'{action}_count'] = len(action_df)
            wallet_feat[f'{action}_amount'] = action_df['amount'].sum()

        features.append(wallet_feat)

    return pd.DataFrame(features)
