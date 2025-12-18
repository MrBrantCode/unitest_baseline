"""
QUESTION:
Write a function `calculate_deciles(scores)` that takes a sorted list of integers `scores` with at least 10 elements and returns a dictionary where the keys are the decile indices (0 to 10) and the values are the corresponding decile values. The deciles divide the data into ten equal parts, and the "Zeroth" decile represents the minimum value, while the "Tenth" decile represents the maximum value.
"""

def calculate_deciles(scores):
    scores.sort()
    deciles = {}
    for i in range(11):
        index = int((len(scores) - 1) * (i / 10))
        deciles[i] = scores[index]
    return deciles