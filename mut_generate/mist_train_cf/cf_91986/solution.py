"""
QUESTION:
Create a function named `round_and_format` that takes a list of numbers as input, rounds each number to the nearest thousandth decimal place, formats it as a string, and returns a new list of the formatted strings sorted in ascending order based on the rounded values.
"""

def round_and_format(numbers):
    return sorted(['{:.3f}'.format(round(number, 3)) for number in numbers])