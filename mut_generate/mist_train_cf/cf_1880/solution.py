"""
QUESTION:
Write a function called `longestIncreasingSubsequence` that takes a list of integers as input and returns the length of the longest increasing subsequence, where each number in the subsequence is greater than the previous number. The function should return 0 if the input list is empty.
"""

def longestIncreasingSubsequence(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)