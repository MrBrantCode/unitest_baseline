"""
QUESTION:
Implement a function `fib(n, fib_cache)` that generates the nth Fibonacci number in a sequence where the first two numbers are stored in the `fib_cache` dictionary. The function should use memoization to store previously computed Fibonacci numbers in the `fib_cache` dictionary to avoid redundant calculations.
"""

def fib(n, fib_cache):
    if n in fib_cache:
        return fib_cache[n]
    else:
        fib_cache[n] = fib(n-1, fib_cache) + fib(n-2, fib_cache)
        return fib_cache[n]