"""
QUESTION:
Create a function `below_zero` that takes a list of tuples representing bank account operations in the format (operation type, operation value) and an optional case-insensitive flag. The function should return `True` if the account balance falls below zero at any point, `False` otherwise, or an error message if an invalid operation is encountered. The function should treat 'Deposit' and 'deposit' and 'Withdrawal' and 'withdrawal' as the same when the case-insensitive flag is `True`.
"""

from typing import List, Tuple, Union

def below_zero(operations: List[Tuple[str, int]], case_insensitive: bool = False) -> Union[bool, str]:
    balance = 0
    
    for operation, amount in operations:
        if case_insensitive:
            operation = operation.lower()
        
        if operation == "deposit":
            balance += amount
        elif operation == "withdrawal":
            balance -= amount
        else:
            return "Encountered an illegal operation."
        
        if balance < 0:
            return True
            
    return False