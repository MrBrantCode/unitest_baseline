"""
QUESTION:
Create a function named `below_zero` that takes in a list of operations (tuples of a string and an integer) and an optional boolean parameter `case_insensitive` defaulting to `False`. The function should return `True` if the balance goes below or equals zero after performing all operations. If `case_insensitive` is `True`, the function should treat 'Deposit' and 'deposit', 'Withdrawal' and 'withdrawal' as the same operation.
"""

from typing import List, Tuple

def below_zero(operations: List[Tuple[str, int]], case_insensitive: bool = False) -> bool:
    balance = 0
    
    for operation, value in operations:
        if case_insensitive:
            operation = operation.lower()
        
        if operation == 'deposit':
            balance += value
        elif operation == 'withdrawal':
            balance -= value
        
        if balance <= 0: 
            return True
            
    return False