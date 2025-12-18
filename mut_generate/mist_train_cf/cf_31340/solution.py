"""
QUESTION:
Write a function `transpose_matrix(matrix)` that takes a non-empty 2D list of integers `matrix` as input, where the number of rows may not be equal to the number of columns and does not contain any empty rows or columns, and returns its transpose, a 2D list where the rows and columns of the input matrix are swapped.
"""

from typing import List

def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    # Create a new matrix to store the transpose
    transposed_matrix = [[0 for _ in range(num_rows)] for _ in range(num_cols)]
    
    # Fill in the transposed matrix
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix