"""
QUESTION:
Write a recursive function `factorial(n)` in Python that calculates the factorial of a given positive integer `n`, where `n` is a non-negative integer. The function should return the product of all positive integers less than or equal to `n`.
"""

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)