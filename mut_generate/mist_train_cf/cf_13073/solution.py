"""
QUESTION:
Create a function named `matrix_multiply(A, B)` that takes two matrices A and B as input and returns their product. The function should check if the number of columns in matrix A is equal to the number of rows in matrix B. If not, it should return the message "Matrices cannot be multiplied." Otherwise, it should perform matrix multiplication and return the resulting matrix. The input matrices A and B are represented as lists of lists where each inner list represents a row in the matrix.
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