"""
QUESTION:
Write a function `calculate_final_score(scores)` that takes a list of integers `scores` as input and returns the final score after applying the rule that if the current score is the same as the previous score, the current score is discounted. The list `scores` contains integers in the range [-100, 100] and has a length between 0 and 10^5.
"""

from typing import List

def entrance(scores: List[int]) -> int:
    if not scores:
        return 0

    final_score = scores[0]
    prev_score = scores[0]

    for score in scores[1:]:
        if score != prev_score:
            final_score += score
            prev_score = score

    return final_score