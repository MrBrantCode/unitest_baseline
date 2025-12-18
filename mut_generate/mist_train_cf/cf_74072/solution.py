"""
QUESTION:
Implement a function `matrixMultiply(X, Y)` that takes two 3x3 matrices `X` and `Y` as input and returns their product. The function should not use any external libraries and should optimize the algorithm to reduce time complexity. It should also include exception handling to handle cases where the input matrices cannot be multiplied together due to incompatible dimensions.
"""

def matrix_multiply(X, Y):
    # Check if matrices are eligible for multiplication
    if len(X[0]) != len(Y):
        raise Exception("The matrices cannot be multiplied.")

    # Create a new matrix of zeroes with shape as (rows of X, columns of Y)
    result = [[0 for j in range(len(Y[0]))] for i in range(len(X))]

    # Perform matrix multiplication
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    return result