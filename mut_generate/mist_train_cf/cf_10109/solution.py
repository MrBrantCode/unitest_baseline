"""
QUESTION:
Implement the `binary_search` function, which takes a sorted list of integers and a target integer as input and returns the index of the target in the list. The function should have a time complexity of O(log n) and a space complexity of O(1), where n is the length of the input list. The input list may be empty, contain duplicate elements, and contain up to 10^6 elements with any integer value (positive or negative). If the target is not found, the function should return -1.
"""

def binary_search(nums, target):
    """
    This function performs a binary search on a sorted list of integers.
    
    Args:
    nums (list): A sorted list of integers.
    target (int): The target integer to be searched.
    
    Returns:
    int: The index of the target in the list. Returns -1 if the target is not found.
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1