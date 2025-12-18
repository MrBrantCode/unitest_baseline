"""
QUESTION:
Write a function named `find_index` that takes a list of integers `nums` and a target integer `target` as input, and returns the index of the first occurrence of `target` in `nums`. If `target` does not exist in `nums`, return -1. The function should have a time complexity of O(n) and should not use any built-in search functions or libraries.
"""

def find_index(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1