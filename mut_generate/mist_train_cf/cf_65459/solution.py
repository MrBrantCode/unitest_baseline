"""
QUESTION:
Develop a function `below_zero` that monitors a mock bank account's balance by iterating over a list of integers or floating-point numbers representing deposits (+ve numbers) or withdrawals (-ve numbers). The function should cease and return `True` when the balance falls below zero; otherwise, it returns `False`. The function should handle floating-point numbers, which can be toggled on or off via a boolean argument `handle_float`. If `handle_float` is `False`, any float operations should be skipped.
"""

from typing import List, Union

def below_zero(operations: List[Union[int, float]], handle_float: bool = False) -> bool:
    balance = 0.0 if handle_float else 0
    for op in operations:
        if not handle_float and isinstance(op, float):
            continue
        balance += op
        if balance < 0:
            return True
    return False