"""
QUESTION:
Implement a function `sqrt(n)` to compute the integer square root of a given non-negative integer `n` without using the built-in square root function. The function should return the largest integer whose square is less than or equal to `n`.
"""

def sqrt(n):
    """
    Compute the square root of a given number
    """
    r = n
    while r*r > n:
        r = (r + n/r) // 2
    return r