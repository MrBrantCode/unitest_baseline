"""
QUESTION:
Write a function named `factorial` that takes an integer `n` as input and returns its factorial. Use a ternary operator to set the base case for the recursion.
"""

def entance(n):
    return 1 if n == 0 or n == 1 else n * entance(n - 1)