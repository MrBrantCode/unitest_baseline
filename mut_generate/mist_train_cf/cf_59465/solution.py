"""
QUESTION:
Create a function `custom_sort(arr)` to sort a given multi-dimensional array `arr` in ascending order based on the sum of the integer values of each sub-array. The function should return the sorted array. The input array contains only integer values and the sub-arrays can be of any length. The function should not use any external libraries and should be implemented in Python.
"""

def custom_sort(arr):
    """
    Sorts a given multi-dimensional array in ascending order based on the sum of the integer values of each sub-array.

    Args:
        arr (list): A multi-dimensional array containing integer values.

    Returns:
        list: The sorted array.
    """
    return sorted(arr, key=sum)