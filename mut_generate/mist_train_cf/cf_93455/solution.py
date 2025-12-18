"""
QUESTION:
Write a function called `transpose_matrix` that takes a square 2D array of binary strings as input. The function should convert each binary string to its decimal equivalent and return a new 2D array where the rows of the input matrix are transposed to columns. The dimensions of the output matrix should be the same as the input matrix.
"""

def transpose_matrix(inputMatrix):
    n = len(inputMatrix)
    transposedMatrix = [[0] * n for _ in range(n)]

    for j in range(n):
        for i in range(n):
            decimalValue = int(inputMatrix[i][j], 2)
            transposedMatrix[j][i] = decimalValue

    return transposedMatrix