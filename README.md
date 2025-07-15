# Aave Wallet Credit Scoring

This project builds a credit scoring system for wallets based on their historical interactions with the **Aave V2 DeFi protocol**.

## Objective

Assign a **credit score between 0 and 1000** to each wallet using only on-chain transaction behavior. The goal is to reward responsible users and flag potentially risky or bot-like accounts.

---

## Methodology

### Step 1: Data Input
- Source: Raw JSON data of ~100,000 transactions from Aave V2
- Fields: `wallet`, `timestamp`, `action`, `amount`, `asset`

### Step 2: Feature Engineering
For each wallet:
- Count and total amount of `deposit`, `borrow`, `repay`, `redeemunderlying`, and `liquidationcall` actions
- Number of active days
- Behavior ratios (e.g., repay/deposit)

### Step 3: Scoring Logic
- Rule-based formula prioritizing:
  - High deposits and repayments (+)
  - Regular activity (+)
  - Liquidations (–)
- Normalized final score to **0–1000** using MinMaxScaler

---

##  Architecture

```text
📁 aave-credit-scoring
├── data/                  # Raw input JSON (not included in repo)
├── outputs/               # Final credit scores & analysis plot
├── src/                   # Feature engineering + scoring code
├── README.md              # Project overview (this file)
├── analysis.md            # Score insights and distribution
└── requirements.txt       # Dependencies


🚀 How to Run
Step 1: Install Requirements
pip install -r requirements.txt

Step 2: Run the Scoring Pipeline
Make sure you have user_transactions.json inside the data/ folder.
python src/run_scoring.py

 OUTPUT
The results will be saved to:
outputs/wallet_scores.csv

📊 Example Score Distribution
For more insights, see analysis.md.

📬 Contact
For queries or suggestions, feel free to reach out via GitHub Issues or create a pull request!

