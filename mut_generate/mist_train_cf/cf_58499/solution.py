"""
QUESTION:
Write a function called `sortDescending` that takes an array of negative integers as input and returns the array sorted in descending order without using built-in sort functions that sort in-place or non-in-place with a descending order option.
"""

def sortDescending(arr):
    """
    Sorts an array of negative integers in descending order without using built-in sort functions.

    Args:
        arr (list): A list of negative integers.

    Returns:
        list: The array sorted in descending order.
    """
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr