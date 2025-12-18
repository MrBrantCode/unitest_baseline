"""
QUESTION:
Write a function `below_zero` that takes a list of integers representing deposit and withdrawal transactions and returns a tuple containing a boolean indicating whether the balance went below zero, the transaction that caused the balance to dip below zero (or None if no such transaction occurred), and the final balance. Assume the account starts at a balance of zero. The function should support both deposit and withdrawal transactions. The output should be a tuple of three values: a boolean, an integer (or None), and an integer.
"""

from typing import List, Tuple

def below_zero(transactions: List[int]) -> Tuple[bool, int, int]:
    balance = 0
    for transaction in transactions:
        balance += transaction
        if balance < 0:
            return True, transaction, balance
    return False, None, balance