"""
QUESTION:
Write a function named `compute_average_age` that takes a list of numbers as input and returns their average. The function should be able to handle a list of any length.
"""

def compute_average_age(ages):
    return sum(ages) / len(ages)