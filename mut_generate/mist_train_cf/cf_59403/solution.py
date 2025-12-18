"""
QUESTION:
Implement the `below_zero` function, which takes a list of transactions (`operations`) as input and returns `True` if the balance goes below zero or exceeds a balance limit at any point during the transactions, and `False` otherwise. The function should have an optional parameter `handle_float` (default: `False`) to allow floating-point values in the transactions and another optional parameter `balance_limit` (default: `10`) to set the balance limit.
"""

from typing import List, Union

def below_zero(operations: List[Union[int, float]], handle_float: bool = False, balance_limit: int = 10) -> bool:
    balance = 0
    for op in operations:
        if not handle_float and isinstance(op, float):
            continue
        balance += op
        if balance < 0 or balance > balance_limit:
            return True
    return False