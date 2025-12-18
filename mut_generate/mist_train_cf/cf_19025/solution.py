"""
QUESTION:
Implement a function `binary_search_insert` that takes a sorted array of integers and an integer value as input. Using the binary search algorithm, determine whether the given value is present in the array or not. If the value is present, return the index at which it is found. If the value is not present, return the index at which it should be inserted to maintain the sorted order. The function should handle cases where the value is not present in the array.
"""

def binary_search_insert(nums, target):
    """
    This function performs a binary search on a sorted array to find the index of a given target value.
    If the target value is not found, it returns the index where the value should be inserted to maintain the sorted order.

    Args:
        nums (list): A sorted list of integers.
        target (int): The target value to be searched.

    Returns:
        int: The index of the target value if found, or the index where it should be inserted.
    """

    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start