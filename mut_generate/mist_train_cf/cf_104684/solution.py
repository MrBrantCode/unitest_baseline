"""
QUESTION:
Write a function `calculate_name_length` that takes a string of a first name and a string of a last name as input, concatenates them with a space in between, calculates the length of the full name, and returns the length of the full name multiplied by 2.
"""

def calculate_name_length(first_name, last_name):
    """
    Calculate the length of the full name and return the length multiplied by 2.

    Args:
    first_name (str): The first name.
    last_name (str): The last name.

    Returns:
    int: The length of the full name multiplied by 2.
    """
    full_name = first_name + " " + last_name
    return len(full_name) * 2