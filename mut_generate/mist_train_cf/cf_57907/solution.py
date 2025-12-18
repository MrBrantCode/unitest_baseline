"""
QUESTION:
Write a function `find_duplicates` that takes a list of integers as input and returns a list of integers that appear more than once in the list.
"""

import collections

def find_duplicates(nums):
    counter = collections.Counter(nums)
    return [item for item, count in counter.items() if count > 1]