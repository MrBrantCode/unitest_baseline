"""
QUESTION:
Write a function `account_transactions_with_undo` that takes a list of transactions where each transaction is a tuple of account ID, operation type, and value. The function should process the transactions, handle deposits and withdrawals, and check for negative balances and excessive withdrawals. It should return a string indicating whether all transactions are successful or an error message with the transaction index or account ID. 

The function should also maintain a history of transactions for each account. Assume that the input list of transactions is ordered. 

Restrictions: The function should not use external libraries or frameworks, and should handle potential edge cases such as negative deposits and withdrawals.
"""

def account_transactions_with_undo(transactions):
    accounts = {}
    
    for i, (account_id, operation, value) in enumerate(transactions):
        # Initialize account if does not exist
        if account_id not in accounts:
            accounts[account_id] = {"balance": 0, "history": []}
        
        # Check negative deposit and excessive withdrawal
        if operation == "deposit":
            if value < 0:
                return f"Negative deposit at transaction index: {i}"
            else:
                accounts[account_id]["balance"] += value
        elif operation == "withdrawal":
            if accounts[account_id]["balance"] < value:
                return f"Exceeding withdrawal: {value} at transaction index: {i}. Available balance: {accounts[account_id]['balance']}"
            else:
                accounts[account_id]["balance"] -= value
        
        # Maintain a history of transactions for each account
        accounts[account_id]["history"].append((operation, value))
    
    # Check for negative balance
    for account_id, account in accounts.items():
        if account["balance"] < 0:
            return f"Negative balance in account id: {account_id}"
    
    return "All transactions are successful."