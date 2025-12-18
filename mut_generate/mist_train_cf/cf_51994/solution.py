"""
QUESTION:
Implement a function named `below_zero` that takes in a list of operations and an optional case_insensitive flag. The operations can be either integers, string representations of integers, or tuples where the first element is the operation and the second element is a string representing the frequency of the operation. The function should apply these operations to an initial balance of zero and return True if the balance ever falls below zero. If the case_insensitive flag is True, the function should also return True if the balance is exactly zero. The case_insensitive flag is False by default.
"""

from typing import List, Union, Tuple

def below_zero(operations: List[Union[Tuple[int, str], int]], case_insensitive: bool = False) -> bool:
    balance = 0
    for op in operations:
        if isinstance(op, tuple):
            value, frequency = op
            balance += int(value) * int(frequency)
        else:
            balance += int(op)
        if balance < 0 or (case_insensitive and balance == 0):
            return True
    return False