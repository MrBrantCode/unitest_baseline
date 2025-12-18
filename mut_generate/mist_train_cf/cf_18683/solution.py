"""
QUESTION:
Create a function named 'sort_string' that takes a string of at least 5 comma-separated words as input, splits the string into a list using comma as the delimiter, and returns the list sorted in alphabetical order.
"""

def sort_string(input_str):
    """
    This function takes a string of comma-separated words, splits it into a list, 
    and returns the list sorted in alphabetical order.

    Args:
        input_str (str): A string of comma-separated words.

    Returns:
        list: A list of words sorted in alphabetical order.
    """
    return sorted(input_str.split(","))