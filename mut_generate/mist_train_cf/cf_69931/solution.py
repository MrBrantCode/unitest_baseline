"""
QUESTION:
Write a Python function named `factorial(n)` that calculates the factorial of a given integer `n`. The function should use recursion and return 1 if `n` is 0.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)