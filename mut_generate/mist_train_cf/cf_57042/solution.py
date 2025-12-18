"""
QUESTION:
Write a function `maxSumDivByThree(nums)` that determines the highest possible sum of elements in the given array `nums` that is divisible by three. The length of `nums` is between 1 and 4 * 10^4, inclusive, and each element in `nums` is an integer ranging from 1 to 10^4, inclusive.
"""

def maxSumDivByThree(nums):
    dp = [0, float('-inf'), float('-inf')]
    for num in nums:
        dp = [max(dp[i], num + dp[(i-num % 3) % 3]) for i in range(3)]
    return dp[0]