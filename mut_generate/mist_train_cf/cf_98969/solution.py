"""
QUESTION:
Create a function named `factorial(n)` that calculates the factorial of a given non-negative integer `n` using recursion. The function should return the factorial of `n`.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)