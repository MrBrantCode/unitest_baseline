"""
QUESTION:
Implement a function called `strassen_matrix_multiply` that takes two square matrices `a` and `b` with dimensions that are powers of 2 as input and returns their product using Strassen's Matrix multiplication algorithm. The function should handle the base case where the matrices are 1x1, split the matrices into quarters, apply the Strassen's formula, and combine the submatrices to form the resulting matrix. Use NumPy for matrix operations.
"""

import numpy as np

def strassen_matrix_multiply(a, b):
    # Base case: if the matrices are 1x1
    if len(a) == 1:
        return a * b
    
    # Splitting matrices into quarters
    a11, a12, a21, a22 = split_matrix(a)
    b11, b12, b21, b22 = split_matrix(b)
    
    # Applying the Strassen's formula
    p1 = strassen_matrix_multiply(a11 + a22, b11 + b22)  # p1 = (a11 + a22) * (b11 + b22)
    p2 = strassen_matrix_multiply(a21 + a22, b11)       # p2 = (a21 + a22) * (b11)
    p3 = strassen_matrix_multiply(a11, b12 - b22)       # p3 = (a11) * (b12 - b22)
    p4 = strassen_matrix_multiply(a22, b21 - b11)       # p4 = (a22) * (b21 - b11)
    p5 = strassen_matrix_multiply(a11 + a12, b22)       # p5 = (a11 + a12) * (b22)
    p6 = strassen_matrix_multiply(a21 - a11, b11 + b12)  # p6 = (a21 - a11) * (b11 + b12)
    p7 = strassen_matrix_multiply(a12 - a22, b21 + b22)  # p7 = (a12 - a22) * (b21 + b22)
    
    # Combining submatrices to form the resulting matrix
    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21 = p2 + p4
    c22 = p1 + p3 - p2 + p6
    
    # Combining submatrices into a single matrix
    return combine_matrices(c11, c12, c21, c22)

def split_matrix(matrix):
    rows, columns = matrix.shape
    row_mid = rows // 2
    col_mid = columns // 2
    
    return matrix[:row_mid, :col_mid], matrix[:row_mid, col_mid:], matrix[row_mid:, :col_mid], matrix[row_mid:, col_mid:]

def combine_matrices(c11, c12, c21, c22):
    top = np.concatenate((c11, c12), axis=1)
    bottom = np.concatenate((c21, c22), axis=1)
    
    return np.concatenate((top, bottom), axis=0)