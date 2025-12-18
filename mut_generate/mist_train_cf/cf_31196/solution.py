"""
QUESTION:
Write a function `calculateTotalScore(scores)` that takes a list of integers as input and returns the total score calculated based on the following rules:
- Each score is added to the total score.
- If a score is a multiple of 3, it is doubled before being added to the total score.
- If a score is a multiple of 5, it is tripled before being added to the total score.
However, to avoid adding the score multiple times, for each score, apply at most one multiplier: if a score is a multiple of both 3 and 5, use the multiplier of 5.
Note that the input list can contain any integers (positive, negative, or zero).
"""

from typing import List

def calculateTotalScore(scores: List[int]) -> int:
    total_score = 0
    for score in scores:
        if score % 5 == 0:
            total_score += score * 3
        elif score % 3 == 0:
            total_score += score * 2
        else:
            total_score += score
    return total_score