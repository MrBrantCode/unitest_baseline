"""
QUESTION:
Implement the `transpose_matrix` function to transpose a given 2D matrix, converting its rows into columns and vice versa. The function should take a 2D matrix as input and return its transposed form. The function must be able to handle matrices of any size.
"""

def transpose_matrix(matrix):
    transposed_matrix = []
    for i in range(len(matrix[0])):
        transposed_matrix.append([row[i] for row in matrix])
    return transposed_matrix