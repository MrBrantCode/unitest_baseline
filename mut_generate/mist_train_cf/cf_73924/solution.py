"""
QUESTION:
Filter the numbers in a list that are less than or equal to a given boundary limit.

Write a function `filter_numbers` that takes a list of integers and a boundary limit as input, and returns a new list containing only the numbers that are less than or equal to the boundary limit.
"""

def filter_numbers(numbers, boundary_limit):
    return [num for num in numbers if num <= boundary_limit]