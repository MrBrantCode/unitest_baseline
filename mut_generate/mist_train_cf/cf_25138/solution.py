"""
QUESTION:
Compute the factorial of a given non-negative integer using recursion.

Create a function named `factorial(n)` that takes a non-negative integer `n` as input and returns its factorial. The function must use recursion to calculate the result.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)