"""
QUESTION:
Write a function `remove_duplicates` that takes an array of integers as input, removes duplicates, excludes negative numbers, and returns the resulting array in ascending order.
"""

def remove_duplicates(arr):
    """
    Removes duplicates from an array of integers, excludes negative numbers, 
    and returns the resulting array in ascending order.

    Args:
        arr (list): The input array of integers.

    Returns:
        list: The resulting array with no duplicates, excluding negative numbers, in ascending order.
    """
    unique_array = []
    for num in arr:
        if num > 0 and num not in unique_array:
            unique_array.append(num)
    unique_array.sort()
    return unique_array