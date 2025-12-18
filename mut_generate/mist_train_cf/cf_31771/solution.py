"""
QUESTION:
Write a function `calculateTotalScore(scores)` to calculate the total score of a game given a list of integers representing the scores. The function should discount the current score if it is the same as the previous score and return the total score after applying this rule.

- `scores`: a list of integers (1 <= len(scores) <= 1000, 0 <= scores[i] <= 100)
"""

def calculateTotalScore(scores):
    total_score = 0
    prev_score = None
    for score in scores:
        if score != prev_score:
            total_score += score
        prev_score = score
    return total_score