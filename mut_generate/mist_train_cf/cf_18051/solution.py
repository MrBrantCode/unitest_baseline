"""
QUESTION:
Implement a function `reverse_binary_search` that takes a sorted array in descending order and a target value as input, and returns the index of the target value if found, or -1 if not found. The function should have a time complexity of O(log n).
"""

def reverse_binary_search(nums, target):
    """
    This function performs a reverse binary search on a sorted array in descending order.
    
    Args:
        nums (list): A sorted list of integers in descending order.
        target (int): The target value to search for in the list.
    
    Returns:
        int: The index of the target value if found, -1 otherwise.
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            left = mid + 1
        else:
            right = mid - 1
    return -1