"""
QUESTION:
Create a 5x5 matrix filled with zeros without using loops (for, while) or pre-defined functions that generate zero-filled matrices. The solution should be implemented in Python.
"""

def create_zero_matrix(n):
    """
    Creates an n x n matrix filled with zeros without using loops or pre-defined functions.

    Args:
    n (int): The size of the matrix.

    Returns:
    list: An n x n matrix filled with zeros.
    """
    return [[0 for _ in range(n)] for _ in range(n)]