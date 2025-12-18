"""
QUESTION:
Create a function named `below_zero` that takes a list of tuples representing bank account operations and an optional `case_insensitive` flag. Each tuple in the list contains an operation type (either 'Deposit' or 'Withdrawal') and an operation value. The function should start with a balance of zero, apply each operation in the list, and return `True` if the balance ever falls below zero. If the `case_insensitive` flag is `True`, the function should treat 'Deposit' and 'deposit' as the same operation. If an invalid operation is encountered, the function should return the error message 'Invalid operation encountered.' The function should return `False` if the balance never falls below zero. The `case_insensitive` flag defaults to `False` if not provided.
"""

from typing import List, Tuple, Union

def below_zero(operations: List[Tuple[str, int]], case_insensitive: bool = False) -> Union[bool, str]:
    balance = 0
    for op_type, op_value in operations:
        if case_insensitive:
            op_type = op_type.lower()
        if op_type in ["deposit", "Deposit"]:
            balance += op_value
        elif op_type in ["withdrawal", "Withdrawal"]:
            balance -= op_value
        else:
            return "Invalid operation encountered."

        if balance < 0:
            return True
            
    return False