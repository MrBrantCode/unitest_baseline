"""
QUESTION:
Write a function called `binary_search` that takes a sorted list of integers and a target value as input, and returns the index of the target value in the list if it exists, or -1 otherwise. The function should use a binary search algorithm.
"""

def binary_search(nums, target):
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