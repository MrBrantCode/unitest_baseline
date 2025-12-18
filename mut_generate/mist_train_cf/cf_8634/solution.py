"""
QUESTION:
Write a function named `rotate_matrix` that takes a square matrix of integers as input and returns two new matrices representing the clockwise and counterclockwise rotations of the input matrix by 90 degrees. The input matrix size will be between 1x1 and 100x100, and the elements will be integers between -1000 and 1000. The function should have a time complexity of O(n^2) or better, use constant space, and preserve the original matrix.
"""

def rotate_matrix(matrix):
    """
    Rotate a square matrix by 90 degrees in both clockwise and counterclockwise directions.

    Args:
    matrix (list of lists): A square matrix of integers.

    Returns:
    tuple of lists of lists: Two new matrices representing the clockwise and counterclockwise rotations of the input matrix.
    """
    n = len(matrix)
    # Initialize empty matrices for clockwise and counterclockwise rotations
    clockwise_matrix = [[0] * n for _ in range(n)]
    counterclockwise_matrix = [[0] * n for _ in range(n)]

    # Perform rotations
    for i in range(n):
        for j in range(n):
            clockwise_matrix[j][n - 1 - i] = matrix[i][j]
            counterclockwise_matrix[n - 1 - j][i] = matrix[i][j]

    return clockwise_matrix, counterclockwise_matrix