"""
QUESTION:
Given a non-empty array `nums` containing positive integers, determine if the array can be divided into two subsets with equal sums. 

Function name: canPartition 
Input: nums (list of integers) 
Constraints: 1 <= nums.length <= 200, 1 <= nums[i] <= 100 
Return: True if the array can be divided into two subsets with equal sums, False otherwise.
"""

def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0: 
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            if dp[i - num]:
                dp[i] = True
    return dp[target]