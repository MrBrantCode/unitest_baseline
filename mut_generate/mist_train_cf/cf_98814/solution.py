"""
QUESTION:
Create a function `calculate_table_average` that takes a 2D list of integers and floats as input, where some values may be `None`. The function should return a new 2D list where each row contains a single value, which is the rounded average of the non-`None` values in the corresponding row of the input table. If a row contains only `None` values, the average should be 0. The function should also modify the row averages by repeatedly removing the smallest non-`None` value and recalculating the average until the average is greater than 50 or only one non-`None` value remains.
"""

import numpy as np

def calculate_table_average(table):
    new_table = []
    for row in table:
        row = [value for value in row if value is not None]
        while len(row) > 1 and sum(row) / len(row) <= 50:
            row.remove(min(row))
        row_avg = round(sum(row) / len(row)) if row else 0
        new_row = [row_avg for i in range(len(table[0]))]
        new_table.append(new_row)
    return new_table