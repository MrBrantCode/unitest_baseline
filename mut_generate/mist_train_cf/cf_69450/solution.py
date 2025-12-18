"""
QUESTION:
Create a function named `checking_system` that takes two lists, `bank_operations` and `operation_fees`, as input. `bank_operations` contains integers representing account transactions, where positive numbers denote deposits and negative numbers denote withdrawals. `operation_fees` contains floats representing the fees associated with each transaction. 

The function should return a tuple where the first element is a boolean indicating whether the account balance ever goes negative, and the second element is the final account balance after all transactions.

Assume the input lists are the same length, and each transaction fee is subtracted from the account balance after the corresponding transaction is applied.
"""

from typing import List, Tuple

def checking_system(bank_operations: List[int], operation_fees: List[float]) -> Tuple[bool, float]:
    account_balance = 0
    got_negative = False
    for op, fee in zip(bank_operations, operation_fees):
        account_balance += op - fee
        if account_balance < 0:
            got_negative = True
    return got_negative, account_balance