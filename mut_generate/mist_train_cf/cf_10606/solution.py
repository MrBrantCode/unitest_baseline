"""
QUESTION:
Write a recursive function `sum_of_numbers` that calculates the sum of the first `n` natural numbers. The function should take an integer `n` as input and return the sum of all natural numbers from 1 to `n`. The function should handle non-positive inputs by returning 0.
"""

def sum_of_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_numbers(n-1)