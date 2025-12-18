"""
QUESTION:
Write a function named `multiply_matrices` that takes two matrices as input and returns their product. The number of columns in the first matrix must be equal to the number of rows in the second matrix. The function should return a new matrix where each element at position (i, j) is the sum of the products of the elements at position (i, k) of the first matrix and position (k, j) of the second matrix.
"""

def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result