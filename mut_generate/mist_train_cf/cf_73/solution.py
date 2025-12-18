"""
QUESTION:
Implement a function `matrix_multiply` that takes two matrices `matrix1` and `matrix2` as input, both represented as lists of lists. The function should return the result of multiplying `matrix1` by `matrix2`. The implementation must use nested for loops, with the outer loop iterating over the rows of `matrix1` and the inner loop iterating over the columns of `matrix2`. The number of columns in `matrix1` must be equal to the number of rows in `matrix2`.
"""

def matrix_multiply(matrix1, matrix2):
    # Get the number of rows and columns of the matrices
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])
    
    # Create an empty result matrix with the same number of rows as matrix1 and the same number of columns as matrix2
    result = [[0] * cols2 for _ in range(rows1)]
    
    # Multiply the matrices using nested for loops
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result