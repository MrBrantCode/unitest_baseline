"""
QUESTION:
Create a function `below_zero` that takes a list of integers representing deposit and withdrawal operations and an optional boolean flag `case_insensitive` with a default value of `False`. The function should return `True` if the balance, initially set to zero, goes below zero at any point during the operations. If `case_insensitive` is `True`, the function should also return `True` if the balance reaches zero. If the balance never goes below or reaches zero, the function should return `False`.
"""

from typing import List

def below_zero(operations: List[int], case_insensitive: bool = False) -> bool:
    """
    This function takes a series of deposit and withdrawal operations and determines if a starting balance of zero 
    falls below or reaches zero. If 'case_insensitive' is set to True, function will return True when balance reaches
    zero as well. Otherwise, the function will return True only when balance goes below zero.

    Parameters:
    operations (List[int]): A list of integers, each representing an operation on the balance. Positive means deposit 
                            and negative means withdrawal.

    case_insensitive (bool): If set to True, function will return True when balance reaches zero.

    Return:
    bool: Returns True if balance goes below zero or reaches zero (if 'case_insensitive' is True). Otherwise, returns False.
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0 or (case_insensitive and balance == 0):
            return True
    return False