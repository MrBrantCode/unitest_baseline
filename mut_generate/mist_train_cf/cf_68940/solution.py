"""
QUESTION:
Write a function named `compute_median` that takes 5 arguments and returns their median. The function should first store all the arguments in a list, sort the list in ascending order, and then return the middle item. Assume the input will always have 5 numbers.
"""

def compute_median(a, b, c, d, e):
    nums = [a, b, c, d, e]
    nums.sort()
    return nums[2]