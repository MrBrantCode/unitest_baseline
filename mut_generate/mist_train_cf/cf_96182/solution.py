"""
QUESTION:
Create a function called `longest_increasing_subsequence` that takes a list of positive integers as input and returns the length of the longest increasing subsequence. The function should implement a dynamic programming approach and have a time complexity of O(n^2). The input list contains at least one element.
"""

def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)