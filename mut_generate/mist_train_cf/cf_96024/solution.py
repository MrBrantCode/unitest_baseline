"""
QUESTION:
Write a function named `factorial` that takes a positive integer `n` as input, where `n` is less than or equal to 20, and returns the factorial of `n` using a recursive algorithm.
"""

def entance(n):
    if n == 0:
        return 1
    else:
        return n * entance(n-1)