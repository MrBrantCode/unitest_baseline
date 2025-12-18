"""
QUESTION:
Write a function `maxSubarraySumAfterOneOperation(nums)` that takes an array of integers `nums` as input and returns the highest possible sum of a subarray after performing exactly one operation where you can substitute one element `nums[i]` with the square of that element, `nums[i] * nums[i]`. The subarray should not be empty. The length of `nums` is within the range `1 <= nums.length <= 10^5` and the elements of `nums` are within the range `-10^4 <= nums[i] <= 10^4`.
"""

def maxSubarraySumAfterOneOperation(nums):
    n = len(nums)
    f, g = [0]*n, [0]*n     
    f[0] = nums[0]
    g[0] = nums[0]**2   
    for i in range(1, n):
        g[i] = max(g[i-1] + nums[i], f[i-1] + nums[i]**2)
        f[i] = max(f[i-1] + nums[i], nums[i])
    return max(max(f), max(g))