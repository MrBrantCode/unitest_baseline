"""
QUESTION:
Construct a function named `construct_dict` that takes a list of numbers as input and returns a dictionary. The dictionary keys should be the elements of the input list, and the corresponding values should be lists containing the square and cube of each key. The function should handle both integers and floating point numbers.
"""

def construct_dict(lst):
    return {x: [x**2, x**3] for x in lst}