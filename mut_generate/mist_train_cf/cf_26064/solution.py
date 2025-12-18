"""
QUESTION:
Write a function `getSmallestElementRecursive(arr, start, end)` that recursively finds the smallest element in a given array of integers. The function should take in three parameters: an integer array `arr`, and two indices `start` and `end` representing the range of the array to search. The function should return the smallest element in the array from index `start` to `end`.
"""

def getSmallestElementRecursive(arr, start, end):
    """
    Recursively finds the smallest element in a given array of integers.

    Args:
        arr (list): A list of integers.
        start (int): The start index of the range to search.
        end (int): The end index of the range to search.

    Returns:
        int: The smallest element in the array from index start to end.
    """
    if start == end:
        return arr[start]
    min_val = getSmallestElementRecursive(arr, start+1, end)
    return arr[start] if arr[start] < min_val else min_val