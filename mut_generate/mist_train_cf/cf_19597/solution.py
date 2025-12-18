"""
QUESTION:
Implement a function named `linear_search` that performs a case-sensitive linear search in a sorted array. The array must be sorted in ascending order, and the function should return the index of the target value if found, or -1 if not found.
"""

def linear_search(arr, target):
    """
    Performs a case-sensitive linear search in a sorted array.

    Args:
        arr (list): A sorted list of elements.
        target: The value to search for.

    Returns:
        int: The index of the target value if found, or -1 if not found.
    """

    index = -1
    for i in range(len(arr)):
        if arr[i] == target:
            index = i
            break
        elif arr[i] > target:
            break

    return index