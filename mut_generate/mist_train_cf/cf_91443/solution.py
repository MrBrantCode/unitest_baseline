"""
QUESTION:
Create a function named `sum_of_numbers(n)` that calculates and returns the sum of the first `n` numbers using recursion, where `n` is a non-negative integer. The function should handle the base case where `n` is less than or equal to 0 and return 0 in that case.
"""

def entrance(n):
    if n <= 0:
        return 0
    else:
        return n + entrance(n-1)