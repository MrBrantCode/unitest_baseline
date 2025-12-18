"""
QUESTION:
Create a function `round_numbers` that takes a list of numbers as input and returns a new list with each number rounded to 4 decimal points. The function should maintain the original order of the numbers and only use built-in mathematical functions.
"""

def round_numbers(numbers):
    return [round(number, 4) for number in numbers]