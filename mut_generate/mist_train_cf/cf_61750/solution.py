"""
QUESTION:
Construct a function named 'get_row' that accepts a nested list 'lst' and an integer 'x'. The function should return a list of tuples containing the coordinates (row, column) of all occurrences of 'x' in 'lst', with 0-based indexing. The coordinates should be ordered by ascending rows and then by descending columns within the same row.
"""

def get_row(lst, x):
    result = []
    for row_index, row in enumerate(lst):
        for column_index, element in enumerate(row):
            if element == x:
                result.append((row_index, column_index))
    result.sort(key=lambda a: (a[0], -a[1]))
    return result