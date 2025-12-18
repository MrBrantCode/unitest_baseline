"""
QUESTION:
Create a function named `max_disparity(matrix)` that calculates the maximum disparity between the minimum and maximum values in each sub-matrix within a given two-dimensional matrix. The function should return the maximum disparity found among all sub-matrices. Assume that sub-matrices are non-empty and contain integer values.
"""

def max_disparity(matrix):
    disparities = []
    for sub_matrix in matrix:
        disparities.append(max(sub_matrix)-min(sub_matrix))
    return max(disparities)