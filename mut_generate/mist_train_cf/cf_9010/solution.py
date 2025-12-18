"""
QUESTION:
Implement a function `binary_search` that takes a sorted array and a target value as input, and returns the index of the target value if found, or -1 otherwise. The function should achieve a time complexity of O(log n) and a space complexity of O(1).
"""

def binary_search(nums, target):
    """
    Searches for the target value in a sorted array using binary search.

    Args:
    - nums: A sorted array of integers.
    - target: The target value to search for.

    Returns:
    - The index of the target value if found, -1 otherwise.
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1