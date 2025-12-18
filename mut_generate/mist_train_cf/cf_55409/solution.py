"""
QUESTION:
Write a function `widest_range(matrix)` that takes a 2D array of integers as input, calculates the range of values in each inner array (defined as the difference between the smallest and largest value), and returns a list of these ranges.
"""

def widest_range(matrix):
    """
    Calculate the range of values in each inner array of a 2D matrix.

    Args:
    matrix (list of lists): A 2D array of integers.

    Returns:
    list: A list of ranges, where each range is the difference between the smallest and largest value in the corresponding inner array.
    """
    ranges = []
    for array in matrix:
        ranges.append(max(array)-min(array))
    return ranges