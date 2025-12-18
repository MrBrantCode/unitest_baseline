"""
QUESTION:
Write a function `find_max_index` that takes a list of integers as input and returns the index of the maximum element in the list. If there are multiple maximum elements, return the index of the first occurrence. If the list is empty, return -1.
"""

def find_max_index(nums):
    if len(nums) == 0:
        return -1

    max_val = nums[0]
    max_index = 0

    for i in range(1, len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]
            max_index = i

    return max_index