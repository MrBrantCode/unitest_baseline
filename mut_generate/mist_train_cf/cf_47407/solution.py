"""
QUESTION:
Write a function called `determinant` that calculates the determinant of a 3x3 matrix using the formula det(A) = a(ei - fh) - b(di - fg) + c(dh - eg), where the input matrix is a 3x3 list of lists of integers. The function should return the determinant value.
"""

def determinant(matrix):
    """
    This function calculates the determinant of a 3x3 matrix using the formula:
    det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
    
    Args:
        matrix (list of lists): A 3x3 list of lists of integers.
    
    Returns:
        int: The determinant value of the input matrix.
    """
    a = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
    b = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
    c = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    det = a - b + c
    return det