"""
QUESTION:
Write a function named `sum_columns` that takes a 2D array as input and returns a list of sums of all columns in the array. The input array is guaranteed to be a list of lists, where each inner list has the same length.
"""

def sum_columns(matrix):
    """
    This function calculates the sum of each column in a given 2D array.

    Args:
        matrix (list of lists): A 2D array where each inner list has the same length.

    Returns:
        list: A list of sums of all columns in the array.
    """
    return [sum(column) for column in zip(*matrix)]