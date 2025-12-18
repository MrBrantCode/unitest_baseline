"""
QUESTION:
Calculate the average score and standard deviation of a list of scores. 

Create a function named `calculate_unification_scores` that takes a list of scores as input and returns a tuple containing the average score and standard deviation of the input scores. The input list will contain at least one score and all scores are integers or floats between 0 and 10 (inclusive).
"""

import numpy as np

def calculate_unification_scores(scores):
    """
    Calculate the average score and standard deviation of a list of scores.

    Args:
    scores (list): A list of scores. Scores are integers or floats between 0 and 10 (inclusive).

    Returns:
    tuple: A tuple containing the average score and standard deviation of the input scores.
    """
    avg_score = np.mean(scores)
    std_dev = np.std(scores)
    return avg_score, std_dev