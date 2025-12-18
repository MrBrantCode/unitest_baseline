"""
QUESTION:
Write a function named mat_mult that takes two 3x3 matrices X and Y as input and returns the result of the matrix multiplication. The function should not use any built-in matrix multiplication functions and should only use nested loops to perform the multiplication.
"""

def mat_mult(X, Y):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result