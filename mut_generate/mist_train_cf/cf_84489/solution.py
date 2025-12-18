"""
QUESTION:
Write a function called `calculate_difference` that takes a dictionary of numbers (integers and floats) as input and returns the difference between the maximum and minimum values in the dictionary.
"""

def calculate_difference(numbers):
    values = numbers.values()
    max_val = max(values)
    min_val = min(values)
    difference = max_val - min_val
    return difference