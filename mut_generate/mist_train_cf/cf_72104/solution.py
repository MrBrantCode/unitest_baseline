"""
QUESTION:
Given a list of daily operations on a bank account (positive values for deposit, negative values for withdrawal), determine if the balance ever drops below zero or drops to zero based on the 'case_insensitive' flag. Implement a function `below_zero` that takes two parameters: a list of daily operations (`operations`) and an optional boolean flag (`case_insensitive` with default value `False`). The function should return `True` if the balance drops to or below zero (depending on the `case_insensitive` flag) and `False` otherwise.
"""

from typing import List

def below_zero(operations: List[int], case_insensitive: bool = False) -> bool:
    """
    Given a list of daily operations on a bank account (positive values for deposit,
    negative values for withdrawal), determine if the balance ever drops below zero
    or drops to zero based on the 'case_insensitive' flag.

    :param operations: List of daily deposit/withdrawal operations
    :param case_insensitive: Flag indicating if balance dropping to zero should be flagged
    :return: True if balance drops to or below zero, False otherwise
    """
    balance = 0
    for op in operations:
        balance += op
        if case_insensitive and balance <= 0:
            return True
        elif not case_insensitive and balance < 0:
            return True
    return False