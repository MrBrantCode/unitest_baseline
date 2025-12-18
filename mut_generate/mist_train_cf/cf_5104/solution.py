"""
QUESTION:
Write a function named `optimalSum` that takes two parameters: a positive integer `target` and a list of positive integers `nums`. The function should return the minimum number of unique elements in `nums` needed to sum up to `target` using the elements in `nums` any number of times. If it's impossible to sum up to `target` or if the optimal sum cannot be determined, return -1.
"""

def optimalSum(target, nums):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for num in nums:
        for i in range(num, target + 1):
            if dp[i - num] + 1 < dp[i]:
                dp[i] = dp[i - num] + 1

    if dp[target] == float('inf'):
        return -1

    return dp[target]