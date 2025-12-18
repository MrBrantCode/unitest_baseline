"""
QUESTION:
Implement a recursive function `factorial` in Python that calculates the factorial of a given positive integer `n`, with `n` as the only function argument. The function should return the factorial of `n`.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)