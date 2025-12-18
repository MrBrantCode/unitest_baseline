"""
QUESTION:
Write a function `calculate_final_score` that takes a list of integers `scores` and an integer `threshold` as input. The function should calculate the final score of a game where each turn's score is the sum of the previous two turns' scores, but not exceeding the threshold. The function should return the sum of all scores after applying this rule.

Input: 
- `scores`: a list of 2 to 100 non-negative integers not exceeding 1000.
- `threshold`: an integer between 1 and 1000.

Output:
- The final score of the game as an integer.
"""

from typing import List

def calculate_final_score(scores: List[int], threshold: int) -> int:
    final_scores = [min(scores[0], threshold), min(scores[1], threshold)]
    for i in range(2, len(scores)):
        current_score = scores[i] + final_scores[i-1] + final_scores[i-2]
        final_scores.append(min(current_score, threshold))
    return sum(final_scores)