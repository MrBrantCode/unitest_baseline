"""
QUESTION:
Write a function called `nullity` that takes a matrix `A` as input and returns the dimension of its null space. The dimension of the null space, or nullity of a matrix, is the maximum number of linearly independent vectors in the null space of the matrix, which can be calculated using the formula: `Nullity(A) = n - Rank(A)`, where `n` is the number of columns in `A`.
"""

import numpy as np

def nullity(A):
    """
    This function calculates the dimension of the null space of a given matrix A.
    
    Parameters:
    A (numpy array): Input matrix.
    
    Returns:
    int: Dimension of the null space of A.
    """
    
    # Calculate the rank of matrix A
    rank_A = np.linalg.matrix_rank(A)
    
    # Calculate the number of columns in matrix A
    n = A.shape[1]
    
    # Calculate the nullity of matrix A using the formula: Nullity(A) = n - Rank(A)
    nullity_A = n - rank_A
    
    return nullity_A