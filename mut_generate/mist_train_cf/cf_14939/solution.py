"""
QUESTION:
Write a function `transpose_matrix` that takes a square 2D array of binary strings as input and returns the transposed matrix with each binary string converted to its corresponding decimal value. The input matrix is in column-major format and the output should be in row-major format.
"""

def transpose_matrix(inputMatrix):
    n = len(inputMatrix)
    transposedMatrix = [[0] * n for _ in range(n)]

    for j in range(n):
        for i in range(n):
            decimalValue = int(inputMatrix[i][j], 2)
            transposedMatrix[j][i] = decimalValue

    return transposedMatrix