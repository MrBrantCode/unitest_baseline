"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given non-negative integer `n` using recursion. The function should return `1` if `n` is `0` or `1`, and the product of `n` and the factorial of `n - 1` otherwise.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)