"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given non-negative integer `n` using a single line of code and a recursive algorithm.
"""

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)