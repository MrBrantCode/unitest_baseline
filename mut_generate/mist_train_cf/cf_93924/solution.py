"""
QUESTION:
Write a function named `sum_of_odd_elements` that calculates the sum of all odd elements in a given matrix. The matrix is guaranteed to have at least one row and one column, and it may contain negative numbers. The function should compute the sum in a single pass through the matrix without using any extra space.
"""

def sum_of_odd_elements(matrix):
    total = 0
    for row in matrix:
        for num in row:
            if num % 2 != 0:
                total += num
    return total