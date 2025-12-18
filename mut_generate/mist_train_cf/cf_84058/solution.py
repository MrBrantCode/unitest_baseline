"""
QUESTION:
Write a function `cumulative_total(matrix)` that calculates the cumulative total of every individual element present within a given two-dimensional matrix. The input matrix is a list of lists, where each inner list represents a row of integers. The function should return the sum of all elements in the matrix.
"""

def cumulative_total(matrix):
    total = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total += matrix[i][j]

    return total