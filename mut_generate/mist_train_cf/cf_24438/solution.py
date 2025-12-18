"""
QUESTION:
Implement a function named `strassen` that multiplies two square matrices using Strassen's Matrix multiplication algorithm. The input matrices must be square and their dimensions must be powers of 2.
"""

import numpy as np

def strassen(A, B):
    """
    This function multiplies two square matrices A and B using Strassen's Matrix multiplication algorithm.
    
    Parameters:
    A (numpy array): The first input matrix
    B (numpy array): The second input matrix
    
    Returns:
    numpy array: The result of the matrix multiplication
    """
    
    # Get the size of the matrices
    n = A.shape[0]
    
    # Base case: If the matrices are 1x1, return their product
    if n == 1:
        return A * B
    
    # Split the matrices into four sub-matrices of size n/2 x n/2
    mid = n // 2
    A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]
    
    # Calculate the seven products needed for Strassen's algorithm
    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)
    
    # Calculate the elements of the resulting matrix
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6
    
    # Combine the sub-matrices into the resulting matrix
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    
    return C