"""
QUESTION:
Implement a binary search function named `binary_search` that takes a sorted list of integers and a target integer as input, and returns the index of the target integer in the list if found, and -1 otherwise. The list contains even numbers from 2 to 100, inclusive, and the function should have a time complexity of O(log n).
"""

def binary_search(nums, target):
    """
    This function performs a binary search on a sorted list of integers.
    
    Args:
        nums (list): A sorted list of integers.
        target (int): The target integer to be searched in the list.
    
    Returns:
        int: The index of the target integer in the list if found, -1 otherwise.
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1