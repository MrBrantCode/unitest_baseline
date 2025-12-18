"""
QUESTION:
You are given an integer array `nums`. Perform exactly one operation where you can replace one element `nums[i]` with `nums[i] * nums[i]`. Return the maximum possible subarray sum after exactly one operation. The subarray must be non-empty and must contain at least one negative number. 

Function Name: maxSubarraySumAfterOneOperation 
Input: nums (integer array) 
Output: maximum possible subarray sum 
Constraints: 1 <= nums.length <= 10^5, -10^4 <= nums[i] <= 10^4, at least one nums[i] must be negative.
"""

def maxSubarraySumAfterOneOperation(nums):
    n = len(nums)
    
    # check if there is any positive number in the list
    if max(nums)<=0:
        return max(nums)**2

    dp, dp2 = [0]*n, [0]*n

    dp[0] = nums[0]
    dp2[0] = nums[0]**2

    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1]+nums[i])
        dp2[i] = max(dp[i-1]+nums[i]*nums[i], nums[i]*nums[i], dp2[i-1]+nums[i])

    return max(max(dp2),dp[-1])