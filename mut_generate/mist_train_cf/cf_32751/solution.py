"""
QUESTION:
Implement a function `round_reputation_scores` that takes a list of floating-point numbers representing reputation scores and returns a new list with the reputation scores rounded. The function should round each score to the maximum number of decimal places (between 3 and 12) such that it is different from the previously rounded score. If there is no previous score, round to 12 decimal places.
"""

from typing import List

def round_reputation_scores(scores: List[float]) -> List[float]:
    rounded_scores = []
    for score in scores:
        decimal_places = 12
        while decimal_places >= 3:
            rounded_score = round(score, decimal_places)
            if not rounded_scores or rounded_score != round(rounded_scores[-1], decimal_places):
                rounded_scores.append(rounded_score)
                break
            decimal_places -= 1
    return rounded_scores