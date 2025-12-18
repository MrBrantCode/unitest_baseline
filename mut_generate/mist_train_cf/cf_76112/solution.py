"""
QUESTION:
Write a recursive function `factorial(n)` that takes an integer `n` as input and returns its factorial. The function should handle the base case where `n` is 0 or 1 and return 1. For `n` greater than 1, the function should call itself with the argument `n-1` and return the product of `n` and the result.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)