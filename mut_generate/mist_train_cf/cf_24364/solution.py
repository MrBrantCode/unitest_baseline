"""
QUESTION:
Write a function `find_missing_number` that takes a list of integers as input and returns the smallest positive integer that is not present in the list. The input list may be unsorted and may contain duplicate or non-positive numbers. The function should return the smallest positive integer missing from the list, which may be larger than the maximum number in the list.
"""

def entrance(nums):
    positive_nums = [num for num in nums if num > 0]
    num_set = set(positive_nums)
    i = 1
    while True:
        if i not in num_set:
            return i
        i += 1