"""
QUESTION:
Write a function `sum_of_odd_elements(matrix)` that calculates the sum of all odd elements in a given matrix in a single pass, without using any extra space. The matrix has at least one row and one column, and can contain negative numbers.
"""

def sum_of_odd_elements(matrix):
    sum = 0
    for row in matrix:
        for num in row:
            if num % 2 != 0:
                sum += num
    return sum