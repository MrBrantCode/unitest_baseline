"""
QUESTION:
Write a function `transpose_matrix(matrix)` that takes a 2D matrix `matrix` as input, where the matrix is a list of lists and all inner lists have the same length. The function should return the transposed matrix, which is a new 2D matrix where the rows of the original matrix are converted into columns. The function should handle matrices of different dimensions and return the transposed matrix correctly.
"""

def transpose_matrix(matrix):
    # Get the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0])  

    # Create a new matrix to store the transposed elements
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Iterate through the original matrix and fill the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed