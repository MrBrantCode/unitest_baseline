"""
QUESTION:
Write a function `calculate_cumulative_total(matrix)` that calculates the cumulative total of the squared values of only the even elements present within a specified matrix. The input matrix (m x n) will be composed of integers (positive, negative, or zero). The function should handle the complexity of a 2-Dimensional data structure and perform the operations accordingly.
"""

def entance(matrix):
    total = 0
    for row in matrix:
        for num in row:
            if num % 2 == 0:
                total += num ** 2
    return total