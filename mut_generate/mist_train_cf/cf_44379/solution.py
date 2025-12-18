"""
QUESTION:
Create a recursive function `matrix_search` that performs a binary search on a sorted, multi-dimensional array to find a user-defined element. The function should be able to handle arrays of n dimensions, where n is a positive integer, and return the index(es) of the element if found. If the element is not present in the array, the function should return -1.
"""

def matrix_search(matrix, target):
    for index, row in enumerate(matrix):
        if isinstance(row, list):
            result = matrix_search(row, target)
            if result != -1:
                return [index] + result
        else:
            if row == target:
                return [index]
    return -1