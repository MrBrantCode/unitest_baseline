"""
QUESTION:
Write a function named `search` that takes a list of integers `nums` and a target integer `target` as input. Find the index of the first occurrence of `target` in `nums` and return it. If `target` does not exist in `nums`, return -1. The solution should have a time complexity of O(n), use a constant amount of extra space, and not use any built-in search functions or additional data structures.
"""

def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1