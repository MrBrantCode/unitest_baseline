"""
QUESTION:
Write a function named `below_zero` that takes in a list of operations (deposits and withdrawals) and two optional parameters: `handle_float` (a boolean to handle floating point numbers) and `balance_limit` (a specified balance limit for withdrawals). The function should return `True` if the account balance falls below zero or if an operation exceeds the balance limit, and `False` otherwise. The function should be able to handle both integer and floating-point operations. The `handle_float` parameter is `False` by default, and the `balance_limit` is set to infinity by default.
"""

def below_zero(operations: list, handle_float: bool = False, balance_limit: float = float('inf')) -> bool:
    balance = 0
    for op in operations:
        if handle_float and isinstance(op, float):
            balance += float(op)
        else: 
            balance += int(op)
        if balance < 0 or op < -balance_limit: 
            return True
    return False if balance >= 0 else True