"""
QUESTION:
Write a function named `matrix_multiply` that takes two matrices A and B as input. The function should return their product matrix if the matrices can be multiplied, and an error message otherwise. The time complexity of the function should be O(n^3) and the space complexity should be O(m * n), where n is the size of the matrix, and m and n are the dimensions of the matrices.
"""

def matrix_multiply(A, B):
    """
    This function multiplies two matrices A and B.
    
    Args:
    A (list of lists): The first matrix.
    B (list of lists): The second matrix.
    
    Returns:
    list of lists: The product matrix of A and B if the matrices can be multiplied, 
    otherwise it returns an error message.
    """
    
    # Get the dimensions of the matrices
    num_rows_A = len(A)
    num_cols_A = len(A[0])
    num_rows_B = len(B)
    num_cols_B = len(B[0])
    
    # Validate the dimensions of matrices A and B
    if num_cols_A != num_rows_B:
        return "Error: The number of columns in A is not equal to the number of rows in B."
    
    # Create an empty result matrix C
    C = [[0 for _ in range(num_cols_B)] for _ in range(num_rows_A)]
    
    # Perform matrix multiplication
    for i in range(num_rows_A):
        for j in range(num_cols_B):
            for k in range(num_cols_A):  # or 'num_rows_B'
                C[i][j] += A[i][k] * B[k][j]
    
    return C