"""
QUESTION:
Write a function named `swap_first_and_last` that accepts a matrix (a list of lists) as input and returns a new matrix where the first and last elements of each row are swapped, preserving the relative positioning of the remaining elements.
"""

def swap_first_and_last(matrix):
    return [row[-1:] + row[1:-1] + row[:1] for row in matrix]