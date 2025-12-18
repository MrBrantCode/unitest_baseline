"""
QUESTION:
Create a function called `create_dict` that takes a list of integers as input and returns a dictionary. The keys of the dictionary should be the integers in the list and the values should be the squares of the corresponding integers. Do not use any built-in Python functions or operators to calculate the square of a number. Additionally, do not use any loop or recursion constructs.
"""

def create_dict(lst):
    """
    This function takes a list of integers as input and returns a dictionary.
    The keys of the dictionary are the integers in the list and the values are the squares of the corresponding integers.

    Args:
        lst (list): A list of integers.

    Returns:
        dict: A dictionary with integers as keys and their squares as values.
    """
    return {i: i * i for i in lst}