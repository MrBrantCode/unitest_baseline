"""
QUESTION:
Create a function named `modify_strings` that takes a list of strings as input. The function should return a new list where each string has its first character converted to uppercase and leading/trailing whitespace removed. The time complexity of the function should be O(n), where n is the total number of characters in all the strings combined.
"""

def modify_strings(strings):
    """
    Modify a list of strings by converting the first character to uppercase and removing leading/trailing whitespace.

    Args:
        strings (list): A list of strings to be modified.

    Returns:
        list: A new list of modified strings.
    """
    modified_strings = [string.strip().capitalize() for string in strings]
    return modified_strings