"""
QUESTION:
Write a function `calculate_mean` that takes a list of numbers as input and returns the mean of the list. The function should handle the case where the input list is empty and return `None` in this case.
"""

def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else None