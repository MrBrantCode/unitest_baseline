"""
QUESTION:
Write a function `longestIncreasingSubsequence(nums)` that finds the length of the longest increasing subsequence in a given array of numbers. An increasing subsequence is a sequence of numbers where each number is greater than the previous number. If there are multiple subsequences with the same length, return the length of the one that appears first in the original array.

The function should take a list of integers as input and return an integer representing the length of the longest increasing subsequence. The input list can be empty, and the function should return 0 in this case.
"""

def longestIncreasingSubsequence(nums):
    if len(nums) == 0:
        return 0

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)