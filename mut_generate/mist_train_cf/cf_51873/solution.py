"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given non-negative integer `n` efficiently, considering multiple calls with the same argument. The function should utilize memoization to store previously calculated factorial values to minimize redundant computations.
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)