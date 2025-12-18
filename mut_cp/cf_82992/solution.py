"""
ORIGINAL QUESTION:
Create a function named `min_and_max` that takes a list of integers as input and returns a tuple containing the minimum and maximum integers in the list. The function should not use any built-in min or max functions. The input list is not empty and contains at least one integer.
"""

def min_and_max(nums):
    min_num = max_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return min_num, max_num