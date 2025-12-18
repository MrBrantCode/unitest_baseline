"""
QUESTION:
Write a function `calculate_total_score(scores)` that takes a list of integers `scores` of length between 1 and 100, representing the scores of a game. For each turn, calculate the score as the sum of the current and previous turn's scores. If the current and previous scores are the same, double the sum. Return the total score of the player based on the given list of scores.
"""

from typing import List

def calculate_total_score(scores: List[int]) -> int:
    total_score = 0
    prev_score = 0
    for score in scores:
        if score == prev_score:
            total_score += (score + prev_score) * 2
        else:
            total_score += score + prev_score
        prev_score = score
    return total_score