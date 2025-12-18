"""
QUESTION:
Create a function named `below_zero` that takes a list of operation-value pairs and an optional `case_insensitive` flag as input. The function should iterate through the operations, update a balance value, and return True if the final balance is less than or equal to zero. The `case_insensitive` flag should allow for equal treatment of 'Deposit' and 'deposit' or 'Withdrawal' and 'withdrawal', irrespective of their case. If `case_insensitive` is False, only 'deposit' and 'withdrawal' should be recognized. The function should start with a balance of zero and update it based on the operations.
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
    return balance <= 0