"""
QUESTION:
Create a function `below_zero` that takes a list of integers representing bank account transactions (deposits and withdrawals) and returns a tuple containing a boolean indicating whether the account balance ever went below zero, the transaction that caused the deficit (if any), and the final balance. Assume the initial account balance is zero.
"""

from typing import List, Tuple

def below_zero(operations: List[int]) -> Tuple[bool, int, int]:
    balance = 0
    index = None
    for i in operations:
        balance += i
        if balance < 0 and index is None:
            index = i
    return (balance < 0, index, balance)