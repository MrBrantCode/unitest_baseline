"""
QUESTION:
Given a 2D array of integers, write a function called `flatten_sort_array` that creates a new flattened and sorted array excluding negative numbers, and returns the resulting array along with its minimum and maximum values without using built-in min/max functions. The function should be able to process arrays of arbitrary dimensions efficiently.
"""

def flatten_sort_array(matrix):
    """
    Creates a new flattened and sorted array excluding negative numbers, 
    and returns the resulting array along with its minimum and maximum values.

    Args:
        matrix (list): A 2D array of integers.

    Returns:
        tuple: A tuple containing the flattened and sorted array, 
               the minimum value, and the maximum value.
    """
    flattened = [num for sublist in matrix for num in sublist if num >= 0]
    flattened.sort()
    if len(flattened) == 0:
        return "No positive numbers found in the array"
    min_num = max_num = flattened[0]
    for num in flattened[1:]:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return flattened, min_num, max_num