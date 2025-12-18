"""
QUESTION:
Write a function `recursive` that takes an integer `n` as input and returns the sum of all integers from `n` down to 1, or 0 if `n` is 0. Implement this function using recursion.
"""

def recursive(n):
    """Returns the sum of all integers from n down to 1, or 0 if n is 0."""
    if n == 0:
        return 0
    else:
        return n + recursive(n-1)