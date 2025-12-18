"""
QUESTION:
Create a function called `transform_to_uppercase` that takes an array of strings as input and returns a new array where all strings are fully capitalized according to the ASCII standard.
"""

def transform_to_uppercase(strings):
    """
    This function transforms all strings in a given array to fully capitalized 
    according to the ASCII standard.

    Args:
        strings (list): A list of strings to be transformed.

    Returns:
        list: A new list with all strings fully capitalized.
    """
    return [s.upper() for s in strings]