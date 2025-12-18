"""
QUESTION:
Write a function `get_odd_numbers` that takes a list of integers as input and returns a new list containing only the odd numbers without using any conditional statements or loops.
"""

def get_odd_numbers(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))