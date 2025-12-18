"""
QUESTION:
Write a function `multiply_matrices(A, B)` that takes two matrices A and B as input and returns their product matrix. The function should first validate that the number of columns in matrix A is equal to the number of rows in matrix B. If the matrices cannot be multiplied, the function should return an error message. The function should have a time complexity of O(n^2), where n is the size of the matrix, and a space complexity of O(n^2) or optimized to O(1) if possible.
"""

def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        return "Error: The matrices cannot be multiplied."

    # Initialize result matrix C
    C = [[0] * cols_B for _ in range(rows_A)]

    # Multiply matrices
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C