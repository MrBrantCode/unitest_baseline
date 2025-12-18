"""
QUESTION:
Write a function `search(nums, target)` to find the index of the first occurrence of the target integer in the list `nums`. If the target integer does not exist in the list, return -1. The function should have a time complexity of O(n) and only use a constant amount of extra space without utilizing any built-in search functions, libraries, or additional data structures.
"""

def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1