"""
QUESTION:
Create a function named `below_zero` that takes two parameters: `operations` and `case_insensitive`. The `operations` parameter should be a list of integers or strings representing integers. The `case_insensitive` parameter is an optional boolean flag that defaults to False.

The function should return True if at any point the balance of the account falls below zero, or if the `case_insensitive` flag is True and the balance equals zero. Otherwise, it should return False. The function should start with a balance of zero and iterate over each operation in the list, adding the operation to the balance.
"""

from typing import List, Union

def below_zero(operations: List[Union[int, str]], case_insensitive: bool = False) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. The operations can be integers or strings representing integers. Your task is to
    detect if at any point the balance of the account falls below zero, and at that point function
    should return True. Otherwise, it should return False. Include an optional case_insensitive flag
    to return True if the balance equals zero as well.
    
    """
    
    balance = 0
    for op in operations:
        balance += int(op)
        if balance < 0 or (case_insensitive and balance == 0):
            return True
    return False