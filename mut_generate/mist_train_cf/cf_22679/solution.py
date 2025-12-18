"""
QUESTION:
Design a function called `multiply_matrices(A, B)` that takes two matrices A and B as input and returns their product matrix. The function should first validate the dimensions of the input matrices to ensure they can be multiplied. If the matrices cannot be multiplied, the function should return an error message. The time complexity of the function should be O(n^2), where n is the size of the matrix. Additionally, the function should have an optimized solution with a space complexity of O(1), where the original values in matrix A are overwritten with the result.
"""

def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        return "Error: The matrices cannot be multiplied."

    # Multiply matrices
    for i in range(rows_A):
        for j in range(cols_B):
            C_ij = 0
            for k in range(cols_A):
                C_ij += A[i][k] * B[k][j]
            A[i][j % cols_A] = C_ij

    return A