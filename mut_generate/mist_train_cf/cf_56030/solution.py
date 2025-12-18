"""
QUESTION:
Implement a function `minimum_balance` that takes a list of integers representing a series of bank account operations (positive for deposit and negative for withdrawal) and returns the minimum balance that occurred during these operations. If the balance never fell below zero, the function should return 0.

The function should have a time complexity of O(n), where n is the number of operations, and a space complexity of O(1).
"""

def minimum_balance(operations):
    balance = 0
    min_balance = 0
    for op in operations:
        balance += op
        if balance < min_balance:
            min_balance = balance
    return min_balance if min_balance < 0 else 0