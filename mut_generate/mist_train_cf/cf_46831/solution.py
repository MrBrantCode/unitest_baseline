"""
QUESTION:
Create a function `below_zero` that takes a list of operations and an optional boolean flag `case_insensitive` as input. The list of operations contains tuples where the first element is a string representing the transaction type ('Deposit' or 'Withdrawal') and the second element is an integer representing the transaction amount. The function should return `True` if the balance falls below or equals zero after processing all operations. If `case_insensitive` is `True`, the function should treat 'Deposit' and 'deposit' (or 'Withdrawal' and 'withdrawal') as the same operation. If not specified, `case_insensitive` defaults to `False`.
"""

from typing import List, Tuple

def below_zero(operations: List[Tuple[str, int]], case_insensitive: bool = False) -> bool:
    balance = 0
    for operation in operations:
        transaction, amount = operation
        if case_insensitive:
            transaction = transaction.lower()
        if transaction == "deposit":
            balance += amount
        elif transaction == "withdrawal":
            balance -= amount
        if balance <= 0:
            return True
    return False