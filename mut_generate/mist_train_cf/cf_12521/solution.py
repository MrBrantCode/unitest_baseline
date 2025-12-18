"""
QUESTION:
Implement the function `search(nums, target)` that takes a sorted array `nums` and a target value `target` as input and returns the index of the target in the array if found. If the target is not found, return -1. The function should use the binary search algorithm to achieve a time complexity of O(log n).
"""

def search(nums, target):
    """
    Searches for the target value in a sorted array using the binary search algorithm.

    Args:
        nums (list): A sorted list of integers.
        target (int): The target value to be searched.

    Returns:
        int: The index of the target in the array if found, -1 otherwise.
    """

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1