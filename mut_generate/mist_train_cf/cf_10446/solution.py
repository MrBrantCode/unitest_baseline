"""
QUESTION:
Write a function named `binary_search` that takes a sorted list of integers and a target element as input, and returns the index of the target element if it is found in the list, and -1 if it is not found. The function should have a time complexity of O(log n), where n is the length of the list.
"""

def entrance(nums, target):
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