"""
QUESTION:
Implement a function `maxProduct(nums)` that finds the maximum product of a contiguous non-empty subarray within the given integer array `nums`, with the condition that the subarray must contain at least one positive number. The input array `nums` is guaranteed to have at least one positive number and its length is between 1 and 2 * 10^4. The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.
"""

def maxProduct(nums):
    max_dp = [0]*len(nums)
    min_dp = [0]*len(nums)
    max_dp[0] = min_dp[0] = nums[0]
    for i in range(1,len(nums)):
        if nums[i] > 0:
            max_dp[i] = max(nums[i], max_dp[i-1]*nums[i])
            min_dp[i] = min(nums[i], min_dp[i-1]*nums[i])
        else:
            max_dp[i] = max(nums[i], min_dp[i-1]*nums[i])
            min_dp[i] = min(nums[i], max_dp[i-1]*nums[i])
    return max(max_dp)