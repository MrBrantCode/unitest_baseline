"""
QUESTION:
Write a function `below_zero` that takes two lists of the same length as input: `operations` and `fees`, both containing integers. The function should return a tuple of two values: a boolean indicating whether the balance of a bank account falls below zero at any point after applying the fees, and the final balance of the account. The account starts with a balance of zero. Each operation in the `operations` list represents a deposit or withdrawal, and each corresponding fee in the `fees` list is subtracted from the balance after applying the operation. If the balance falls below zero, the function should return `True` and the balance at that point; otherwise, it should return `False` and the final balance.
"""

from typing import List, Tuple

def below_zero(operations: List[int], fees: List[int]) -> Tuple[bool, int]:
    balance = 0
    for op, fee in zip(operations, fees):
        balance += op - fee
        if balance < 0:
            return True, balance
    return False, balance