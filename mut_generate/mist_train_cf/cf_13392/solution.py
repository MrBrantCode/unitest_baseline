"""
QUESTION:
Implement a function named `linear_search` that takes in an array of integers `nums` and a target integer `target_num`. The function should perform a linear search on the array to find the index of the target number. If the target number is found, return its index; otherwise, return -1. The array can contain any integers and may not be sorted.
"""

def linear_search(nums, target_num):
    for i in range(len(nums)):
        if nums[i] == target_num:
            return i
    return -1