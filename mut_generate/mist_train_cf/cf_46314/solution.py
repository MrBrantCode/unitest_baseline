"""
QUESTION:
Write a function `format_data(data)` that takes a list of floating point numbers and returns a string representation of the numbers, formatted to two decimal places, separated by commas. The function should be optimized for large datasets, minimizing both time and space complexity, and only using standard Python libraries.
"""

def format_data(data):
    return ", ".join((f"{i:.2f}" for i in data))