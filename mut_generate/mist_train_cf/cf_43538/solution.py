"""
QUESTION:
Write a function named `factorial(n)` that takes a positive integer `n` as input and returns the product of all positive integers from 1 to `n` (inclusive). The input `n` is obtained from the user. If the user input is not a positive integer, display an error message and do not proceed with the calculation.
"""

def factorial(n):
    """
    Function to compute the factorial of a given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)