"""
QUESTION:
Create a function `below_zero` that takes in a list of financial operations as tuples and an optional boolean flag `case_insensitive`. Each tuple contains an account holder's name, an operation type ('Deposit' or 'Withdrawal'), and an operation value. The function should check if the balance of any account goes below zero or equals zero if `case_insensitive` is True and withdrawals and deposits are mixed case. It should raise exceptions for negative inputs for operation values and for non-existent account operations. Return True if any account balance goes below zero or equals zero, and False otherwise.
"""

from typing import List, Tuple

class FinancialException(Exception):
    """Exception to indicate financial operation errors"""

def below_zero(operations: List[Tuple[str, str, int]], case_insensitive: bool = False) -> bool:
    balances = {}

    for operation in operations:
        account, op_type, amount = operation
        account = account.lower() if case_insensitive else account

        if op_type.upper() not in ["DEPOSIT", "WITHDRAWAL"]:
            raise FinancialException(f"Unsupported operation: {op_type} for account holder: {account}")
        if amount < 0:
            raise FinancialException(f"Negative amount error: {amount} for account holder: {account}")
        if account not in balances:
            balances[account] = 0

        if op_type.lower() == "deposit":
            balances[account] += amount
        else:
            balances[account] -= amount

        if balances[account] <= 0:
            return True
    return False