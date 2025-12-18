"""
QUESTION:
Create a function called `square_dict` that takes a list of integers as input and returns a dictionary where each integer in the list is a key and its corresponding value is a list containing the integer itself and its square.
"""

def square_dict(lst):
    """Returns a dictionary where each integer in the input list is a key and its corresponding value is a list containing the integer itself and its square."""
    return {element: [element, element**2] for element in lst}