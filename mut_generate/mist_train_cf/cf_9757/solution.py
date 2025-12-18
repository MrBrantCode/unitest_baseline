"""
QUESTION:
Write a function named `remove_threes` that takes a list of integers as input and returns the modified list with all elements of value 3 removed. The solution should have a time complexity of O(n) and be implemented in a single pass without using built-in functions like `filter()` or `list comprehension`.
"""

def remove_threes(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 3:
            nums.pop(i)
        else:
            i += 1
    return nums