"""
QUESTION:
Create a function named `transpose` that takes a 2D array (MxN matrix) as input and returns its transposed matrix. The function should not use any built-in transpose function or method, and it should handle matrices of any size.
"""

def transpose(matrix):
    tr_matrix = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            tr_matrix[j][i] = col
    return tr_matrix