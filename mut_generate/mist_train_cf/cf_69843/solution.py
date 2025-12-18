"""
QUESTION:
Write a function `MaximumScore` that takes an array `score` of length `n` as input, where `score[i]` is the score of the `i-th` problem, and returns the maximum score among all problems.
"""

def MaximumScore(score):
    """
    This function calculates the maximum score among all problems in a given assignment.

    Parameters:
    score (list): A list of scores for each problem in the assignment.

    Returns:
    int: The maximum score among all problems.
    """
    max_score = 0
    for i in range(len(score)):
        if score[i] > max_score:
            max_score = score[i]
    return max_score