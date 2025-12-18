"""
QUESTION:
Write a function `transposeDiagonal(matrix)` that takes a square matrix of integers as input and returns the transposed matrix diagonally from top-left to bottom-right, swapping the elements at mirror image positions across the diagonal. The input matrix is a list of lists where the number of rows equals the number of columns.
"""

def transposeDiagonal(matrix):
    n = len(matrix) 
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix