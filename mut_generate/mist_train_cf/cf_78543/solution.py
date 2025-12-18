"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given integer. The function should take one argument `n`, which is a non-negative integer. The function should return the factorial of `n`, which is the product of all positive integers up to `n`.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)