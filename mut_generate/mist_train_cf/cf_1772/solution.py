"""
QUESTION:
Write a function `find_smallest_missing` that takes a list of integers and an integer `K` as input, and returns the smallest missing positive number greater than or equal to `K`. The function should have a time complexity of O(n) and should not use extra space. If there is no missing positive number greater than or equal to `K` in the list, return -1. The input list can contain duplicates, negative numbers, zeros, floating point numbers, and can be unsorted.
"""

def find_smallest_missing(nums, K):
    missing = -1
    while K in nums:
        K += 1
    if K not in nums:
        return K
    for num in nums:
        if num > K and (missing == -1 or num < missing):
            missing = num
    return missing if missing != -1 else -1