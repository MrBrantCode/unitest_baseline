"""
QUESTION:
Write a function `most_frequent(nums)` that takes a list of integers as input and returns the value that appears most frequently in the list. The input list will contain at least one element and all elements are integers.
"""

def most_frequent(nums):
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    max_count = 0
    res = 0
    for key, val in count.items():
        if val > max_count:
            res = key
        max_count = max(max_count, val)
    return res