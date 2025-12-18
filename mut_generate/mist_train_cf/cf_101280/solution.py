"""
QUESTION:
Create a function called `factorial` that calculates the factorial of a given integer `n` using recursion. The function should return the factorial of `n` as an integer. The input `n` will be a non-negative integer.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)