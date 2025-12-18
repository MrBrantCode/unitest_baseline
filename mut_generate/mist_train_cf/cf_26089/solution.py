"""
QUESTION:
Create a function `generate_matrix(n)` that takes a positive integer `n` as input and returns an nxn matrix filled with numbers counting up from 1 to n^2.
"""

def generate_matrix(n):
    """Returns an nxn matrix filled with numbers counting up from 1 to n^2."""
    return [[i*n + j + 1 for j in range(n)] for i in range(n)]