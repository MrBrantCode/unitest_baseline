"""
QUESTION:
Create a function `append_two` that takes a list of integers as input and returns a new list where each element is a string representation of the original integer with '2' appended to it.
"""

def append_two(lst):
    return [str(i) + '2' for i in lst]