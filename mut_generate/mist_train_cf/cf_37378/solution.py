"""
QUESTION:
Write a function `highest_score` that takes a list of integers as input, each representing a score in a game, and returns the highest score achievable by removing exactly one score from the list. The function should return the maximum possible score.
"""

def highest_score(scores):
    max_score = max(scores)
    if scores.count(max_score) > 1:
        return max_score * 2
    else:
        scores.remove(max_score)
        return max(scores)