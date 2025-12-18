"""
QUESTION:
Implement a function called `detect_fraudulent_transactions` that takes a list of transaction records as input and returns a list of flagged transactions for further review. Each transaction record is a dictionary containing 'id', 'amount', 'timestamp', and 'account' details. Flag a transaction if its amount exceeds $10,000 or if there are at least three transactions within a 30-minute time window for the same account.
"""

import pandas as pd

def is_high_frequency(transactions, account, current_timestamp, threshold_minutes=30):
    count = 0
    for t in transactions:
        if t["account"] == account and t["timestamp"] != current_timestamp:
            time_diff = abs((pd.to_datetime(t["timestamp"]) - pd.to_datetime(current_timestamp)).total_seconds() / 60)
            if time_diff <= threshold_minutes:
                count += 1
                if count >= 3:  
                    return True
    return False

def detect_fraudulent_transactions(transactions):
    flagged_transactions = []
    for transaction in transactions:
        if transaction["amount"] > 10000.0:
            flagged_transactions.append(transaction)
        elif is_high_frequency(transactions, transaction["account"], transaction["timestamp"]):
            flagged_transactions.append(transaction)
    return flagged_transactions