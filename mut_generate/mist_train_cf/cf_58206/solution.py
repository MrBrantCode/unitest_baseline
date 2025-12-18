"""
QUESTION:
Write a function `below_zero` that takes a list of deposit and withdrawal operations and a case_insensitive flag. The operations can be integers, strings representing integers, or tuples containing an integer and a string representing the number of times to perform the operation. The function should return True if the balance dips below zero at any point or equals zero when the case_insensitive flag is set, and False otherwise. The function should be case insensitive when the flag is set. The function should also handle both positive and negative integers.
"""

from typing import List, Union, Tuple

def below_zero(operations: List[Union[Tuple[int, str], int]], case_insensitive: bool = False) -> bool:
    balance = 0
    for op in operations:
        if isinstance(op, Tuple):  # If operation is tuple
            value, num = int(op[0]), int(op[1])
            balance += value * num
        else:  # If operation is int or str
            balance += int(op)
        if balance < 0 or (case_insensitive and balance == 0):
            return True
    return False