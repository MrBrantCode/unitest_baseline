"""
QUESTION:
Write a function called `find_disparity` that takes a 2D list of integers as input and returns a list of integers. Each integer in the output list represents the difference between the maximum and minimum values in the corresponding sub-list of the input list.
"""

def find_disparity(matrix):
    disparities = []
    for submatrix in matrix:
        disparities.append(max(submatrix) - min(submatrix))
    return disparities