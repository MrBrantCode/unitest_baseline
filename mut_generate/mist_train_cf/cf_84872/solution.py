"""
QUESTION:
Given a sequence of integers, write a function named `longest_subsequence` that identifies the longest continuous subsequence containing the maximum number of distinct integers. The function should take a list of integers as input and return the length of the longest continuous subsequence.
"""

def longest_subsequence(arr):
    if not arr:
        return 0

    left = 0
    max_length = 0
    distinct_nums = set()

    for right in range(len(arr)):
        while arr[right] in distinct_nums:
            distinct_nums.remove(arr[left])
            left += 1
        distinct_nums.add(arr[right])
        max_length = max(max_length, right - left + 1)

    return max_length