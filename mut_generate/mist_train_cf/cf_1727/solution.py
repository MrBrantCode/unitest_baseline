"""
QUESTION:
Implement a function named binarySearch that takes a sorted list of integers and a target number as input, and returns the index of the last occurrence of the target number in the list. The function should have a time complexity of O(log n) and use a constant amount of extra memory. If the target number is not found, the function should return -1. The input list may contain duplicates of the target number.
"""

def binarySearch(nums, target):
    """
    This function performs a binary search on a sorted list of integers to find the index of the last occurrence of a target number.
    
    Args:
        nums (list): A sorted list of integers.
        target (int): The target number to be searched.
    
    Returns:
        int: The index of the last occurrence of the target number if found, -1 otherwise.
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                return mid
            else:
                left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1