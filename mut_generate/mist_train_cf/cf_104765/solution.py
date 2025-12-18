"""
QUESTION:
Write a function called `matrix_sum` to compute the sum of two matrices A and B of size m x n, where each matrix contains only positive integers. The sum matrix should have the same size as A and B, and the sum of all its elements should be calculated.
"""

def matrix_sum(A, B):
    """
    Compute the sum of two matrices A and B of size m x n.

    Args:
        A (list of lists): Matrix A containing positive integers.
        B (list of lists): Matrix B containing positive integers.

    Returns:
        list of lists: The sum matrix C = A + B.
    """
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]