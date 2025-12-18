"""
QUESTION:
Create a function named `factorial` that takes a single positive integer `n` and returns its factorial. Use this function to generate a new sequence where each individual element from the given sequence is replaced by its factorial.
"""

def entance(n):
    if n == 0:
        return 1
    else:
        return n * entance(n-1)