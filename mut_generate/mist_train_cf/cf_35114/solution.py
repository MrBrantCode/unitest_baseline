"""
QUESTION:
Given a list of integers representing the scores of a game, write a function `calculate_final_score(scores)` to calculate the final score according to the following rules: 
- A player's score is the sum of the scores of the last two turns.
- If the last two turns have the same score, the player's score is doubled instead.
The input list `scores` contains at least two elements. The function should return the final score as an integer.
"""

from typing import List

def calculate_final_score(scores: List[int]) -> int:
    if len(scores) <= 2:
        return sum(scores)
    
    total_score = scores[0] + scores[1]
    for i in range(2, len(scores)):
        if scores[i-1] == scores[i-2]:
            total_score *= 2
        else:
            total_score += scores[i]
    
    return total_score