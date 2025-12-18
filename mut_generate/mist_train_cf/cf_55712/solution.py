"""
QUESTION:
Create a function `diagonalProduct(A, B)` that takes two matrices `A` (size Nx3) and `B` (size 3xN) as input, and returns a vector of size N, where each element at index `i` is the product of the `i-th` row of `A` and the `i-th` column of `B`. The function should be implemented in a single line of code using Eigen library.
"""

def diagonalProduct(A, B):
    """
    This function takes two matrices A (size Nx3) and B (size 3xN) as input, 
    and returns a vector of size N, where each element at index i is the product 
    of the i-th row of A and the i-th column of B.

    Parameters:
    A (list of lists): A matrix of size Nx3
    B (list of lists): A matrix of size 3xN

    Returns:
    list: A vector of size N containing the product of corresponding rows and columns
    """
    return [sum(a * b for a, b in zip(row, col)) for row, col in zip(A, zip(*B))]