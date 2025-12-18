"""
QUESTION:
Create a function called `matrix_mul(A, B)` that takes two matrices `A` and `B` as input. The function should multiply `A` and `B` without using any external libraries, and return the resulting matrix. The matrices are guaranteed to have compatible dimensions for multiplication (i.e., the number of columns in `A` equals the number of rows in `B`).
"""

def matrix_mul(A, B):
    result = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result