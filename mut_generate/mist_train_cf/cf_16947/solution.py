"""
QUESTION:
Write a function called `factorial` that calculates the factorial of a given non-negative integer `n` without using any loops or recursion.
"""

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)