"""
QUESTION:
Transform each string in the given list to uppercase and sort the list in descending order based on the length of the strings. Write a function named `sort_uppercase_strings` that takes a list of strings as input and returns the sorted list.
"""

def sort_uppercase_strings(strings):
    """
    Transform each string in the given list to uppercase and sort the list in descending order based on the length of the strings.

    Args:
        strings (list): A list of strings.

    Returns:
        list: The sorted list of uppercase strings.
    """
    return sorted([s.upper() for s in strings], key=len, reverse=True)