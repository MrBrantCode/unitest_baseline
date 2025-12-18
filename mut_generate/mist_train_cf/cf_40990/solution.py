"""
QUESTION:
Write a function `maxPossibleScore` that takes a list of integers `scores` representing the scores of a game and returns the maximum possible score that can be achieved, where a player's score is the sum of the scores of the last two moves, and the player starts with a score of 0. The input list `scores` contains at least two integers, and the output should be an integer.
"""

from typing import List

def maxPossibleScore(scores: List[int]) -> int:
    if len(scores) <= 2:
        return sum(scores)
    
    dp = [0] * len(scores)
    dp[0] = scores[0]
    dp[1] = scores[1]
    
    for i in range(2, len(scores)):
        dp[i] = max(dp[i-1], dp[i-2]) + scores[i]
    
    return max(dp[-1], dp[-2])