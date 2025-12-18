"""
QUESTION:
Implement a function `multiply_matrices(mat1, mat2)` that multiplies two matrices represented as lists of lists. The function should check if the matrices can be multiplied (i.e., the number of columns in the first matrix is equal to the number of rows in the second matrix) and return the resulting matrix. If the matrices cannot be multiplied, the function should return an indication of this (e.g., a message or None).
"""

def multiply_matrices(mat1, mat2):
    # Find dimensions of input matrices
    rows_mat1 = len(mat1)
    cols_mat1 = len(mat1[0])
    rows_mat2 = len(mat2)
    cols_mat2 = len(mat2[0])

    # Check if matrices can be multiplied
    if cols_mat1 != rows_mat2:
        print("Matrices cannot be multiplied!")
        return

    # Create resulting matrix
    result = [[0 for _ in range(cols_mat2)] for _ in range(rows_mat1)]

    # Multiply two matrices
    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(cols_mat1): 
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result