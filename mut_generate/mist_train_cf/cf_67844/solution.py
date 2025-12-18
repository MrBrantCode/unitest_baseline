"""
QUESTION:
Create a function called `below_zero` that takes a list of integers representing banking transactions (credits and debits) starting with a balance of zero, and returns a tuple containing a boolean indicating whether the account balance goes below zero and the transaction number where this first occurs, or None if the balance never goes below zero. The transaction number is 1-indexed (i.e., the first transaction is numbered 1, not 0).
"""

def below_zero(operations):
    balance = 0
    for index, operation in enumerate(operations):
        balance += operation
        if balance < 0:
            return (True, index + 1)  # "+1" as transactions start from 1 not 0
    return (False, None)