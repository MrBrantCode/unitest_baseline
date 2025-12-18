"""
QUESTION:
Create a function `replaceNonAlphaNumCharacters` that takes a string as input and replaces all non-alphanumeric characters with the '#' symbol. The function should return the resulting string.
"""

def replaceNonAlphaNumCharacters(s):
    """
    Replaces all non-alphanumeric characters in the input string with the '#' symbol.

    Args:
        s (str): The input string.

    Returns:
        str: The resulting string with non-alphanumeric characters replaced.
    """
    return ''.join(c if c.isalnum() else '#' for c in s)