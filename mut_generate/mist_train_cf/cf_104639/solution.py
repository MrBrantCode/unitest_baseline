"""
QUESTION:
Write a function called `factorial(n)` that calculates the factorial of a given number `n` without using the built-in factorial function or any external libraries. The function should handle cases where `n` is 0 or 1, and it should be able to calculate the factorial for any positive integer.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)