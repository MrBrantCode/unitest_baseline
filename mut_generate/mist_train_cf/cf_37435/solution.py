"""
QUESTION:
Write a function `calculateAverage` that takes a list of integers as input, excluding the highest and lowest scores, and returns the average score rounded to the nearest whole number. The function should handle cases where the list has two or fewer elements, in which case all scores are included in the average.
"""

from typing import List

def calculateAverage(scores: List[int]) -> int:
    if len(scores) <= 2:
        return round(sum(scores) / len(scores))
    
    scores.sort()
    return round(sum(scores[1:-1]) / (len(scores) - 2))