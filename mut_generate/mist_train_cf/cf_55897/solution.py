"""
QUESTION:
Create a function called `below_zero` that takes a list of operations (either int or float) as input and returns a boolean value indicating whether the balance goes below zero. The function should have two optional parameters: `handle_float` (default is False) and `operation_type` (default is 'withdrawal'). The function should support floating-point numbers when `handle_float` is True, and it should distinguish between deposit and withdrawal operations based on the `operation_type` parameter.
"""

from typing import List, Union

def below_zero(operations: List[Union[int, float]], handle_float: bool = False, operation_type: str = 'withdrawal') -> bool:
    balance = 0.0 if handle_float else 0
  
    for op in operations:
        # Account for the operation type
        if operation_type == 'deposit':
            balance += op
        else: # 'withdrawal'
            balance -= op

        if balance < 0:
            return True
    return False