"""
QUESTION:
Write a function `find_highest_score(scores)` that takes a list of integers `scores` with a length between 1 and 100, representing game scores, and returns the highest score achieved in the series.
"""

def find_highest_score(scores):
    highest_score = float('-inf')  # Initialize with negative infinity to ensure any score will be greater
    for score in scores:
        if score > highest_score:
            highest_score = score
    return highest_score