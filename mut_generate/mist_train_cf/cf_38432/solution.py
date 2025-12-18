"""
QUESTION:
Given a list of integers representing game scores, write a function `calculate_average_score(scores)` that calculates the average score, excluding any scores that are negative. If there are no positive scores, the function should return 0.
"""

def calculate_average_score(scores):
    positive_scores = [score for score in scores if score >= 0]
    if positive_scores:
        average_score = sum(positive_scores) / len(positive_scores)
        return average_score
    else:
        return 0