"""
QUESTION:
Write a function `matrix_mul(A, B)` that multiplies two 3x3 square matrices `A` and `B` and returns the result. The function should perform standard matrix multiplication and handle the matrices as 3x3 lists of lists, where each inner list represents a row in the matrix. Assume that the input matrices are valid 3x3 matrices.
"""

def matrix_mul(A, B):
    # Initialize a 3x3 result matrix with all elements set to 0
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Perform matrix multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result