"""
QUESTION:
Define a function `cross_multiply(matrix1, matrix2)` that takes two non-square NumPy matrices as input and returns their cross product if the number of columns in `matrix1` equals the number of rows in `matrix2`. If the matrices are incompatible for multiplication, return an error message. The function should handle large matrices efficiently without causing memory overflow or excessive computation time.
"""

import numpy as np

def cross_multiply(matrix1, matrix2):
    rows_matrix1, cols_matrix1 = np.shape(matrix1)
    rows_matrix2, cols_matrix2 = np.shape(matrix2)
    
    if cols_matrix1 != rows_matrix2:
        return "Error: The number of columns in the first matrix must equal the number of rows in the second matrix for multiplication."
    
    result = np.dot(matrix1, matrix2)
    
    return result