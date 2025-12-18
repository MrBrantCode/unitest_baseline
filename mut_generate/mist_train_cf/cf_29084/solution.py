"""
QUESTION:
Write a function `calculateAverage(scores)` that takes a list of integers `scores` with at least three elements, excludes the highest and lowest scores, and returns the average of the remaining scores rounded to the nearest whole number.
"""

def calculateAverage(scores):
    if len(scores) < 3:
        return 0  # No valid average if less than 3 scores

    scores.sort()  # Sort the scores in ascending order
    trimmed_scores = scores[1:-1]  # Exclude the highest and lowest scores
    average = round(sum(trimmed_scores) / len(trimmed_scores))  # Calculate the average and round to the nearest whole number
    return average