"""
QUESTION:
Write a function `calculate_points` that takes a list of integers representing game scores and returns the total points earned based on the following rules: 
- If a player's score is greater than or equal to the previous player's score, they receive a bonus of 2 points.
- Otherwise, they receive a penalty of 1 point.
- The first player receives a bonus of 2 points if their score is greater than 0, and no bonus or penalty if their score is 0 or less.
"""

from typing import List

def entrance(scores: List[int]) -> int:
    total_points = 0
    if scores[0] > 0:
        total_points += 2
    for i in range(1, len(scores)):
        if scores[i] >= scores[i-1]:
            total_points += 2
        else:
            total_points -= 1
    return total_points