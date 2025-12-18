"""
QUESTION:
Write a function `lengthOfLIS(nums)` to find the length of the longest increasing subsequence (LIS) within the list of integers `nums`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. The function should return the length of the longest increasing subsequence. The input `nums` is a list of integers, and the function should return an integer.
"""

def lengthOfLIS(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)