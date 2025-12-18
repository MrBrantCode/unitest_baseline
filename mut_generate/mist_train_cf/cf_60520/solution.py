"""
QUESTION:
Create a method named `sort_rows` that takes a 2D array as input, sorts each row in ascending order, and returns the sorted array. Additionally, create another method named `find_medians` that takes a 2D array as input, calculates the median of each row, and returns an array of these medians.
"""

def sort_rows(matrix):
    return [sorted(row) for row in matrix]

def find_medians(matrix):
    return [sorted(row)[len(row) // 2] if len(row) % 2 != 0 else (sorted(row)[len(row) // 2 - 1] + sorted(row)[len(row) // 2]) / 2 for row in matrix]