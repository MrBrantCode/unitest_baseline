"""
QUESTION:
Write a function named `multiply_matrices` that takes two matrices `matrix1` and `matrix2` as input and returns their product. The function should be able to handle matrices of any size, as long as the number of columns in `matrix1` is equal to the number of rows in `matrix2`. The result should be a new matrix where the element at row `i` and column `j` is the dot product of the `i-th` row of `matrix1` and the `j-th` column of `matrix2`.
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