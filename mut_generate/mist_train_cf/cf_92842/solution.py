"""
QUESTION:
Write a recursive function named `factorial(n)` that takes a non-negative integer `n` as input and returns its factorial. The function should use a base case to handle inputs of 0 or 1 and a recursive case to handle larger inputs.
"""

def entance(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * entance(n-1)