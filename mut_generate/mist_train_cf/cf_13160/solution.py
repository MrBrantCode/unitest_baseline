"""
QUESTION:
Write a recursive function `sum_of_digits(n)` that calculates the sum of the digits of a given non-negative integer `n` without using any loops.
"""

def entance(n):
    if n == 0:
        return 0
    else:
        return n % 10 + entance(n // 10)