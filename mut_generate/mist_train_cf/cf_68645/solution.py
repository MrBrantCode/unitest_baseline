"""
QUESTION:
Create a function `below_zero` that takes two parameters: a list of integers and/or floats (`operations`) and an optional boolean flag (`handle_float`). The function should iterate over each operation in the list, update the balance accordingly, and return `True` as soon as the balance goes below zero. If the `handle_float` flag is `True`, floating point comparisons should be made using an epsilon value for precision. If `handle_float` is `False` or not provided, floating point comparisons should be made directly.
"""

from typing import List, Union

def below_zero(operations: List[Union[int, float]], handle_float: bool = False) -> bool:
    balance = 0
    for op in operations:
        balance += op

        if balance < 0:
            if handle_float and isinstance(balance, float):
                if balance + 1e-9 < 0:
                    return True
            else:
                return True
    return False