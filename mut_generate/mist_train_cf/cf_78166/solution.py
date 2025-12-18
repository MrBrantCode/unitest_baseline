"""
QUESTION:
Create a function `is_symmetric(matrix)` that determines whether a given matrix is symmetric or not. The function should be able to handle matrices of any size, including non-square matrices, as well as matrices with negative numbers and zero. A symmetric matrix is a square matrix that is equal to its transpose. The function should return `False` if the matrix is not a square matrix, and `True` if the matrix is symmetric, otherwise return `False`.
"""

def is_symmetric(matrix):
    # Check if the matrix is a square
    if len(matrix) != len(matrix[0]):
        return False
    # Check for symmetry
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True