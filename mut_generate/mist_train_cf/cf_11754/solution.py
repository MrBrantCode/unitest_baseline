"""
QUESTION:
Create a function `round_and_format` that takes a list of numbers as input. The function should round each number to the nearest thousandth decimal place, format it as a string, and sort the list in ascending order based on the rounded values. The function should return the sorted list of formatted strings.
"""

def round_and_format(numbers):
    return sorted(['{:.3f}'.format(round(num, 3)) for num in numbers])