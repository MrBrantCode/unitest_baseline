"""
QUESTION:
Write a function `max_total_score(nums)` that calculates the maximum total score that can be achieved in a game where a player can either take the score at the current position or skip one score and take the score at the next position.

The function takes a list of integers `nums` as input, representing the scores at each position. The length of the input list is guaranteed to be between 1 and 10^5. The function should return an integer representing the maximum total score that can be achieved.
"""

from typing import List

def max_total_score(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return max(dp)