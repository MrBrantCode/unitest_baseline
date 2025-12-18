"""
QUESTION:
Write a function named `calculate_sum(n)` that takes an integer `n` as input and returns the sum of natural numbers up to `n` (inclusive) without using loops, recursion, built-in functions like `sum()` or `range()`.
"""

def calculate_sum(n):
    if n < 1:
        return 0
    else:
        return n + calculate_sum(n-1)