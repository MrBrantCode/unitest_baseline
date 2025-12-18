"""
QUESTION:
Write a function `calculate_determinant(matrix)` that calculates the determinant of a given 3x3 matrix. The function should take a 3x3 list of lists (or a 2D list) as input, where each inner list represents a row in the matrix, and return the calculated determinant. Assume the input matrix is a valid 3x3 matrix of integers or floats.
"""

def calculate_determinant(matrix):
    """
    Calculate the determinant of a 3x3 matrix.

    Args:
        matrix (list of lists): A 3x3 matrix represented as a 2D list.

    Returns:
        int or float: The determinant of the input matrix.
    """
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    
    return a * e * i + b * f * g + c * d * h - c * e * g - b * d * i - a * f * h