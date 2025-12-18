"""
QUESTION:
Write a function `sort_descending(nums)` that takes a 2D list of floating point numbers as input and returns a new 2D list where each sub-array is sorted in descending order. The length of each sub-array can vary. The function should not modify the original input list.
"""

def sort_descending(nums):
    sorted_nums = []
    for sublist in nums:
        sorted_nums.append(sorted(sublist, reverse=True))
    return sorted_nums