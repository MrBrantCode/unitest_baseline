"""
QUESTION:
Write a function named null_space_dimension that calculates the dimension of the null space of a given matrix A. The function should take a 2D list or matrix A as input and return the dimension of the null space.
"""

import numpy as np

def null_space_dimension(A):
    # Convert the input matrix A to a numpy array
    A = np.array(A, dtype=float)
    
    # Perform Gaussian elimination to bring matrix A to row-reduced echelon form
    n_rows, n_cols = A.shape
    current_row = 0
    for j in range(n_cols):
        if current_row >= n_rows:
            break
        pivot_row = current_row
        while pivot_row < n_rows and A[pivot_row, j] == 0:
            pivot_row += 1
        if pivot_row == n_rows:
            continue
        A[[current_row, pivot_row]] = A[[pivot_row, current_row]]
        pivot = A[current_row, j]
        A[current_row] = A[current_row] / pivot
        for i in range(n_rows):
            if i != current_row:
                A[i] = A[i] - A[i, j] * A[current_row]
        current_row += 1
    
    # Count the number of zero rows (i.e., non-pivot columns) to find the null space dimension
    null_space_dim = n_cols - current_row
    
    return null_space_dim