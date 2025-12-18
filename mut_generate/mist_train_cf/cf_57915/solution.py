"""
QUESTION:
Write a function named `sum_of_diagonals_and_matrix` that takes an integer `n` as input and returns or prints the sum of primary and secondary diagonals and the whole square matrix of size `n x n`. The function should efficiently handle both odd and even dimensions of the matrix, and optimize for time and space complexity.
"""

import numpy as np

def sum_of_diagonals_and_matrix(n):
    matrix = np.arange(n*n).reshape(n, n)
    primary_diagonal_sum = sum(matrix[i][i] for i in range(n))
    secondary_diagonal_sum = sum(matrix[i][n-i-1] for i in range(n))
    total_sum = np.sum(matrix)
    return primary_diagonal_sum, secondary_diagonal_sum, total_sum