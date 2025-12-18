"""
QUESTION:
Write a function called `sum_of_elements` that calculates the sum of all elements in a given two-dimensional array. The function should take a 2D array as input and return the sum of its elements.
"""

def sum_of_elements(matrix):
    """
    Calculate the sum of all elements in a given two-dimensional array.

    Args:
        matrix (list): A 2D list of integers.

    Returns:
        int: The sum of all elements in the 2D list.
    """
    return sum(sum(row) for row in matrix)