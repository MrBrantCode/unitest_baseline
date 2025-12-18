"""
QUESTION:
Implement a function named `below_zero` that takes a list of integers representing banking operations (deposits and withdrawals) and returns a tuple containing a boolean indicating whether the balance went below zero, the transaction that caused the balance to go below zero (or `None` if it didn't), and the final account balance. The balance starts at zero.
"""

from typing import List, Tuple

def below_zero(operations: List[int]) -> Tuple[bool, int, int]:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return (True, op, balance)
    return (False, None, balance)