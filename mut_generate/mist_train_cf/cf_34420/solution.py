"""
QUESTION:
Given an array of distinct positive integers in ascending order and an integer k, find the k-th positive integer that is missing from the array. The array is guaranteed to be sorted in ascending order, and 1 <= len(arr) <= 1000, 1 <= k <= 1000. The function should be named findKthPositive(arr, k) and return the k-th missing positive integer.
"""

def findKthPositive(arr, k):
    missing_numbers = 0
    next_expected = 1

    for x in arr:
        while x != next_expected:
            missing_numbers += 1
            if missing_numbers == k:
                return next_expected
            next_expected += 1
        next_expected += 1

    return arr[-1] + k - missing_numbers