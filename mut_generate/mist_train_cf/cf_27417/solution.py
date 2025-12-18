"""
QUESTION:
Implement a function `calculate_average_scores(summary)` that calculates the average score for each student in a class based on their test scores. The function takes a dictionary `summary` where the keys are student names (strings) and the values are lists of test scores (integers) with equal lengths. The function should return a new dictionary where the keys are student names and the values are the average scores (rounded to the nearest integer).
"""

def calculate_average_scores(summary):
    average_scores = {}
    for student, scores in summary.items():
        average_scores[student] = round(sum(scores) / len(scores))
    return average_scores