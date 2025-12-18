"""
QUESTION:
Write a function `findMaxValue(array)` that finds the maximum value in a given array. The array is assumed to be non-empty and contains at least one number. The function should return the maximum value in the array.
"""

def findMaxValue(array):
    """
    This function finds the maximum value in a given array.

    Args:
        array (list): A list of numbers.

    Returns:
        The maximum value in the array.
    """
    maxValue = float('-inf')  # Initialize max_value as negative infinity
    for element in array:
        if element > maxValue:
            maxValue = element
    return maxValue