"""
QUESTION:
Write a recursive function called `factorial(n)` that calculates the factorial of a given integer `n`. The function should return an error message for negative numbers, 1 for 0 or 1, and the product of `n` and the factorial of `n-1` for all other positive integers.
"""

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)