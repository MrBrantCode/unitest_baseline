"""
QUESTION:
Given a list of integers `scores`, write a function `calculate_total_scores` to calculate the total score for each round. The total score for each round is the sum of the current score and the scores of the previous two rounds. If there are not enough previous rounds, the total score is the sum of scores in the available previous rounds. The function should return a list of integers representing the total score for each round. 

Restrictions: The input list `scores` contains 1 to 1000 integers, each between 0 and 100.
"""

from typing import List

def calculate_total_scores(scores: List[int]) -> List[int]:
    total_scores = []
    for i in range(len(scores)):
        if i == 0:
            total_scores.append(scores[i])
        elif i == 1:
            total_scores.append(scores[i-1] + scores[i])
        else:
            total_scores.append(sum(scores[i-2:i+1]))
    return total_scores