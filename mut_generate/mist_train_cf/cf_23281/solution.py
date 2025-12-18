"""
QUESTION:
Write a function `transpose(matrix)` that calculates the transpose of a given m x n matrix. The input matrix is represented as a 2D list, where m is the number of rows and n is the number of columns. The function should return the transposed matrix as a 2D list. The input matrix is not empty and all rows have the same number of elements.
"""

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]