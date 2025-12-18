"""
QUESTION:
Write a function `calculate_total_scores(scores: List[int]) -> List[int]` that takes a list of integers representing the scores of each round and returns a list of integers representing the total scores of each round, where the score of each player is the sum of their scores in the current and the previous round. If a player has no previous round, their score is just the score of the current round. The function should handle edge cases such as an empty input list or a list with only one score.
"""

from typing import List

def entrance(scores: List[int]) -> List[int]:
    total_scores = []
    prev_score = 0
    for score in scores:
        total_score = score + prev_score
        total_scores.append(total_score)
        prev_score = score
    return total_scores