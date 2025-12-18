"""
QUESTION:
Create a function `below_zero` that takes in a list of bank account operations (deposits and withdrawals) as a list of integers or floats, an optional `handle_float` flag to handle floating point precision, and an optional `balance_limit` to restrict withdrawals. The function should return `True` if the account balance falls below zero at any point, and `False` otherwise. The function should also handle invalid operations such as negative deposits and withdrawals exceeding the balance limit.
"""

from typing import List, Union

def below_zero(operations: List[Union[int, float]], handle_float: bool = False, balance_limit: int = None) -> bool:
    balance = 0

    if handle_float:
        operations = [round(op, 2) for op in operations]

    for op in operations:
        if op < 0:
            print("Negative deposit operation is invalid!")
            continue

        if balance_limit and op > balance_limit:
            print("The withdrawal operation exceeds the balance limit!")
            continue

        balance += op 

        if balance < 0:
            return True

    return False