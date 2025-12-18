"""
QUESTION:
Write a function `add_to_identity_matrix` that takes a 3x3 matrix as input and returns the result of adding the input matrix to the 3x3 identity matrix. The function should return a new 3x3 matrix where each element at position (i, j) is the sum of the corresponding elements in the input matrix and the identity matrix.
"""

def add_to_identity_matrix(matrix):
    """
    Adds the input matrix to the 3x3 identity matrix.

    Args:
    matrix (list): A 3x3 matrix.

    Returns:
    list: The result of adding the input matrix to the 3x3 identity matrix.
    """
    identity_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    result_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(len(identity_matrix)):
        for j in range(len(identity_matrix[0])):
            result_matrix[i][j] = identity_matrix[i][j] + matrix[i][j]

    return result_matrix