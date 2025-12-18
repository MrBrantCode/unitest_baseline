"""
QUESTION:
Write a function `find_min_missing` that takes a list of integers and an integer K as input. The function should find the smallest missing positive number greater than or equal to K in the list, with a time complexity of O(n) and without using extra space. If there is no missing positive number greater than or equal to K in the list, return -1.
"""

def find_min_missing(nums, k):
    minMissing = k
    for num in nums:
        if 0 < num <= minMissing:
            minMissing = num + 1
    return -1 if minMissing == k else minMissing