"""
QUESTION:
Write a function called `factorial` that calculates the factorial of a given integer `n` using a recursive algorithm and only one line of code. The function should return 1 if `n` is 0.
"""

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)