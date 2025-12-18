"""
QUESTION:
Create a function `cache_func` that uses `functools.lru_cache` to memoize another function. The provided function to be memoized is `fibonacci(n)`, a recursive function that calculates the nth Fibonacci number. Use the `cache_func` to decorate the `fibonacci` function. The `fibonacci` function should correctly calculate the nth Fibonacci number after being memoized. Restriction: the solution must use the `functools.lru_cache` function for memoization.
"""

import functools

@functools.lru_cache(maxsize=None)  
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)