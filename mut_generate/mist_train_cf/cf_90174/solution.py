"""
QUESTION:
Write a function `transform_list` that takes a list of distinct positive integers as input, multiplies each odd number by 7, and replaces each even number with its cube, maintaining the original order. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list.
"""

def transform_list(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            nums[i] *= 7
        else:
            nums[i] = nums[i] ** 3
    return nums