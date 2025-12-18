"""
QUESTION:
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. However, the subarray cannot contain any two consecutive numbers. The length of `nums` is between 1 and 3 * 10^4 (inclusive), and each number in `nums` is between -10^5 and 10^5 (inclusive). Implement the function `maximum_subarray(nums)` to solve this problem.
"""

def maximum_subarray(nums):
    if not nums:
        return 0
    elif len(nums) <= 2:
        return max(nums)
        
    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
    return dp[-1]