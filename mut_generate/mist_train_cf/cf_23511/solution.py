"""
QUESTION:
Write a function `sum_odd_matrix(matrix)` that calculates the sum of all odd elements in a given 2D matrix. The input matrix is a list of lists where each inner list represents a row in the matrix. The function should return the total sum of odd elements.
"""

def sum_odd_matrix(matrix):
    sum = 0
    for row in matrix:
        for value in row:
            if value % 2 != 0:
                sum += value
    return sum