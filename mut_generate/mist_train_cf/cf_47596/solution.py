"""
QUESTION:
Write a function `calculate_balance` that takes a list of integers representing financial operations as input. The function should return the maximum balance after performing all the operations, while adhering to the following conditions: 
- If the balance remains negative after all operations, return 0. 
- If the balance exceeds 1000 at any point, return 1000.
"""

from typing import List

def calculate_balance(operations: List[int]) -> int:
    min_balance = max_balance = balance = 0
    for op in operations:
        balance += op
        # Prevent exceeding 1000
        if balance > 1000:
            return 1000
        min_balance = min(balance, min_balance)
        max_balance = max(balance, max_balance)
    # Prevent negative balance
    if min_balance < 0:
        return 0
    return max_balance