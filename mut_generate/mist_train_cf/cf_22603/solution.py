"""
QUESTION:
Write a function `row_sums(matrix)` that takes a 2D list of integers as input and returns a list containing the sum of each row in the matrix, followed by the total sum of all elements in the matrix. The input matrix can be of any size.
"""

def entrance(matrix):
    result = []
    total_sum = 0

    for row in matrix:
        row_sum = sum(row)
        result.append(row_sum)
        total_sum += row_sum

    result.append(total_sum)
    return result