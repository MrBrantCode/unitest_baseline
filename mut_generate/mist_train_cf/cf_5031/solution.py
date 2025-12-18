"""
QUESTION:
Write a function `calculate_determinant(matrix)` that calculates the determinant of a given square matrix using the Laplace expansion method. The input matrix is a 2D list of integers, and its size is guaranteed to be between 1 and 10 (inclusive). You are not allowed to use any built-in functions or libraries to calculate the determinant.
"""

def calculate_determinant(matrix):
    """
    Calculate the determinant of a given square matrix using the Laplace expansion method.

    Args:
        matrix (list): A 2D list of integers representing a square matrix.

    Returns:
        int: The determinant of the given matrix.
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for i in range(n):
            submatrix = []
            for j in range(1, n):
                row = []
                for k in range(n):
                    if k != i:
                        row.append(matrix[j][k])
                submatrix.append(row)
            determinant += ((-1) ** i) * matrix[0][i] * calculate_determinant(submatrix)
        return determinant