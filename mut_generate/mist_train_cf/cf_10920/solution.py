"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a given positive integer `n`. The function should return an error message if `n` is not a positive integer. The maximum recursion depth should not exceed 1000.
"""

import sys
sys.setrecursionlimit(1000)

def factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Input should be a positive integer."
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)