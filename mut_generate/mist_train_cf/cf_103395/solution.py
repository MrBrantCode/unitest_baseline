"""
QUESTION:
Write a function `find_largest_integer(nums)` that takes a list of integers as input and returns a tuple containing the index position and value of the largest integer in the list. Assume the input list is non-empty and contains at least one integer. The index position is 0-based.
"""

def find_largest_integer(nums):
    max_num = float('-inf')
    max_index = -1
    for i in range(len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
            max_index = i
    return (max_index, max_num)