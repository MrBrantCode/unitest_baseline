"""
QUESTION:
Write a function named 'below_zero' that takes a list of Union[int, float] representing bank transactions and an optional boolean 'handle_float' flag. The function should return True immediately when the account balance is below zero and False otherwise. The 'handle_float' flag, when set to True, allows the function to handle floating-point numbers in the transaction list; otherwise, it ignores them.
"""

from typing import List, Union

def entrance(operations: List[Union[int, float]], handle_float: bool = False) -> bool:
    balance = 0
    for op in operations:
        if isinstance(op, float) and not handle_float:
            continue
        balance += op
        if balance < 0:
            return True
    return False