"""
QUESTION:
Implement a function named `calculate_average_scores` that takes in a dictionary `scores` where the keys are student names and the values are lists of test scores, and an optional parameter `average_type` which specifies the type of average to be calculated (mean, median, or mode) and defaults to 'mean' if not specified. The function should return a dictionary with the calculated average score for each student.
"""

from statistics import mean, median, mode

def calculate_average_scores(scores, average_type='mean'):
    average_functions = {
        'mean': mean,
        'median': median,
        'mode': mode
    }

    average_func = average_functions.get(average_type, mean)

    average_scores = {}
    for student, score_list in scores.items():
        average_scores[student] = average_func(score_list)

    return average_scores