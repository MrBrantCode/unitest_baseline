"""
QUESTION:
Write a recursive function named `factorial` that takes a positive integer `n` as input and returns its factorial. The function should only work for integers less than or equal to a certain number.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)