"""
QUESTION:
Write a function named `explode_string` that takes a string and a delimiter as input, splits the string into a list of elements based on the delimiter, and returns the list with any whitespace characters removed from the beginning and end of each element.
"""

def explode_string(input_string, delimiter):
    """
    Explode a string into a list of elements based on a delimiter and remove whitespace characters.

    Args:
        input_string (str): The input string to be exploded.
        delimiter (str): The delimiter used to split the string.

    Returns:
        list: A list of elements with whitespace characters removed from the beginning and end of each element.
    """
    return [element.strip() for element in input_string.split(delimiter)]