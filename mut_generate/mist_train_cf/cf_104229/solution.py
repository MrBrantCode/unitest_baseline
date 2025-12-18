"""
QUESTION:
Create a function `calculate_scores` that takes a list of scores as input and returns the maximum score, minimum score, average score, and median score. The input list may contain duplicate values.
"""

import statistics

def calculate_scores(scores):
    """
    Calculate the maximum score, minimum score, average score, and median score.

    Args:
    scores (list): A list of scores.

    Returns:
    tuple: A tuple containing the maximum score, minimum score, average score, and median score.
    """
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)
    median_score = statistics.median(scores)
    return max_score, min_score, avg_score, median_score