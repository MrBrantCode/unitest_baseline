"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of integers as input and returns a new list with only the unique elements, preserving the original order. The input list may contain negative integers, be empty, or have non-consecutive duplicates, and the function should have a time complexity of O(n) or less without using built-in Python functions or libraries for removing duplicates.
"""

def remove_duplicates(nums):
    unique_nums = {}
    for num in nums:
        if num not in unique_nums:
            unique_nums[num] = 1
        else:
            unique_nums[num] += 1
    unique_list = []
    for num in nums:
        if unique_nums[num] == 1:
            unique_list.append(num)
    return unique_list