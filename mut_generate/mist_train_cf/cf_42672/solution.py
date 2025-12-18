"""
QUESTION:
Write a function `calculateAverageScore(scores)` that calculates the average score of a game, excluding the highest and lowest scores. The function takes in a list of integers `scores` where 2 <= len(scores) <= 100 and returns the average score, rounded to the nearest integer.
"""

def calculateAverageScore(scores):
    if len(scores) < 4:
        return round(sum(scores) / len(scores))
    
    scores.sort()
    return round(sum(scores[1:-1]) / (len(scores) - 2))