"""
QUESTION:
Given a list of deposit and withdrawal operations on a bank account that begins with zero balance and a list of fees corresponding to each operation, implement the function `account_balance(operations: List[int], fees: List[float])` that returns a tuple of two values: a boolean indicating if the balance goes below zero at any point, and the account balance upon the conclusion of all operations, rounded to two decimal places.
"""

def account_balance(operations, fees):
    balance = 0.0
    balance_below_zero = False
    for op, fee in zip(operations, fees):
        balance += op - fee
        if balance < 0:
            balance_below_zero = True
    return balance_below_zero, round(balance, 2)