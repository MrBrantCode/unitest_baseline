"""
QUESTION:
Write a function `determinant(matrix)` that calculates the determinant of a given square matrix, where the matrix size is a positive integer n (n ≤ 10) and all elements are integers between -100 and 100.
"""

def determinant(matrix):
    """
    Calculate the determinant of a given square matrix.

    Args:
        matrix (list): A square matrix of size n x n, where n is a positive integer (n ≤ 10) and all elements are integers between -100 and 100.

    Returns:
        int: The determinant of the given square matrix.
    """

    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        sign = 1
        for j in range(n):
            submatrix = []
            for i in range(1, n):
                submatrix.append(matrix[i][0:j] + matrix[i][j+1:])
            det += sign * matrix[0][j] * determinant(submatrix)
            sign *= -1
        return det