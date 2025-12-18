"""
QUESTION:
Implement a function named `overdraft_alert` that takes a list of tuples, where each tuple contains an operation type and a value, and an optional `ignore_case` flag. The function should update the balance based on the operations and apply a transaction fee after each operation, following a tiered system. The function should return `True` if the balance ever goes below zero or is exactly zero at the end, and `False` otherwise. The tiered transaction fee system is as follows: 2% for balances between 0 and 1000, 1% for balances between 1001 and 5000, and 0.5% for balances above 5000. If the `ignore_case` flag is `True`, the function should treat 'Deposit' and 'deposit' (as well as 'Withdrawal' and 'withdrawal') as identical.
"""

def transaction_fee(current_balance: int) -> float:
    if current_balance >= 0 and current_balance <= 1000:
        return 0.02
    elif current_balance > 1000 and current_balance <= 5000:
        return 0.01
    elif current_balance > 5000:
        return 0.005
    else:
        return 0

def overdraft_alert(operations, ignore_case: bool = False):
    balance = 0
    for op, value in operations:
        if ignore_case:
            op = op.lower()
        if op == 'deposit':
            balance += value
            balance -= value * transaction_fee(balance)  # Apply transaction fee
        elif op == 'withdrawal':
            balance -= value
            balance -= value * transaction_fee(balance)  # Apply transaction fee
        if balance < 0:
            return True
    return balance == 0