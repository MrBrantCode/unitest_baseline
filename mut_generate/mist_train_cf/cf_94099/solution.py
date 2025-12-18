"""
QUESTION:
Implement a function `factorial(n)` that calculates the factorial of a given non-negative integer `n` using recursion. The function should handle edge cases where `n` is negative, returning `None` in such cases, and where `n` is 0, returning 1.
"""

def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)