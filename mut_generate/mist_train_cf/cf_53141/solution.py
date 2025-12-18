"""
QUESTION:
Write a function named `shiftOneNumber` that takes an array of unique integers as input and returns the minimum number of right shift operations required to sort the array according to positive and negative numbers (negatives first, followed by positives). If it is not possible to sort the array through shifting, return -1. If the input array is empty, return 0.
"""

def shiftOneNumber(arr):
    """
    This function takes an array of unique integers as input and returns the minimum number of right shift operations required 
    to sort the array according to positive and negative numbers (negatives first, followed by positives). If it is not possible 
    to sort the array through shifting, return -1. If the input array is empty, return 0.

    Args:
        arr (list): A list of unique integers.

    Returns:
        int: The minimum number of right shift operations required to sort the array.
    """

    if not arr:
        return 0

    negatives = sorted([num for num in arr if num < 0])
    positives = sorted([num for num in arr if num >= 0])
    sorted_arr = negatives + positives

    for i in range(len(arr)):
        shifted_arr = arr[i:] + arr[:i]
        if shifted_arr == sorted_arr:
            return i

    return -1