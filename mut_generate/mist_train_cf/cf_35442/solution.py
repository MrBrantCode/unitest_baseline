"""
QUESTION:
Implement a function `longestIncreasingSubsequence` that takes an array of integers `nums` as input and returns the length of the longest increasing subsequence in the array. The function should find the longest sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements, and where the elements are in increasing order.
"""

def longestIncreasingSubsequence(nums):
    n = len(nums)
    if n == 0:
        return 0

    dp = [1] * n  

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)  

    return max(dp)  