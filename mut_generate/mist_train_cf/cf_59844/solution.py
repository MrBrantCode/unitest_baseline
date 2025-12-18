"""
QUESTION:
Write a function `max_difference_sum` that calculates the sum of the maximum differences between the smallest and the largest elements in each sub-array of a given two-dimensional array of integers. The function should take the two-dimensional array as input and return the sum of differences.
"""

def max_difference_sum(array):
    """
    This function calculates the sum of the maximum differences between the smallest and the largest elements in each sub-array of a given two-dimensional array of integers.

    Args:
        array (list): A two-dimensional array of integers.

    Returns:
        int: The sum of differences.
    """
    return sum(max(sub_array) - min(sub_array) for sub_array in array)