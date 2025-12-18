"""
QUESTION:
Create a Python function named `square_list` that takes a list of integers as input and returns a new list with each integer squared. The function should be part of a Python package that can be easily installed and imported into other Python projects. Implement the package structure, including the necessary metadata for distribution, and the `square_list` function within the module.
"""

def square_list(input_list):
    """
    Squares each integer in the input list and returns a new list.
    
    Args:
    input_list (list): A list of integers.
    
    Returns:
    list: A new list with each integer squared.
    """
    return [x**2 for x in input_list]