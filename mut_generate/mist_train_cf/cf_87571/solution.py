"""
QUESTION:
Implement the function `binary_search_last_occurrence` that performs a binary search in a given list of integers and returns the index of the last occurrence of a target number. The list is guaranteed to be sorted in non-decreasing order, can contain up to 10^9 elements, and the target number can be any integer within the range of -10^12 to 10^12. If the target number is not found, return -1. Do not use any built-in sorting functions or libraries for the binary search algorithm implementation.
"""

def binary_search_last_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    last_occurrence = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            last_occurrence = mid
            left = mid + 1  
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last_occurrence