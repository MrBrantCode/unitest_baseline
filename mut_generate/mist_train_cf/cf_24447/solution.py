"""
QUESTION:
Implement a function named binary_search that takes a sorted list of integers and a target integer as input. The function should return the index of the target if found in the list, otherwise return -1. The list is assumed to be sorted in ascending order.
"""

def entrance(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1