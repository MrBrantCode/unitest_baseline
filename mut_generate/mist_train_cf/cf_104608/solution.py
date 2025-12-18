"""
QUESTION:
Write a function `reverse_sorted_last_char` that takes a list of strings as input, sorts the list in alphabetical order based on the last character of each string, and returns the reverse of the sorted list. The list may contain any number of strings. The function should return a list of strings.
"""

def reverse_sorted_last_char(strings):
    """
    Sorts a list of strings in alphabetical order based on the last character of each string and returns the reverse of the sorted list.

    Args:
    strings (list): A list of strings.

    Returns:
    list: The reverse of the sorted list of strings.
    """
    return sorted(strings, key=lambda x: x[-1])[::-1]