"""
QUESTION:
Write a function `sum_of_rows(matrix)` that takes a 2D matrix of integers as input and returns a list of the sums of each row, excluding any rows where the sum is less than 10 or greater than 1000. The integers in the matrix are between -1000 and 1000.
"""

def sum_of_rows(matrix):
    result = []
    for row in matrix:
        row_sum = sum(row)
        if 10 <= row_sum <= 1000:
            result.append(row_sum)
    return result