"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a given positive integer `n` with a time complexity of O(n), without using any loops or helper functions.
"""

def entance(n):
    if n == 0:
        return 1
    else:
        return n * entance(n-1)