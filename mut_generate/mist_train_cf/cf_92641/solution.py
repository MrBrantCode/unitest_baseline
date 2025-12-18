"""
QUESTION:
Create a function named `matrix_multiply` that takes two 2D lists `A` and `B` as input, representing two matrices, and returns their product as a 2D list. The function should check if the number of columns in `A` matches the number of rows in `B`, and return an error message if they do not match. Otherwise, it should perform matrix multiplication and return the resulting matrix.
"""

def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        return "Matrices cannot be multiplied."
    else:
        result = [[0]*len(B[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        return result