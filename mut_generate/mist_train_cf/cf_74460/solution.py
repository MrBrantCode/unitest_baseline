"""
QUESTION:
Write a function named `below_zero` that takes a list of integers and/or floats representing deposit and withdrawal operations on a bank account with an initial balance of zero. The function should return `True` if the balance ever falls below zero and `False` otherwise. Include an optional `handle_float` parameter to allow or disallow floating point numbers (default is `False`) and a `balance_limit` parameter to set the maximum allowed balance (default is `10`). The function should correctly handle negative deposits and withdrawals that exceed the balance limit.
"""

from typing import List, Union

def below_zero(operations: List[Union[int, float]], handle_float: bool = False, balance_limit: int = 10) -> bool:
    """
    Checks if a bank account's balance ever falls below zero given a list of deposit and withdrawal operations.

    Args:
    operations (List[Union[int, float]]): A list of integers and/or floats representing deposit and withdrawal operations.
    handle_float (bool): Optional parameter to allow or disallow floating point numbers. Defaults to False.
    balance_limit (int): Optional parameter to set the maximum allowed balance. Defaults to 10.

    Returns:
    bool: True if the balance ever falls below zero, False otherwise.
    """
    balance = 0
    for op in operations:
        if not handle_float and isinstance(op, float):
            continue
        if op > 0 and balance + op > balance_limit:
            balance = balance_limit
        elif op < 0 and balance + op < 0:
            return True
        else:
            balance += op
    return False