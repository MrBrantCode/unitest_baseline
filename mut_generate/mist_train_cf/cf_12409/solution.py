"""
QUESTION:
Find the minimum number of elements from a given set of positive integers that sum up to a target value, where each element can be used multiple times. If it is not possible to reach the target sum, return -1. 

Function: find_optimal_sum(target, numbers) 

Restrictions: 
- The target and the given numbers are positive integers.
- Each number in the set can be used multiple times to reach the target.
- The given set of numbers can be in any order.
"""

def find_optimal_sum(target, numbers):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for current_number in numbers:
        for i in range(current_number, target + 1):
            dp[i] = min(dp[i], dp[i - current_number] + 1)

    return -1 if dp[target] == float('inf') else dp[target]