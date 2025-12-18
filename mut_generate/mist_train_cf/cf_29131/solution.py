"""
QUESTION:
Write a function `calculate_average_score(scores)` that takes a list of at least 3 unique integers `scores` and returns the average of the scores excluding the highest and lowest scores, rounded to the nearest whole number.
"""

def calculate_average_score(scores):
    scores.sort()
    scores = scores[1:-1]
    average_score = round(sum(scores) / len(scores))
    return average_score