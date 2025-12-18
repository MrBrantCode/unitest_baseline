"""
QUESTION:
Write a function `calculate_total_score(scores)` where `scores` is a list of integers representing game scores with the following conditions:
- 1 <= len(scores) <= 10^5
- 0 <= scores[i] <= 1000
- If the current score is the same as the previous score, the player's total score is doubled; otherwise, the current score is added to the total score.
The function should return the total score according to the game's rules.
"""

from typing import List

def entrance(scores: List[int]) -> int:
    total_score = 0
    prev_score = None
    for score in scores:
        if score == prev_score:
            total_score += score * 2
        else:
            total_score += score
        prev_score = score
    return total_score