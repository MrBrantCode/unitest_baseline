"""
QUESTION:
Sort an array of strings in descending order of length. If two strings have the same length, sort them alphabetically. The array can contain duplicate strings. Implement a function, for example, `sort_strings`, to achieve this.
"""

def sort_strings(strings):
    """
    Sorts an array of strings in descending order of length. 
    If two strings have the same length, they are sorted alphabetically.

    Args:
    strings (list): A list of strings.

    Returns:
    list: A list of strings sorted in descending order of length and alphabetically.
    """
    return sorted(strings, key=lambda x: (-len(x), x))