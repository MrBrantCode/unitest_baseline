"""
QUESTION:
Write a function `remove_duplicates` that takes a list of integers as input. The function should return a list of distinct integers in descending order without modifying the original input list.
"""

def remove_duplicates(nums):
    distinct_nums = list(set(nums))
    sorted_nums = sorted(distinct_nums, reverse=True)
    return sorted_nums