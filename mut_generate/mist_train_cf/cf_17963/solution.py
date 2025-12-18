"""
QUESTION:
Write a function named `calculate_determinant` to calculate the determinant of a given square matrix of size n x n, where n is a positive integer. The function should take a 2D list of integers as input and return the determinant of the matrix.
"""

def calculate_determinant(matrix):
    """
    Calculate the determinant of a given square matrix of size n x n.

    Args:
        matrix (list): A 2D list of integers representing the square matrix.

    Returns:
        int: The determinant of the matrix.
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(n):
            minor = [row[:i] + row[i+1:] for row in matrix[1:]]
            det += ((-1) ** i) * matrix[0][i] * calculate_determinant(minor)
        return det