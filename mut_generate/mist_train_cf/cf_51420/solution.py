"""
QUESTION:
Implement the `account_balance` function, which takes a list of deposit and withdrawal operations and a list of corresponding fees as input. The function should return a tuple containing a boolean indicating whether the balance went below zero at any point, the operation index where the balance first went below zero (or -1 if it did not), and the final balance after all operations, rounded to two decimal places. The function should update the balance after each operation and apply the fees.
"""

from typing import List, Tuple

def account_balance(operations: List[int], fees: List[float]) -> Tuple[bool, float, int]:
    balance = 0
    for i, (op, fee) in enumerate(zip(operations, fees)):
        balance = round(balance + op - fee, 2)
        if balance < 0:
            return (True, balance, i)
    return (False, balance, -1)