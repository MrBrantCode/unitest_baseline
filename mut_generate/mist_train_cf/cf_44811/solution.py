"""
QUESTION:
Create a function `flatten_3d_matrix(matrix)` that takes a 3D matrix of integers as input and returns a 1D list of integers. The function should be able to handle both positive and negative integers, including zero, and edge cases such as an empty matrix or matrices with inconsistent sub-array lengths.
"""

def flatten_3d_matrix(matrix):
    if not bool(matrix) or not isinstance(matrix, list):
        return []

    flat_list = []
    for element in matrix:
        if isinstance(element, list):
            flat_list.extend(flatten_3d_matrix(element))
        elif isinstance(element, (int, float)):
            flat_list.append(element)

    return flat_list