"""
QUESTION:
Implement a function named `matrix_addition` that takes two sparse matrices `matrix1` and `matrix2` as input, where each matrix is represented as a two-dimensional array with the same number of rows and columns. The function should return the result of matrix addition. The time complexity should be O(n), where n is the total number of non-zero elements in the matrices, and the space complexity should be O(m + n), where m is the number of rows and n is the number of columns.
"""

def matrix_addition(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result