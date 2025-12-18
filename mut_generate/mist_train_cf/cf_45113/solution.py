"""
QUESTION:
Create a function `below_zero` that takes a list of transactions as input, where a positive number represents a deposit and a negative number represents a withdrawal. The function should return a tuple containing three values: a boolean indicating whether the bank account balance drops below zero, the transaction that led to the balance dropping below zero (or None if the balance never dropped below zero), and the final balance. Assume the initial bank account balance is zero.
"""

from typing import List, Tuple

def below_zero(transactions: List[int]) -> Tuple[bool, int, int]:
    balance = 0
    for transaction in transactions:
        balance += transaction
        if balance < 0:
            return True, transaction, balance
    return False, None, balance