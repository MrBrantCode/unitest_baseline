"""
QUESTION:
Create a function `get_odd_numbers` that takes a list of integers as input and returns a new list containing only the odd numbers from the original list. The function should use a list comprehension to achieve this.
"""

def get_odd_numbers(numbers):
    return [x for x in numbers if x % 2 != 0]