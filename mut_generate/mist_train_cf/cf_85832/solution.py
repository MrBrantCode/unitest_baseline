"""
QUESTION:
Write a function named `find_duplicates` that takes a list of integers as input and returns a set of integers that appear more than once in the list.
"""

def find_duplicates(nums):
    return set([num for num in nums if nums.count(num) > 1])