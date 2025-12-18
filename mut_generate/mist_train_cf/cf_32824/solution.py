"""
QUESTION:
Write a function `calculateAverage(scores)` that takes a list of integers `scores` with a length between 2 and 100 (inclusive) and returns the average score, excluding the lowest and highest scores, rounded to two decimal places.
"""

def entrance(scores):
    if len(scores) < 3:
        return "At least 3 scores are required to calculate the average."

    sorted_scores = sorted(scores)
    trimmed_scores = sorted_scores[1:-1]  # Exclude the lowest and highest scores
    average = sum(trimmed_scores) / len(trimmed_scores)
    return round(average, 2)