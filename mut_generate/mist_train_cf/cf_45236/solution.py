"""
QUESTION:
Write a function `matrix_multiply` that performs matrix multiplication on two given matrices. The function should take two 2D lists (matrices) as input and return the resulting matrix. The matrices are guaranteed to be of compatible dimensions for multiplication. The function should handle the multiplication and return the resulting matrix.
"""

def matrix_multiply(A, B):
    """
    Performs matrix multiplication on two given matrices.

    Args:
        A (list): The first 2D list (matrix)
        B (list): The second 2D list (matrix)

    Returns:
        list: The resulting matrix
    """
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result