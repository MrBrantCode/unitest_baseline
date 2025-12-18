"""
QUESTION:
Implement a function `calculate_average_score` that takes a list of student scores as input and returns the average score rounded to the nearest integer. If the average score is exactly halfway between two integers, it should be rounded up. The function should handle a list of integers representing the student scores and return an integer representing the average score.
"""

from typing import List

def calculate_average_score(scores: List[int]) -> int:
    return round(sum(scores) / len(scores))