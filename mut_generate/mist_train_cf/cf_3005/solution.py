"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a positive integer `n` without using loops or the multiplication operator. The function should return the factorial if `n` is a non-negative integer, and an error message if `n` is negative.
"""

def entance(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Factorial is not defined for negative numbers."
    else:
        return n * entance(n - 1)