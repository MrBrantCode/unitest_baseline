"""
QUESTION:
Create a function named `linear_search` that takes two parameters: a list of integers `nums` and a target integer `target_num`. The function should perform a linear search on the list to find the index of the `target_num` and return the index if found. If the `target_num` is not found in the list, the function should return -1. The list `nums` will contain 10,000,000 random integers ranging from -10,000,000 to 10,000,000.
"""

def linear_search(nums, target_num):
    for i in range(len(nums)):
        if nums[i] == target_num:
            return i
    return -1