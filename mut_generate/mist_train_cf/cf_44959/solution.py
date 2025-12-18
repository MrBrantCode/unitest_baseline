"""
QUESTION:
Given a list of integers, write a function `lengthOfLIS(nums)` to find the length of the longest strictly increasing subsequence within the list. The function should be able to handle a list of up to 10,000 elements in length and have a time complexity no worse than O(n log n).
"""

from bisect import bisect_left

def lengthOfLIS(nums):
    dp = []
    for i in range(len(nums)):
        # Find first number in dp >= nums[i] using binary search
        idx = bisect_left(dp, nums[i])
        if idx == len(dp):
            # If not found, append it to the tail
            dp.append(nums[i])
        else:
            # Otherwise update dp[idx]
            dp[idx] = nums[i]
    return len(dp)