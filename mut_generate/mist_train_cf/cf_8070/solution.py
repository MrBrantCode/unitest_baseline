"""
QUESTION:
Create a function called `calculate_average` that calculates the average of a list of numbers and returns the result rounded to the nearest integer. The input is a list of integers representing the scores.
"""

def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    average = round(total / len(scores))
    return average