"""
QUESTION:
Write a function named "below_zero" that takes two parameters: a list of tuples containing operation types and values, and an optional "case_insensitive" flag set to False by default. The function should determine if the balance of a bank account falls below zero after performing a series of deposit and withdrawal operations. If the "case_insensitive" flag is set to True, treat 'Deposit' and 'deposit' as well as 'Withdrawal' and 'withdrawal' as the same and return True if the balance equals zero. The function should return True if the balance falls below or equals zero and False otherwise.
"""

from typing import List, Tuple

def below_zero(operations: List[Tuple[str, int]], case_insensitive: bool = False) -> bool:
    balance = 0
    for op_type, value in operations:
        if case_insensitive:
            op_type = op_type.lower()
        if op_type in ['deposit', 'deposits']:
            balance += value
        elif op_type in ['withdrawal', 'withdrawals']:
            balance -= value
        if balance <= 0:
            return True
    return False