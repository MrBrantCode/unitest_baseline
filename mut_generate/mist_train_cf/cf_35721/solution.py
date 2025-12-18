"""
QUESTION:
Implement the `longestIncreasingSubsequence` function, which takes a list of integers `nums` as input and returns the length of the longest increasing subsequence within the sequence. A subsequence is a sequence derived from another sequence by deleting some or no elements without changing the order of the remaining elements, and an increasing subsequence is a subsequence in which the elements are in non-decreasing order.
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