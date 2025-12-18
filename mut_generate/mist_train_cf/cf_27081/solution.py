"""
QUESTION:
Implement a function `maxGameScore(scores)` that takes a list of integers representing game scores as input, where the game ends immediately when a score of 0 is encountered. The function should return the maximum score that can be achieved by summing consecutive scores before a 0 is encountered. The function should iterate through the list only once and handle cases where the list does not contain a 0.
"""

from typing import List

def maxGameScore(scores: List[int]) -> int:
    max_score = 0
    current_score = 0
    for score in scores:
        if score == 0:
            max_score = max(max_score, current_score)
            current_score = 0
        else:
            current_score += score
    return max(max_score, current_score)