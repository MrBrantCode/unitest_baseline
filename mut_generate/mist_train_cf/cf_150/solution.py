"""
QUESTION:
Create a function `squares_of_odd_numbers_greater_than_ten` that takes a list of integers as input and returns a new list containing the squares of the odd numbers greater than 10 from the original list.
"""

def squares_of_odd_numbers_greater_than_ten(lst):
    """Returns a new list containing the squares of the odd numbers greater than 10 from the original list."""
    return [x**2 for x in lst if x > 10 and x % 2 != 0]