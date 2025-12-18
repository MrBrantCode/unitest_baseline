"""
QUESTION:
You are given a list of integers representing the scores of a game where a player gains a point for a higher score than the previous player and loses a point for a lower or equal score. Write a function `calculate_points(scores: List[int]) -> int` that calculates the total points gained or lost by the players based on the given scores, where the input list `scores` has a length between 1 and 100 inclusive.
"""

from typing import List

def calculate_points(scores: List[int]) -> int:
    total_points = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[i-1]:
            total_points += 1
        else:
            total_points -= 1
    return total_points