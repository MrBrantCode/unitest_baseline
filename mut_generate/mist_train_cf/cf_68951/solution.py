"""
QUESTION:
Write a function named `find_min_in_matrix` that takes a 2D array (matrix) as input, which may contain different data types, and returns the minimum numeric value in the matrix. The function should handle cases where the matrix contains non-numeric data types. If the matrix contains no numeric values, the function should return `None`.
"""

def find_min_in_matrix(matrix):
    min_val = None
    for row in matrix:
        for item in row:
            try:
                val = float(item)
                if min_val is None or val < min_val:
                    min_val = val
            except ValueError:
                continue
    return min_val