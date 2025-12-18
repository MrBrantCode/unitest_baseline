"""
QUESTION:
Create a function named `below_zero` that takes a list of integers representing bank account operations and an optional `case_insensitive` boolean flag. The function should return `True` if the account balance falls below zero (or equals zero if `case_insensitive` is `True`), and `False` otherwise. The account starts with a balance of zero, and the function should check the balance after each operation.
"""

from typing import List

def below_zero(operations: List[int], case_insensitive: bool = False) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if case_insensitive:
            if balance <= 0:
                return True
        else:
            if balance < 0:
                return True
    return False