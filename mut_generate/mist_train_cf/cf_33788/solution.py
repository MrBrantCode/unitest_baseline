"""
QUESTION:
Write a function `process_transactions(transactions)` that takes a list of transactions as input, where each transaction is a dictionary containing 'type' ('deposit' or 'withdrawal') and 'amount', and returns the final account balance after processing all transactions in order. The balance should be updated by adding the amount for 'deposit' and subtracting the amount for 'withdrawal'.
"""

def entrance(transactions):
    balance = 0
    for transaction in transactions:
        if transaction['type'] == 'deposit':
            balance += transaction['amount']
        elif transaction['type'] == 'withdrawal':
            balance -= transaction['amount']
    return balance