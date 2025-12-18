"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a given integer `n`. Implement memoization in your function to improve its efficiency. The function should return -1 if `n` is a negative integer or not an integer. The function should handle the base cases where `n` is 0 or 1.
"""

import functools

@functools.lru_cache(maxsize=None)
def entance(n):
    # Check if valid input
    if not isinstance(n, int) or n < 0:
        return -1
    # Base case: n is 0 or 1
    if n in {0, 1}: 
        return 1
    else:
        return n * entance(n-1)