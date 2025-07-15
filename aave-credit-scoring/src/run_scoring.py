
import pandas as pd
from src.feature_engineering import build_features
from src.scoring_model import compute_scores

df = pd.read_json("data/user_transactions.json", lines=True)
wallet_features = build_features(df)
wallet_scores = compute_scores(wallet_features)
wallet_scores.to_csv("outputs/wallet_scores.csv", index=False)
print(" Scoring complete. Output saved at outputs/wallet_scores.csv")
