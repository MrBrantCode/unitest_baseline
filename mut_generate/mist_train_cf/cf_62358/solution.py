"""
QUESTION:
Implement the function `minimum_balance(operations: List[int]) -> int` to compute the lowest balance that occurred during a series of fiscal operations in a bank account initially with a zero balance. The function should return the minimum balance if it ever goes below zero, otherwise return None.
"""

def minimum_balance(operations):
    minimum_balance = 0
    current_balance = 0

    for op in operations:
        current_balance += op
        
        if current_balance < minimum_balance:
            minimum_balance = current_balance

    return minimum_balance if minimum_balance < 0 else None