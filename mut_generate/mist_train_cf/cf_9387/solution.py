"""
QUESTION:
Create a function named `round_list` that takes a list of numbers as input and returns a new list with each number rounded to 4 decimal points. The function should maintain the same order as the input list.
"""

def round_list(numbers):
    return [round(num, 4) for num in numbers]