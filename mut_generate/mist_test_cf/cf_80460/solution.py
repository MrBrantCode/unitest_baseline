"""
QUESTION:
Create a Python function `check_tuple_duplicates(matrix)` that takes a two-dimensional matrix of tuples as input. The function should return `True` if there are any duplicated tuple elements in the matrix and `False` otherwise.
"""

def entrance(matrix):
    flat_list = [item for sublist in matrix for item in sublist]
    return len(set(flat_list)) != len(flat_list)