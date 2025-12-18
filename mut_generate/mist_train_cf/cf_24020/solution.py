"""
QUESTION:
Implement a function `search` that takes a list of elements and a target element as input, and returns the index of the target element in the list if found. If the target element is not found, return -1. The function should have a space complexity of O(n), where n is the number of elements in the list.
"""

def search(nums, target):
    for i in range(len(nums)): 
        if nums[i] == target: 
            return i 
    return -1