"""
QUESTION:
Implement a function named binary_search that takes in a sorted list of integers and a target value as input, and returns the index of the target value if it exists in the list, or -1 if it does not. The function should have a time complexity of O(log n) and should only consider the given list as the search space.
"""

def binary_search(nums, target):
    """
    Searches for a target value in a sorted list of integers.

    Args:
        nums (list): A sorted list of integers.
        target (int): The target value to search for.

    Returns:
        int: The index of the target value if it exists, -1 otherwise.
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