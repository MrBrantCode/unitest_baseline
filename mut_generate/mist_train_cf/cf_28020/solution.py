"""
QUESTION:
Create a function `sum_columns` that takes a single parameter `input_str`, a string representing a matrix of floating-point numbers where rows are separated by newline characters and columns are separated by commas. The function should return a list containing the sum of each column in the input matrix, ignoring any non-numeric characters and handling empty cells as 0.0.
"""

def sum_columns(input_str):
    rows = input_str.strip().split('\n')
    num_cols = len(rows[0].split(','))
    col_sums = [0.0] * num_cols

    for row in rows:
        cols = row.split(',')
        for i, col in enumerate(cols):
            try:
                col_sums[i] += float(col)
            except ValueError:
                pass

    return col_sums