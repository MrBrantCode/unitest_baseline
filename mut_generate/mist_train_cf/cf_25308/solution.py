"""
QUESTION:
Write a function `max_sum_with_no_duplicates` that takes an array of integers as input and returns the highest sum that can be obtained by including different members from the array, such that no two members have the same index.
"""

def max_sum_with_no_duplicates(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [[0, 0] for _ in range(n)]
    
    dp[0][0] = 0
    dp[0][1] = nums[0]
    
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = dp[i-1][0] + nums[i]
    
    return max(dp[-1][0], dp[-1][1])