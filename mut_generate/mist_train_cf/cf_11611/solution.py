"""
QUESTION:
Write a function named `remove_duplicates` that takes a list of integers as input and returns a list of distinct integers in descending order without modifying the original list.
"""

def remove_duplicates(nums):
    distinct_nums = list(set(nums))
    sorted_nums = sorted(distinct_nums, reverse=True)
    return sorted_nums