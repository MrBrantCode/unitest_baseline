"""
QUESTION:
Write a function `below_zero` that takes a list of operations and two optional boolean flags. Each operation is a tuple of three elements: a string describing the type of operation (either 'deposit' or 'withdraw'), an integer describing the value of the operation, and a float describing the transaction fee. The function returns `True` if the balance falls below zero at any point, `False` otherwise, or an error message if an invalid operation is encountered. The `case_insensitive` flag makes the function disregard the casing of the operation type, and the `fee_included` flag makes the function subtract the transaction fee from the balance for each operation.
"""

from typing import List, Tuple, Union

def below_zero(operations: List[Tuple[str, int, float]], case_insensitive: bool = False, fee_included: bool = False) -> Union[bool, str]:
    balance = 0
    for operation in operations:
        op_type, op_value, fee = operation
        if case_insensitive:
            op_type = op_type.lower()
        if op_type == 'deposit':
            balance += op_value
            if fee_included:
                balance -= fee
        elif op_type == 'withdraw':
            balance -= op_value
            if fee_included:
                balance -= fee
        else:
            return 'Invalid operation'

        if balance < 0:
            return True

    return False