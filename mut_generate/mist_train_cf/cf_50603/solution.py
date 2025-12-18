"""
QUESTION:
Create a function named `smallest_nums` that takes an array of integers as input. The function should return the five smallest unique numbers in the array, ignoring any duplicate values and handling the possibility of negative numbers.
"""

def smallest_nums(array):
    """
    Returns the five smallest unique numbers in the array, 
    ignoring any duplicate values and handling the possibility of negative numbers.

    Args:
    array (list): A list of integers.

    Returns:
    list: The five smallest unique numbers in the array.
    """
    unique_nums = list(set(array))  # Removes duplicates from the array.
    unique_nums.sort()  # Sorts the array from smallest to biggest.
    return unique_nums[:5]  # Returns the first 5 smallest unique numbers.