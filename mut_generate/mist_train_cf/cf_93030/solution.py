"""
QUESTION:
Create a function `sort_strings_by_length` that takes a list of strings as input and returns the list sorted in descending order based on the length of the strings.
"""

def sort_strings_by_length(strings):
    """
    Sorts a list of strings in descending order based on their length.

    Args:
        strings (list): A list of strings.

    Returns:
        list: The sorted list of strings.
    """
    return sorted(strings, key=lambda x: len(x), reverse=True)