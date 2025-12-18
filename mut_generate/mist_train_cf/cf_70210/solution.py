"""
QUESTION:
Given an unsorted list of n integers (1 <= n <= 10^5), create a recursive function `find_max` that finds the maximum element and its index position in the list, and also determines the total number of occurrences for the maximum element. The function should take the list as an input and return the maximum number, the index of its first occurrence, and its total count.
"""

def find_max(nums, idx=0, max_num=None, max_idx=None, count=0):
    if idx == len(nums):
        return max_num, max_idx, count
    elif max_num is None or nums[idx] > max_num:
        return find_max(nums, idx+1, nums[idx], idx, 1)
    elif nums[idx] == max_num:
        return find_max(nums, idx+1, max_num, max_idx, count+1)
    else:
        return find_max(nums, idx+1, max_num, max_idx, count)