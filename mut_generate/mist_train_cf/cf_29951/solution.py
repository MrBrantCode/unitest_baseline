"""
QUESTION:
Write a function `calculate_total_score(scores)` that takes a list of integers `scores` and returns the total score after applying the rule: if the current score is the same as the previous score, the current score is discounted.
"""

from typing import List

def calculate_total_score(scores: List[int]) -> int:
    total_score = 0
    prev_score = None
    for score in scores:
        if score != prev_score:
            total_score += score
        prev_score = score
    return total_score