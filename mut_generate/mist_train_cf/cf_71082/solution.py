"""
QUESTION:
Given a list of transactions (positive for deposit, negative for withdrawal), implement a function `minimum_balance` to find the smallest balance encountered during the transactions. If the balance never goes below zero, return 0. The function should take a list of integers as input and return an integer as output.
"""

from typing import List

def minimum_balance(operations: List[int]) -> int:
    balance = 0
    min_balance = 0
    for op in operations:
        balance += op
        if balance < min_balance:
            min_balance = balance
    return min_balance if min_balance < 0 else 0