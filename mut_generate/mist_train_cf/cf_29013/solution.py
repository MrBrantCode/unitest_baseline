"""
QUESTION:
Write a function `calculateTotalScore(scores)` that takes a list of integers `scores` (0 <= scores[i] <= 100) representing game scores. Calculate the total score by summing the scores of the last two turns, doubling the sum if the last two turns have the same score. Return the total score as an integer.
"""

def entance(scores):
    total_score = 0
    if len(scores) >= 2:
        last_two_sum = scores[-1] + scores[-2]
        total_score = last_two_sum * (2 if scores[-1] == scores[-2] else 1)
    return total_score