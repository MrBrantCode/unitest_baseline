"""
QUESTION:
Create a Python function `fibonacci_memoized` that takes a non-negative integer `n` as input and returns the `n`-th Fibonacci number. The Fibonacci sequence is defined such that the first two numbers are 0 and 1, and each subsequent number is the sum of the two preceding ones. Implement the function using the `lru_cache` decorator to efficiently compute the `n`-th Fibonacci number. The function should cache the results of previous function calls to improve performance.
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memoized(n):
    if n <= 1:
        return n
    else:
        return fibonacci_memoized(n-1) + fibonacci_memoized(n-2)