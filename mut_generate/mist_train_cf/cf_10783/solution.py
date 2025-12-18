"""
QUESTION:
Write a function named `sum_matrix` that takes a 2D list of integers as input and returns the sum of all non-negative integers in the matrix.
"""

def sum_matrix(matrix):
    total_sum = 0
    for row in matrix:
        for element in row:
            if element >= 0:
                total_sum += element
    return total_sum