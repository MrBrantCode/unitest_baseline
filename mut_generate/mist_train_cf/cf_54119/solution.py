"""
QUESTION:
Implement a function named `below_zero` that takes in a list of banking transactions (`operations`) and two optional parameters: `handle_float` (default is `False`) and `balance_limit` (default is `10.0`). The function should return `True` if the balance drops below zero after processing the transactions, and `False` otherwise. The function should also check for negative deposits, withdrawals exceeding the balance limit, and handle both integer and floating-point numbers based on the `handle_float` parameter. The transactions can be either integers or floating-point numbers.
"""

from typing import List, Union

def below_zero(operations: List[Union[int, float]], handle_float: bool = False, balance_limit: Union[int, float] = 10.0):
    balance = 0.0
    for op in operations:
        if op < 0 and abs(op) > balance_limit:  
            return True
        elif op > 0 and abs(op) > balance_limit:  
            return True
        
        if handle_float and isinstance(op, float):  
            balance += op
        elif isinstance(op, int):  
            balance += op

        if balance < 0:  
            return True
    return False