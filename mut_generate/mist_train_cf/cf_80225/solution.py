"""
QUESTION:
Write a function `compute_longest_side` that calculates the length of the longest side of a piece of paper after two folds, given the original length of the longest side, with each fold reducing the length of what was then the longer side. The function should return the result rounded to the nearest decimal point.
"""

def compute_longest_side(length, folds):
    for _ in range(folds):
        length /= 2
    return round(length, 1)