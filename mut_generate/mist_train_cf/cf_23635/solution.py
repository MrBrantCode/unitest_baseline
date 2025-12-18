"""
QUESTION:
Write a function `longest_increasing_subsequence` that takes an array of integers and its length as input. The function should return the longest increasing subsequence in the array. 

The subsequence should be strictly increasing, i.e., each element should be greater than the previous one.
"""

def longest_increasing_subsequence(nums):
    if not nums:
        return []

    dp = [[num] for num in nums]

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [nums[i]]

    return max(dp, key=len)