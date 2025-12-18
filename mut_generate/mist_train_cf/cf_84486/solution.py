"""
QUESTION:
Create a function named `multiplyMatrixByTwo` that takes a 2D matrix `y` as input, containing both positive and negative integers. The function should multiply each element in the matrix by 2 using only bitwise shift operators and return the resulting matrix.
"""

def multiplyMatrixByTwo(y):
    for i in range(len(y)):
        for j in range(len(y[i])):
            y[i][j] = y[i][j] << 1
    return y