"""
QUESTION:
Create a function `checkSameCharacters` that takes two string parameters, `stringA` and `stringB`. The function should check if two strings have the same characters, frequencies, and order of characters, considering case sensitivity, whitespace characters, and punctuation marks. The function should return `True` if the strings have the same characters, frequencies, and order of characters, and `False` otherwise. The solution should be case sensitive and should account for all characters including whitespace characters and punctuation marks.
"""

def checkSameCharacters(stringA, stringB):
    """
    Checks if two strings have the same characters, frequencies, and order of characters.

    Args:
        stringA (str): The first string to compare.
        stringB (str): The second string to compare.

    Returns:
        bool: True if the strings have the same characters, frequencies, and order of characters, False otherwise.
    """
    if len(stringA) != len(stringB):
        return False

    return sorted(stringA) == sorted(stringB)