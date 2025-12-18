"""
QUESTION:
Write a function `maxNonAdjacentScore` that takes in a list of integers `scores` with a length between 1 and 10^5, where each integer is an integer between -1000 and 1000, and returns the highest possible score that can be achieved by choosing a subset of non-adjacent scores.
"""

def maxNonAdjacentScore(scores: list[int]) -> int:
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