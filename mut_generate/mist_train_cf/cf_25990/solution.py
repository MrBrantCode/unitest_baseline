"""
QUESTION:
Write a function `largest_number` that takes a list of integers as input and returns the largest possible integer that can be formed by concatenating the integers in the list. The input list contains non-negative integers and the function should return a string representation of the largest possible integer.
"""

def largest_number(nums):
    from functools import cmp_to_key
    nums = list(map(str, nums))
    nums.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
    return '0' if nums[0] == '0' else ''.join(nums)