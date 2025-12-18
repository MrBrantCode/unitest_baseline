"""
QUESTION:
Write a Python function named `last_nonzero_digit` that takes an integer `n` as input and returns the last non-zero digit in the factorial of `n`. The function should handle cases where `n` is less than 0. It should also avoid directly calculating the entire factorial to prevent overflow errors, especially for large input values.
"""

def last_nonzero_digit(n):
    if n < 0:
        return None
    arr = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]
    res = 1
    for i in range(n, 0, -1):
        while i % 10 == 0:
            i //= 10
        res *= i % 10
        while res % 10 == 0:
            res //= 10
        res %= 10
    return res