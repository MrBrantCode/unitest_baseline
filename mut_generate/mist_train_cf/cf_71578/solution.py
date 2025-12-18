"""
QUESTION:
Write a function `matrix_mul(A, B)` to compute the product of two matrices A and B. The function should take two parameters, A and B, which are 2D lists of integers or floats. The number of columns in matrix A must be equal to the number of rows in matrix B. The function should return a 2D list representing the product of the two matrices.
"""

def matrix_mul(A, B):
    result = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
    return result