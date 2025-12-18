"""
QUESTION:
Complete the `below_zero` function that takes a list of integers and/or floats representing bank transactions, a boolean indicating whether to handle floats, and an integer balance limit. The function checks if the account balance ever falls below zero during these transactions. If it does, the function returns True, else it returns False. It should correctly process negative deposits and withdrawals beyond the balance limit.
"""

from typing import List, Union

def below_zero(operations: List[Union[int, float]], handle_float: bool = False, balance_limit: int = 10):
    balance = balance_limit

    for op in operations:
        if handle_float and isinstance(op, float):
            balance += op
        elif isinstance(op, int):
            balance += op
        else:
            raise Exception("Invalid transaction type")

        if balance < 0:
            return True
    return False