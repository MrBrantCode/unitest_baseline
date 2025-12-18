"""
QUESTION:
Implement the binary_search function, which takes in a sorted list of elements and a target element, and returns the index of the target element if found, or -1 if not found. The function should use the Binary Search algorithm, repeatedly dividing the list in half until the target element is found or the list is exhausted. The function should assume that the input list is sorted in ascending order.
"""

def binary_search(nums, target):
    """
    Searches for a target element in a sorted list using the Binary Search algorithm.

    Args:
        nums (list): A sorted list of elements.
        target: The target element to search for.

    Returns:
        int: The index of the target element if found, or -1 if not found.
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