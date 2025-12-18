"""
QUESTION:
Create a function named `below_zero` that takes a list of integers representing deposit and withdrawal transactions. The function should return a tuple containing a boolean indicating whether the account balance goes below zero at any point and the final balance. The initial balance is zero, and transactions are applied sequentially.
"""

from typing import List, Tuple

def below_zero(operations: List[int]) -> Tuple[bool, int]:
    balance = 0
    negative_balance = False
    for op in operations:
        balance += op
        if balance < 0:
            negative_balance = True
    return negative_balance, balance