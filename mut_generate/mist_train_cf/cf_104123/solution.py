"""
QUESTION:
Create a function `matrix_multiply(matrixA, matrixB)` to multiply two matrices. The input matrices can have different dimensions but will always be compatible for multiplication. The function should return the resulting matrix.
"""

def entance(matrixA, matrixB):
    result = []
    for i in range(len(matrixA)):
        row = []
        for j in range(len(matrixB[0])):
            element = 0
            for k in range(len(matrixB)):
                element += matrixA[i][k] * matrixB[k][j]
            row.append(element)
        result.append(row)
    return result