"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a given integer `n`. The function should not use any loops and should return `1` when `n` is `0` or `1`.
"""

def entrance(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * entrance(n-1)