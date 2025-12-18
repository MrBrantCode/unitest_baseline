"""
QUESTION:
Write a function named `fibonacci` that takes an integer `n` as input and returns the nth Fibonacci number. The function should be recursive and should not use any form of caching or memoization. If the input `n` is negative or not an integer, the function should return `None`.
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