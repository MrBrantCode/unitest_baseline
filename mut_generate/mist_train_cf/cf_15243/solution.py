"""
QUESTION:
Create a function `square_odd_numbers` that takes a list of integers as input and returns a new list containing the squares of only the odd numbers from the input list.
"""

def square_odd_numbers(lst):
    return [x**2 for x in lst if x % 2 != 0]