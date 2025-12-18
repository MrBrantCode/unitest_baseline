"""
QUESTION:
Create a function `matrix_mult(matrixA, matrixB)` that performs matrix multiplication of two 2D arrays. The function should take two 2x2 matrices `matrixA` and `matrixB` as input and return their product, where each element of the result matrix is the sum of the products of corresponding elements from a row in `matrixA` and a column in `matrixB`. The function should only work for 2x2 matrices.
"""

def matrix_mult(matrixA, matrixB):
    # Initialize a result matrix with zeroes
    result = [[0, 0], 
              [0, 0]]

    # Iterate through rows of matrixA
    for i in range(len(matrixA)):
       # Iterate through columns of matrixB
       for j in range(len(matrixB[0])):
           # Iterate through rows of matrixB
           for k in range(len(matrixB)):
               result[i][j] += matrixA[i][k] * matrixB[k][j]

    return result