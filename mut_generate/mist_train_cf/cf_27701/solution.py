"""
QUESTION:
Write a function `calculate_average_score(scores)` that takes a list of integers `scores` with a length between 2 and 100 (inclusive) and returns the average score, rounded to the nearest integer, after excluding the highest and lowest scores.
"""

def calculate_average_score(scores):
    if len(scores) < 4:
        return round(sum(scores) / len(scores))
    
    scores.sort()
    return round(sum(scores[1:-1]) / (len(scores) - 2))