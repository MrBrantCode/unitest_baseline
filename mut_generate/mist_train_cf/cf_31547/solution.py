"""
QUESTION:
Implement a `factorial` function that calculates the factorial of a given non-negative integer `n`. The function should be able to handle large inputs without exceeding the maximum recursion depth. The function should take a non-negative integer `n` as input and return its factorial.
"""

import sys

def factorial(n: int) -> int:
    sys.setrecursionlimit(5000)  # Set a higher recursion limit to handle large inputs
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)