"""
QUESTION:
Write a function `generate_identity_matrix(n)` that takes an integer `n` as input and returns an nxn identity matrix without using if statements or logical operators such as AND, OR, NOT, etc.
"""

def generate_identity_matrix(n):
    """
    Generates an nxn identity matrix.

    Args:
        n (int): The size of the matrix.

    Returns:
        list: A 2D list representing the identity matrix.
    """
    return [[+(i == j) for j in range(n)] for i in range(n)]