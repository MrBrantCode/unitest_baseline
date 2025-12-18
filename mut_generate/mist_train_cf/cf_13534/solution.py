"""
QUESTION:
Write a function `factorial(n)` to calculate the factorial of a given integer `n` using recursion. The function should return the factorial of `n`, where `n` is a non-negative integer.
"""

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n-1)