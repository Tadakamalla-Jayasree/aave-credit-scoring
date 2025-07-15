
# Aave Wallet Credit Scoring

This project assigns a credit score (0–1000) to wallets based on their transaction behavior on the Aave V2 protocol.

## Objective

To identify and reward responsible DeFi wallet behavior while penalizing risky or bot-like actions using data-driven scoring.

## How It Works

1. Load JSON transaction history.
2. Extract behavior features per wallet.
3. Score wallets using rule-based logic.
4. Normalize scores between 0–1000.

## Features Used

- Total transactions, deposits, borrows, repayments
- Amounts transacted per action
- Active usage days
- Liquidation penalties

## Run the Pipeline

```bash
pip install -r requirements.txt
python src/run_scoring.py
```

## Output

File: `outputs/wallet_scores.csv` containing:

wallet,credit_score
0x123,385.47
0x456,912.34
