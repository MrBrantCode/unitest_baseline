"""
QUESTION:
Write a recursive function `fibonacci(n)` that calculates the nth Fibonacci number. The function should handle edge cases where the input `n` is negative or not an integer, and return `None` in these cases. The function should not use any form of caching or memoization to improve performance.
"""

def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        return None

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)