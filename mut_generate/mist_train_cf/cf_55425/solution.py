"""
QUESTION:
Create a function named `below_zero_and_max_balance` that takes a list of operations (which can be either integers or floats) and an optional boolean flag `handle_float` with a default value of `False`. The function should return a tuple containing two elements: a boolean indicating whether the balance ever fell below zero during the operations, and the maximum balance achieved. If `handle_float` is `True`, the function should convert any non-integer float values to integers before performing the operations.
"""

from typing import List, Union, Tuple
import math

def below_zero_and_max_balance(operations: List[Union[int, float]], handle_float: bool = False) -> Tuple[bool, float]:
    balance = 0
    max_balance = 0
    ever_below_zero = False
    for op in operations:
        if handle_float and isinstance(op, float) and not math.isinf(op) and op != int(op):
            op = int(op)
        balance += op
        if balance < 0:
            ever_below_zero = True
        if balance > max_balance:
            max_balance = balance
    return ever_below_zero, max_balance