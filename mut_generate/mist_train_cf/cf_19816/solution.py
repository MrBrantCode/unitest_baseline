"""
QUESTION:
Create a function called `find_optimal_sum` that takes two parameters: a list of positive integers `nums` and a target integer `target`. The function should find the minimum number of elements from the list `nums` that sum up to the `target`, with the option to reuse elements from `nums` multiple times. If it's impossible to reach the `target` or determine the optimal sum, return -1.
"""

def find_optimal_sum(nums, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for i in range(1, target + 1):
        for j in nums:
            if j <= i and dp[i - j] + 1 < dp[i]:
                dp[i] = dp[i - j] + 1

    if dp[target] == float('inf'):
        return -1
    else:
        return dp[target]