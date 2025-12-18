"""
QUESTION:
Create a function named `longest_common_subsequence` that takes a list of integers as input and returns the length of the longest subsequence of consecutive integers in the list. The function should assume that the input list is non-empty and contains at least one integer. The function should also have a time complexity of O(n), where n is the length of the input list.
"""

def longest_common_subsequence(nums):
    max_len = 0
    curr_len = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            curr_len += 1
        else:
            curr_len = 1

        if curr_len > max_len:
            max_len = curr_len

    return max_len