"""
QUESTION:
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string.  You don't have to worry with strings with less than two characters.
"""

def remove_first_and_last_char(s: str) -> str:
    """
    Removes the first and last characters of the given string.

    Parameters:
    s (str): The original string from which the first and last characters will be removed.

    Returns:
    str: The modified string with the first and last characters removed.
    """
    return s[1:-1]