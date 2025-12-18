"""
QUESTION:
Write a function `countWaysToReachTarget` that takes in a list of integers `scores` and an integer `target` as parameters. The function should return the number of ways to reach the target score by summing up the scores in the list, where each score can be used any number of times. The input restrictions are 1 <= scores.length <= 100, 1 <= scores[i] <= 1000, and 1 <= target <= 10000.
"""

from typing import List

def countWaysToReachTarget(scores: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(1, target + 1):
        for score in scores:
            if i - score >= 0:
                dp[i] += dp[i - score]

    return dp[target]