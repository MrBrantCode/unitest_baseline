"""
QUESTION:
Write a function `sum_matrix_elements(matrix)` that calculates the sum of all elements in a given 2D matrix, where each element is multiplied by its row index. The matrix can contain negative numbers. The function should return the total sum.
"""

def sum_matrix_elements(matrix):
    total_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total_sum += matrix[i][j] * i
    return total_sum