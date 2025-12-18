"""
QUESTION:
Implement a function `binary_search_closest(arr, val)` that performs a binary search on a sorted array `arr` to find the number closest to a given value `val`. If `val` is present in `arr`, return it as the closest number. If there are two numbers equally close to `val`, return the larger number.
"""

def binary_search_closest(arr, val):
    """
    Performs a binary search on a sorted array to find the number closest to a given value.

    Args:
        arr (list): A sorted list of numbers.
        val (int): The target value.

    Returns:
        int: The number closest to the target value in the array.
    """

    left = 0
    right = len(arr) - 1
    closest = float('inf')
    closest_num = None

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == val:
            return arr[mid]

        diff = abs(arr[mid] - val)

        if diff < closest:
            closest = diff
            closest_num = arr[mid]
        elif diff == closest and arr[mid] > closest_num:
            closest_num = arr[mid]

        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    return closest_num