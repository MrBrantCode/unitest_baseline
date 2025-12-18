"""
QUESTION:
Write a recursive function named `factorial` that takes a positive integer `n` as input and returns its factorial. The function should handle the base case where `n` is 0 or 1.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)