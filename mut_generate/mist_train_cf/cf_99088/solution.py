"""
QUESTION:
Write a function `format_numbers(numbers, width)` that takes a list of numbers and a width constraint as input and returns a string where each number in the list is formatted to fit within the specified width, handling negative numbers by including the sign within the width constraint.
"""

def format_numbers(numbers, width):
    specifier = "{:>{}}"
    formatted_numbers = [specifier.format(number, width) for number in numbers]
    separator = ", "
    return separator.join(formatted_numbers)