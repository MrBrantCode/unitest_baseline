"""
QUESTION:
Create a function called `add_positive_numbers` that takes a list of numbers as input. The function should sort the list in ascending order, exclude any negative numbers, and then return the sum of the remaining numbers.
"""

def add_positive_numbers(numbers):
    return sum(sorted([num for num in numbers if num > 0]))