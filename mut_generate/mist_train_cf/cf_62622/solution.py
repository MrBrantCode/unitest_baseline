"""
QUESTION:
Given a non-empty integer array `nums` and an integer `k`, return the maximum absolute sum of any subarray of `nums` with exactly `k` elements. The absolute sum of a subarray is the absolute value of the sum of its elements. Note that `abs(x)` is defined as `-x` if `x` is negative and `x` if `x` is non-negative.

Constraints: 
`1 <= nums.length <= 10^5`, `1 <= k <= nums.length`, and `-10^4 <= nums[i] <= 10^4`.
"""

def maxAbsoluteSum(nums, k):
    n = len(nums)
    prefix_sum = [0]*(n+1)
    
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1]+nums[i-1]
        
    max_sum = float('-inf')
    min_sum = float('inf')
    
    for i in range(k, n+1):
        max_sum = max(max_sum, prefix_sum[i] - prefix_sum[i-k])
        min_sum = min(min_sum, prefix_sum[i] - prefix_sum[i-k])
        
    return max(abs(max_sum), abs(min_sum))