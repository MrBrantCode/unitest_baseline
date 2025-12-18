"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given non-negative integer `n` using recursion, where the factorial of 0 is defined as 1. The function should return the result of the factorial calculation.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)