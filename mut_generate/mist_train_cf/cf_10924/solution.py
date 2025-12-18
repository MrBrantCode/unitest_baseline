"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given non-negative integer `n` using recursion. The function should return the factorial of `n` without using loops or built-in factorial functions.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)