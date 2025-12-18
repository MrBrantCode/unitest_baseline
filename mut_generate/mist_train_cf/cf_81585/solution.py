"""
QUESTION:
Implement a function called `square_data` that takes a list of integers as input, calculates the square of each distinct element, and returns a list of the squared values.
"""

def square_data(data):
    return [i ** 2 for i in set(data)]