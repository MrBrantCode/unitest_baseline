"""
QUESTION:
Write a function `findMaxScore` that takes a 2D array `scores` as input, where each row represents a player's scores in different game levels, and returns the maximum total score that can be achieved by selecting one score from each player. If a player has no scores, their total score is considered to be 0. The function should handle cases where the `scores` array is empty, the number of games for each player may vary, and the number of players may vary.
"""

from typing import List

def findMaxScore(scores: List[List[int]]) -> int:
    if not scores:  
        return 0

    maxScore = 0
    for playerScores in scores:
        totalScore = sum(playerScores)
        maxScore = max(maxScore, totalScore)

    return maxScore