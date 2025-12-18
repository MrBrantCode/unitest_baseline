"""
QUESTION:
Write a function `calculateAverageScore(scores)` that takes a list of integers `scores` (length between 2 and 100 inclusive) and returns the average score, rounded to the nearest integer, after excluding the highest and lowest scores.
"""

def calculateAverageScore(scores):
    if len(scores) < 4:
        return "Not enough scores to calculate average"
    
    scores.sort()
    trimmed_scores = scores[1:-1]  # Exclude the highest and lowest scores
    average_score = round(sum(trimmed_scores) / len(trimmed_scores))
    return average_score