"""
QUESTION:
Implement a recursive function named `factorial` that takes an integer `n` as input and returns its factorial, which is the product of all positive integers less than or equal to `n`, without using any iterative loops.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)