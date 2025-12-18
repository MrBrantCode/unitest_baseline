"""
QUESTION:
Write a function `below_zero` that determines if a bank account's balance goes below zero after a series of deposit and withdrawal operations, considering transaction charges. The function should take a list of tuples in the format `(operation_type, operation_value, fee)` and two boolean flags `case_insensitive` and `fee_included`. The function should handle invalid transactions and return an error message. The function should return a boolean value indicating whether the balance goes below zero, or an error message if an invalid transaction is encountered.
"""

from typing import List, Tuple, Union

def below_zero(operations: List[Tuple[str, int, float]], case_insensitive: bool = False, fee_included: bool = False) -> Union[bool, str]:
    balance = 0
    for op in operations:
        tType, tValue, tFee = op
        if case_insensitive:
            tType = tType.lower()
        if tType not in ['deposit', 'withdraw']:
            return f"Invalid transaction type {tType}"
        if tType == 'deposit':
            balance += tValue
        else:  # assume 'withdraw'
            if balance < tValue:
                return True
            if fee_included:
                balance -= (tValue + tFee)
            else:
                balance -= tValue

    return balance < 0