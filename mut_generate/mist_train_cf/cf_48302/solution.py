"""
QUESTION:
Write a function `account_balance` that takes three lists as input: `operations`, `fees`, and `interests`. `operations` is a list of deposit and withdrawal operations on a bank account that starts with a zero balance, `fees` is a list of fees for each operation, and `interests` is a list of interest rates (annual) for each operation. The function should return a tuple of two values: a boolean indicating whether the account balance falls below zero at any point, and the final account balance at the end of the year. The function should apply the fees and interests to the balance after each operation and return as soon as the balance falls below zero. The order of operations is from the start of the year to the end of the year.
"""

from typing import List, Tuple

def account_balance(operations: List[int], fees: List[int], interests: List[float]) -> Tuple[bool, float]:
    balance = 0
    for op, fee, interest in zip(operations, fees, interests):
        balance += op - fee
        balance += balance * (interest / 100)
        if balance < 0:
            return True, balance
    return False, balance