"""
QUESTION:
Given a list of integers `nums`, implement a function `longestIncreasingSubsequence(nums)` to find the length of the longest increasing subsequence within `nums` using dynamic programming. The function should return the maximum length of the increasing subsequence. The input list `nums` can be empty. The solution should have a time complexity of O(n^2) and a space complexity of O(n).
"""

def longestIncreasingSubsequence(nums):
    if not nums:
        return 0

    dp = [1]*len(nums)
    for i in range (1 , len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)