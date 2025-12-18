"""
QUESTION:
Write a function named `find_max_score` that takes a set of integers as input and returns the maximum score without using any built-in sorting functions or methods. The function should handle the case when the input set is empty.
"""

def find_max_score(scores):
    max_score = None
    for score in scores:
        if max_score is None or score > max_score:
            max_score = score
    return max_score