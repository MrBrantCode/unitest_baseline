"""
QUESTION:
Create a function called `findMax` that takes an array of integers as input and returns the maximum element in the array. The array can contain both positive and negative integers, and it will not be empty.
"""

def findMax(array):
    """
    This function finds the maximum element in an array of integers.

    Args:
    array (list): A list of integers.

    Returns:
    int: The maximum element in the array.
    """
    max_value = array[0]
    for num in array[1:]:
        if num > max_value:
            max_value = num
    return max_value