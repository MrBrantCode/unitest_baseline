"""
QUESTION:
Write a function `maximal_path_sum(matrix)` that takes a 2D list `matrix` of integers and returns the maximum sum of numbers along a path from the top left to the bottom right of the matrix by only moving right and down. Assume the input matrix is a square matrix of size n x n, where n is a positive integer, and the numbers in the matrix are non-negative integers. The function should return the maximum sum as an integer.
"""

def maximal_path_sum(matrix):
    n = len(matrix)

    sums = [[0]*n for _ in range(n)]

    sums[0][0] = matrix[0][0]
    for i in range(1, n):
        sums[i][0] = sums[i-1][0] + matrix[i][0]
        sums[0][i] = sums[0][i-1] + matrix[0][i]

    for i in range(1, n):
        for j in range(1, n):
            sums[i][j] = max(sums[i-1][j], sums[i][j-1]) + matrix[i][j]

    return sums[-1][-1]