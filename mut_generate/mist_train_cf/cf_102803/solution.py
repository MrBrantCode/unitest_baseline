"""
QUESTION:
Write a recursive function `factorial(n)` in Python that calculates the factorial of a given positive integer `n`. The function should only take one argument `n` and return the factorial of `n`. The function should not include any error handling or input validation for non-positive integers or non-integer inputs.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)