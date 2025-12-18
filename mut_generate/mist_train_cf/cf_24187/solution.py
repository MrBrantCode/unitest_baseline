"""
QUESTION:
Write a function called `make_dict_key_iterable` that makes dictionary keys iterable in Python. The function should take a dictionary as input and return an iterable object of the keys in the dictionary.
"""

def make_dict_key_iterable(input_dict):
    """
    Makes dictionary keys iterable in Python.

    Args:
        input_dict (dict): The input dictionary.

    Returns:
        iterable: An iterable object of the keys in the dictionary.
    """
    return input_dict.keys()