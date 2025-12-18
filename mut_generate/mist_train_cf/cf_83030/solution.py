"""
QUESTION:
Write a function called `findMinimumElement` that takes a sorted rotated array `arr` as input. The array is sorted in ascending order but rotated (shifted) at an unknown pivot index. The function should return the minimum element in the array. Assume that there are no duplicate elements in the array.
"""

def findMinimumElement(arr):
    """
    This function finds the minimum element in a sorted rotated array.

    Args:
    arr (list): A sorted rotated array.

    Returns:
    int: The minimum element in the array.
    """
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + ((high - low) // 2)

        if arr[mid] > arr[mid + 1]:
            return arr[mid + 1]
        elif arr[mid - 1] > arr[mid]:
            return arr[mid]
        elif arr[0] <= arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return arr[0]