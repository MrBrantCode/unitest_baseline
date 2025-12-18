"""
QUESTION:
Write a function named `fibonacci(n)` that calculates the nth Fibonacci number using memoization. The function should be able to efficiently handle larger inputs by storing the results of previous computations and reusing them when the same input occurs again. The function should be designed to work with the input `n` in the range of 0 to 49.
"""

import functools

@functools.lru_cache(None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)