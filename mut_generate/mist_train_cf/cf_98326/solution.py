"""
QUESTION:
Create a Python function named 'max_nested_table' that accepts a table with up to 3 levels of depth and a 'threshold' parameter. The function should return a table with the same structure, where each element is the maximum value in its respective row, excluding values below the threshold.
"""

def max_nested_table(table, threshold):
    if isinstance(table, (list, tuple)):
        return type(table)(max_nested_table(row, threshold) for row in table)
    else:
        return table if table > threshold else threshold