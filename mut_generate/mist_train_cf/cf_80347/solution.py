"""
QUESTION:
Write a function `account_activities` that takes two parameters: `operations` and `fees`, both of which are lists of lists of integers and floats respectively. Each sublist in `operations` and `fees` represents a bank account's operations and corresponding fees respectively. Return a list of tuples, where each tuple contains a boolean indicating whether the account balance went negative at any point after applying the fees, and the final account balance rounded to two decimal places.
"""

from typing import List, Tuple

def account_activities(operations: List[List[int]], fees: List[List[int]]) -> List[Tuple[bool, float]]:
    result = []
    for operation, fee in zip(operations, fees):
        balance = 0
        goes_negative = False
        for op, fee in zip(operation, fee):
            balance += op - fee
            if balance < 0:
                goes_negative = True
        result.append((goes_negative, round(balance, 2)))
    return result