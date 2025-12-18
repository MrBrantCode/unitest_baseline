"""
QUESTION:
Write a recursive function named `factorial` in Python that calculates the factorial of a non-negative integer `n`. The function should call itself until it reaches the base case where `n` equals 0 or 1, at which point it returns 1. For any other value of `n`, the function should return `n` multiplied by the factorial of `n-1`.
"""

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)