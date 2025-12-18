"""
QUESTION:
You are given a list of integers representing the scores of a game. Write a function `calculate_average_score(scores)` that takes in a list of integers `scores` with a length between 2 and 100 (inclusive), and returns the average score excluding the highest and lowest scores. If there are multiple occurrences of the highest or lowest score, only one instance of each should be excluded from the average.
"""

def calculate_average_score(scores):
    if len(scores) < 4:
        return 0  # Not enough scores to calculate average

    total_score = sum(scores) - min(scores) - max(scores)
    num_scores = len(scores) - 2  # Excluding the highest and lowest scores
    average_score = total_score / num_scores
    return average_score