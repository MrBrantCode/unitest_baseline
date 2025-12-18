"""
QUESTION:
Create a function named `sum_of_each_row_and_highest_average` that takes a 2D matrix of integers as input where each integer is between -1000 and 1000. The function should return two values: a list of the sums of each row where the sum is between 10 and 1000 (inclusive), and the index of the column with the highest average. Assume that the input matrix is a valid 2D matrix and has at least one row.
"""

def sum_of_each_row_and_highest_average(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    row_sum = [sum(row) for row in matrix if 10 <= sum(row) <= 1000]

    col_avg = [sum(col) / rows for col in zip(*matrix)]

    highest_avg_col = col_avg.index(max(col_avg))

    return row_sum, highest_avg_col