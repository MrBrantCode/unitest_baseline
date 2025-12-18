"""
QUESTION:
Create a function named `trim_string` that takes a string as input and returns the string with leading and trailing whitespace characters removed and extra spaces between words condensed into a single space.
"""

def trim_string(input_string):
    """
    Remove leading and trailing whitespace characters and condense extra spaces between words into a single space.

    Args:
        input_string (str): The input string to be trimmed.

    Returns:
        str: The trimmed string.
    """
    return " ".join(input_string.split())