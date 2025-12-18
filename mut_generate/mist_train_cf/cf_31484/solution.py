"""
QUESTION:
Write a function `calculateAverageScore` that takes in a list of integers `scores` and returns the average score, rounded to the nearest whole number, excluding the highest and lowest scores. The input list `scores` will always contain at least 3 elements, and all elements are valid integers.
"""

def calculateAverageScore(scores):
    scores.sort()
    scores = scores[1:-1]
    average_score = round(sum(scores) / len(scores))
    return average_score