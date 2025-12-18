"""
QUESTION:
Create a Python function named `matrix_mul(A, B)` that takes two matrices A and B as input and returns the result of matrix multiplication. The function should check if the number of columns in matrix A is equal to the number of rows in matrix B, and return nothing if the condition is not met. The function should then compute the cross products and summations for each corresponding set of elements to output the resultant matrix.
"""

def matrix_mul(A, B):
    # check if number of columns in A is equal to number of rows in B
    if len(A[0]) != len(B):
        print("Matrix Multiplication is not possible!")
        return
        
    # create a zero matrix with the size of the resulted matrix
    result = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    
    # iterate through rows of A
    for i in range(len(A)):
        # iterate through columns of B
        for j in range(len(B[0])):
            # iterate through rows of B (or columns of A)
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
                
    return result