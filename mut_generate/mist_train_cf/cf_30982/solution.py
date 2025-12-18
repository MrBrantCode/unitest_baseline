"""
QUESTION:
Write a function named `compare_averages` that takes a 2D list of integers as input and returns an integer. The function should calculate the average of each row and column in the matrix and return the index of the row whose average is greater than the maximum average of any column; otherwise, return -1. Assume that the input matrix is not empty and contains at least one row and one column.
"""

from typing import List

def compare_averages(matrix: List[List[int]]) -> int:
    row_averages = [sum(row) / len(row) for row in matrix]
    column_averages = [sum(column) / len(column) for column in zip(*matrix)]

    max_column_average = max(column_averages)

    for index, average in enumerate(row_averages):
        if average > max_column_average:
            return index
    return -1