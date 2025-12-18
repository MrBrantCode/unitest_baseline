"""
QUESTION:
Write a function `find_index` that takes a list of integers as input and returns the index of the first element that is less than the element immediately to its right. If no such element exists, return -1. The function should only consider the list as input and should not use any other information.
"""

def find_index(nums):
    i = len(nums) - 2
    while i >= 0:
        if nums[i] < nums[i + 1]:
            return i
        i -= 1
    return -1