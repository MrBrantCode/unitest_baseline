"""
QUESTION:
Calculate the total score of a game given a list of integers representing scores, where consecutive duplicate scores are not counted towards the total score. Write a function `calculate_total_score(scores: List[int]) -> int` that takes in a list of integers `scores` with a length between 1 and 10^5 and returns the total score of the game, ensuring efficiency for large inputs.
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