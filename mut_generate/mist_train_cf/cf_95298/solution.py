"""
QUESTION:
Write a function `find_median` that takes a sorted list of positive integers as input and returns the median using only logical and bitwise operators. The input list may have an odd or even number of elements.
"""

def find_median(nums):
    count = len(nums)
    is_odd = count & 1

    if is_odd:
        middle_index = count // 2
        median = nums[middle_index]
    else:
        first_middle_index = count // 2 - 1
        second_middle_index = count // 2
        median = (nums[first_middle_index] + nums[second_middle_index]) // 2

    return median