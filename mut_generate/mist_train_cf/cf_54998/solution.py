"""
QUESTION:
Write a function called `is_valid()` that takes a string `s` as input and returns `True` if the string is a valid string and `False` otherwise.
"""

def is_valid(s):
    """
    Checks if the input string is a valid string.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is valid, False otherwise.
    """

    # Check if the input is a string
    if not isinstance(s, str):
        return False

    # A string is considered valid if it's not empty
    return len(s) > 0