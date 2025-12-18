"""
QUESTION:
Create a function `matrix_mul(A, B)` that multiplies two matrices A and B. The input matrices A and B must be valid for multiplication, i.e., the number of columns in A must be equal to the number of rows in B. The function should return the resulting matrix after multiplication. The input matrices A and B are 2D lists of integers or floats.
"""

def matrix_mul(A, B):
    num_rows_A = len(A)
    num_cols_A = len(A[0])
    num_rows_B = len(B)
    num_cols_B = len(B[0])
    
    assert num_cols_A == num_rows_B, 'Matrices are not m*n and n*p'

    result_matrix = [[0 for j in range(num_cols_B)] for i in range(num_rows_A)]

    for i in range(num_rows_A):
        for j in range(num_cols_B):
            for k in range(num_cols_A): 
                result_matrix[i][j] += A[i][k] * B[k][j]
    return result_matrix