"""
QUESTION:
Create a function named 'below_zero' that takes a list of integers or floats representing deposits or withdrawals from a bank account, and an optional boolean flag 'handle_float' to handle floating point numbers. The function should return True if the balance becomes less than zero at any point, otherwise return False. The 'handle_float' flag is optional and defaults to False.
"""

from typing import List, Union

def below_zero(operations: List[Union[int, float]], handle_float: bool = False) -> bool:
    balance = 0.0 if handle_float else 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False