"""
QUESTION:
Write a function named `max_submatrix` that takes a 2D matrix of integers as input and returns the highest cumulative sum of a submatrix. A submatrix is a rectangular subset of the input matrix that can be formed by deleting rows or columns. The function should handle cases where the input matrix has a single row, a single column, or a single element, as well as cases where the matrix contains only negative integers. The function should return the highest cumulative sum, which can be negative if all elements in the matrix are negative.
"""

def max_submatrix(matrix):
    if not matrix or not matrix[0]:
        return 0 

    m, n = len(matrix), len(matrix[0])

    sum_matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            sum_matrix[i+1][j+1] = matrix[i][j] + sum_matrix[i][j+1] + sum_matrix[i+1][j] - sum_matrix[i][j]

    max_sum = float('-inf')
    for i in range(m):
        for j in range(n):
            for x in range(i, m):
                for y in range(j, n):
                    temp_sum = sum_matrix[x+1][y+1] - sum_matrix[i][y+1] - sum_matrix[x+1][j] + sum_matrix[i][j]
                    max_sum = max(max_sum, temp_sum)

    return max_sum