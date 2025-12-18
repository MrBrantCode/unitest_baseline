"""
QUESTION:
Complete the function `below_zero` that accepts a list of integers representing bank deposit and withdrawal transactions. The function should identify if at any point the account balance dips below zero, initially starting with zero balance, and return the results accordingly.

The function should return a tuple containing a boolean indicating whether the balance went below zero, the operation that caused the balance to dip if applicable, and the final balance. If the balance never goes below zero, the second element of the tuple should be `None`.
"""

from typing import List, Tuple

def below_zero(operations: List[int]) -> Tuple[bool, int, int]:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return (True, operation, balance)
    return (False, None, balance)