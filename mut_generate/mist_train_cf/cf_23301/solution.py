"""
QUESTION:
Write a function `matrix_multiply` that takes two NxN matrices A and B as input and returns their product. The function should assume that the input matrices are valid for multiplication, i.e., they have the same number of rows and columns. The output should be a new NxN matrix where each element at position (i, j) is the sum of the products of the elements from row i of matrix A and column j of matrix B.
"""

def matrix_multiply(A, B):
    # Get the size of the matrices
    N = len(A)

    # Create an NxN matrix result, initialized to 0
    result = [[0 for _ in range(N)] for _ in range(N)]

    # loop through matrix A and B
    for i in range(N):
        for j in range(N):
            for k in range(N):
                # multiply the elements of A and B
                result[i][j] += A[i][k] * B[k][j]

    # return the result matrix
    return result