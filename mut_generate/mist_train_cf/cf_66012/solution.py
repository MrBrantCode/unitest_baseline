"""
QUESTION:
Create a function called `find_symmetrical_numbers` that takes a list of integers as input and returns a list of integers where each integer is symmetrical, meaning it reads the same forward and backward.
"""

def find_symmetrical_numbers(lst):
    # Use list comprehension to filter out symmetrical numbers
    # numbers are converted to string for reverse comparison
    return [n for n in lst if str(n) == str(n)[::-1]]