"""
QUESTION:
Given a function `sum_row_sums(matrix)`, calculate the sum of elements in each row of a given 2D array `matrix`. The function should return the row(s) with the highest sum, the row(s) with the lowest sum, and the average sum of all rows. If multiple rows have the same highest or lowest sum, the function should return all of them.
"""

import numpy as np

def sum_row_sums(matrix):
    """
    Calculate the sum of elements in each row of a given 2D array.
    Returns the row(s) with the highest sum, the row(s) with the lowest sum, and the average sum of all rows.

    Parameters:
    matrix (numpy array): A 2D array

    Returns:
    tuple: A tuple containing the rows with the highest sum, the rows with the lowest sum, and the average sum of all rows
    """

    # Calculate the sum of elements in each row
    row_sums = {i: sum(row) for i, row in enumerate(matrix)}

    # Get the rows with the highest sum
    max_sum = max(row_sums.values())
    max_sum_rows = [key for key, value in row_sums.items() if value == max_sum]

    # Get the rows with the lowest sum
    min_sum = min(row_sums.values())
    min_sum_rows = [key for key, value in row_sums.items() if value == min_sum]

    # Calculate the average sum of all rows
    average_sum = sum(row_sums.values()) / len(row_sums)

    return max_sum_rows, min_sum_rows, average_sum