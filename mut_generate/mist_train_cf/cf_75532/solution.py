"""
QUESTION:
Create a function `below_zero` that takes in a list of transactions, where each transaction can be either a deposit (positive number) or a withdrawal (negative number), and returns `True` if the balance goes below zero or exceeds the balance limit at any point, and `False` otherwise.

The function should support both integer and floating-point transactions, and should be able to handle negative transactions and withdrawals that exceed the balance limit. The balance limit is set to a default value of 10, but can be changed by the user. The function should also have an optional flag `handle_float` that determines whether the function supports floating-point numbers.
"""

from typing import List, Union

def below_zero(operations: List[Union[int, float]], balance_limit: int = 10, handle_float: bool = False) -> bool:
    balance = 0.0 if handle_float else 0
    for op in operations:
        balance += op
        if balance < 0 or (balance_limit is not None and balance > balance_limit):
            return True
    return False