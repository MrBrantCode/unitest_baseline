"""
QUESTION:
Create a function `square_exclude_divisible_by_three` that takes a list of integers as input, and returns a new list containing the square of each element, excluding any elements that are divisible by 3.
"""

def square_exclude_divisible_by_three(numbers):
    return [x**2 for x in numbers if x % 3 != 0]