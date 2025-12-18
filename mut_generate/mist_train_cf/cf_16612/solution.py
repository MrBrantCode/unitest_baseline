"""
QUESTION:
Implement a function `determinant_4x4(matrix)` that calculates the determinant of a given 4x4 matrix without using any built-in matrix operations or libraries and without using recursion. The input matrix is a 2D list of integers or floats, where each inner list represents a row in the matrix. The function should return the determinant of the matrix as a float.
"""

def determinant_4x4(matrix):
    """
    Calculate the determinant of a given 4x4 matrix.

    Args:
    matrix (list of lists): A 2D list of integers or floats representing the matrix.

    Returns:
    float: The determinant of the matrix.
    """
    
    # Unpack the matrix elements
    a11, a12, a13, a14 = matrix[0]
    a21, a22, a23, a24 = matrix[1]
    a31, a32, a33, a34 = matrix[2]
    a41, a42, a43, a44 = matrix[3]

    # Calculate cofactors
    cofactor11 = a22 * (a33 * a44 - a34 * a43) - a23 * (a32 * a44 - a34 * a42) + a24 * (a32 * a43 - a33 * a42)
    cofactor12 = -(a21 * (a33 * a44 - a34 * a43) - a23 * (a31 * a44 - a34 * a41) + a24 * (a31 * a43 - a33 * a41))
    cofactor13 = a21 * (a32 * a44 - a34 * a42) - a22 * (a31 * a44 - a34 * a41) + a24 * (a31 * a42 - a32 * a41)
    cofactor14 = -(a21 * (a32 * a43 - a33 * a42) - a22 * (a31 * a43 - a33 * a41) + a23 * (a31 * a42 - a32 * a41))

    # Calculate determinant
    return a11 * cofactor11 - a12 * cofactor12 + a13 * cofactor13 - a14 * cofactor14