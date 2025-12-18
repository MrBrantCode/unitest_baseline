"""
QUESTION:
Write a function `calculate_mean` that takes a list of integers as input and returns the mean average. The function should return an error message if the input list is empty or contains non-integer elements.
"""

def calculate_mean(lst):
    if not lst:
        return "Error: The list is empty."
    
    if not all(isinstance(x, int) for x in lst):
        return "Error: The list contains non-integer elements."
    
    return sum(lst) / len(lst)