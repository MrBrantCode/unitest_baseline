"""
QUESTION:
Implement a function named `binary_search_last_occurrence` that takes a sorted list of integers `nums` and a target integer `target` as input and returns the index of the last occurrence of `target` in `nums`. If `target` is not found in `nums`, return -1. The function should not use any built-in sorting functions or libraries, and it should work efficiently for a list containing up to 10^9 elements and a target number within the range of -10^12 to 10^12.
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