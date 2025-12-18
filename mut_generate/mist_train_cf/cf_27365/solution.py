"""
QUESTION:
Given a list of integers representing game scores and a threshold value, calculate the final rating as the maximum of the average score and the threshold value, rounded down to the nearest integer. The final rating should never be less than the threshold value. Implement the function `calculate_final_rating` to achieve this.
"""

from typing import List

def calculate_final_rating(scores: List[int], rv: int) -> int:
    average_score = sum(scores) // len(scores)
    final_rating = max(average_score, rv)
    return final_rating