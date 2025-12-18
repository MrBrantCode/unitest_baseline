"""
QUESTION:
Write a Python function named `subtract_matrices` that takes two matrices `mat1` and `mat2` as input, where each matrix is a 2D list of integers with values between 0 and 100 (inclusive). The function should return a new matrix representing the element-wise subtraction of `mat1` and `mat2`. If the input matrices do not have the same dimensions, the function should return an error message.
"""

def subtract_matrices(mat1, mat2):
    # Check if both matrices have the same dimensions.
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Error: The matrices must have the same dimensions."

    # Subtract the matrices.
    res = [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return res