"""
QUESTION:
Write a function named `matrix_sum` that calculates the sum of all elements in a square matrix of size n x n using a precomputed array `rowSum` where `rowSum[i]` represents the sum of all elements in the i-th row of the matrix. The function should have a time complexity of O(n).
"""

def matrix_sum(matrix, rowSum, n):
    """
    Calculate the sum of all elements in a square matrix of size n x n.

    Args:
    matrix (list): A 2D list representing the matrix.
    rowSum (list): A precomputed list where rowSum[i] represents the sum of all elements in the i-th row of the matrix.
    n (int): The size of the matrix.

    Returns:
    int: The sum of all elements in the matrix.
    """
    total_sum = 0
    for i in range(n):
        total_sum += rowSum[i]
    return total_sum