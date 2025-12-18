"""
QUESTION:
Write a function `calculate_leading_disparity(matrix)` that takes a 2D array of integers as input and returns the maximum difference between the minimum and maximum values across all subgroups. If the input matrix is empty or all subgroups are empty, return `None`.
"""

def calculate_leading_disparity(matrix):
    leading_disparity = float('-inf')
    for subgroup in matrix:
        if len(subgroup) > 0:
            max_value = max(subgroup)
            min_value = min(subgroup)
            disparity = max_value - min_value
            leading_disparity = max(leading_disparity, disparity)
    return leading_disparity if leading_disparity != float('-inf') else None