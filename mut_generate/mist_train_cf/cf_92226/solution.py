"""
QUESTION:
Write a function `find_smallest_missing_integer(nums)` that takes a list of integers as input and returns the smallest positive integer that is not present in the list. The input list can contain up to 100,000 integers and may include both positive and negative integers. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def find_smallest_missing_integer(nums):
    positive_nums = set()
    for num in nums:
        if num > 0:
            positive_nums.add(num)
    smallest_missing = 1
    while smallest_missing in positive_nums:
        smallest_missing += 1
    return smallest_missing