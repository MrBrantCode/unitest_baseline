"""
QUESTION:
Write a function `maxNonAdjacentScore` that takes a list of integers `scores` and returns the highest possible score achievable by choosing a subset of non-adjacent scores. The function should return 0 if the input list is empty.
"""

from typing import List

def maxNonAdjacentScore(scores: List[int]) -> int:
    if not scores:
        return 0
    if len(scores) <= 2:
        return max(scores)

    dp = [0] * len(scores)
    dp[0] = scores[0]
    dp[1] = max(scores[0], scores[1])

    for i in range(2, len(scores)):
        dp[i] = max(dp[i-1], dp[i-2] + scores[i])

    return dp[-1]