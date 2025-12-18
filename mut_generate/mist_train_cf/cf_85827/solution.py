"""
QUESTION:
Write a function `below_zero` that takes a list of operations and an optional case_insensitive flag, and returns True if the balance goes below zero or hits zero when case_insensitive is True, and False otherwise. The operations are represented as a list of tuples, where each tuple contains a string indicating the type of operation ('deposit' or 'withdrawal') and an integer indicating the amount. If case_insensitive is True, 'deposit', 'Deposit', 'withdrawal', and 'Withdrawal' should be treated as the same operation.
"""

from typing import List, Tuple

def below_zero(operations: List[Tuple[str, int]], case_insensitive: bool = False) -> bool:
    balance = 0
    for operation, amount in operations:
        if case_insensitive:
            operation = operation.lower()
        if operation == 'deposit':
            balance += amount
        elif operation == 'withdrawal':
            balance -= amount
        if balance < 0:
            return True
    return balance == 0 if case_insensitive else False