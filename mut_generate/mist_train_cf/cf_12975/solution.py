"""
QUESTION:
Create a function `longest_common_subsequence` that takes in a list of integers and returns the length of the longest common subsequence of consecutive elements in the list. The function should have a time complexity of O(n), where n is the length of the input list. The input list will contain at least one element.
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