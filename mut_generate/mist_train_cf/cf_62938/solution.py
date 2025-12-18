"""
QUESTION:
Implement a function named `below_zero` that takes a list of tuples representing bank account operations as input. Each tuple contains the type of operation (deposit or withdrawal) and its corresponding value. The function should return `True` if the balance ever turns negative, or if the `case_insensitive` flag is `True`, also return `True` if the balance reaches zero when operation types are expressed without a consistent case. If none of these conditions are met, the function should return `False`. The function should have an optional parameter `case_insensitive` with a default value of `False`.
"""

from typing import List, Tuple

def below_zero(operations: List[Tuple[str, int]], case_insensitive: bool = False) -> bool:
    balance = 0
    for op in operations:
        operation, value = op

        if case_insensitive:
            operation = operation.lower()

        if operation == 'deposit':
            balance += value
        elif operation == 'withdrawal':
            balance -= value

        if balance < 0 or (case_insensitive and balance == 0):
            return True
    return False