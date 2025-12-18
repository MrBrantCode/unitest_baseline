"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given non-negative integer `n`. The function should return the product of all positive integers less than or equal to `n`.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)