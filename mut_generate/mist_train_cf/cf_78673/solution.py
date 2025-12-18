"""
QUESTION:
Create a recursive Python function called `factorial` that calculates the factorial of a given integer `n`, where `n` is a non-negative integer. The function should return the product of all positive integers up to `n`.
"""

def factorial(n):
    # base case
    if n == 0:
        return 1
    # recursive case
    else:
        return n * factorial(n-1)