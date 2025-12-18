"""
QUESTION:
Implement a function `update_high_scores` that takes a list of high scores and a new score as input, adds the new score to the list, and returns the updated list in descending order. The function should be able to handle any number of high scores. The list should be updated by appending the new score and then sorting the list in descending order.
"""

from typing import List

def update_high_scores(high_scores: List[int], new_score: int) -> List[int]:
    high_scores.append(new_score)  
    high_scores.sort(reverse=True)  
    return high_scores