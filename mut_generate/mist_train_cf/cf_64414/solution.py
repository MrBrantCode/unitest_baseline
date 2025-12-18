"""
QUESTION:
Create a function named `below_zero` that takes two parameters: `operations` and `case_insensitive`. The `operations` parameter is a list of tuples where each tuple contains an operation type (string) and an operation value (integer). The `case_insensitive` parameter is a boolean that defaults to `False`. The function should return `True` if the balance goes below zero after performing the operations and `False` otherwise. If `case_insensitive` is `True`, the function should treat 'Deposit' and 'deposit', and 'Withdrawal' and 'withdrawal' as the same operation.
"""

from typing import List, Tuple

def below_zero(operations: List[Tuple[str, int]], case_insensitive: bool = False) -> bool:
    balance = 0
    for op, amount in operations:
        if case_insensitive:
            op = op.lower()
        if op == 'deposit':
            balance += amount
        elif op == 'withdrawal':
            balance -= amount
            
        if balance < 0:
            return True
            
    return False