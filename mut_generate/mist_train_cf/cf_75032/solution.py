"""
QUESTION:
Write a function `get_positions(s, ch)` that takes a string `s` and a character `ch` as input, and returns a list of positions of all occurrences of `ch` in `s`. The function should be case-insensitive and treat all characters equally, including numbers, special characters, and spaces.
"""

def get_positions(s, ch):
    """
    Returns a list of positions of all occurrences of `ch` in `s`.
    The function is case-insensitive and treats all characters equally.

    Parameters:
    s (str): The input string.
    ch (str): The character to search for.

    Returns:
    list: A list of positions of all occurrences of `ch` in `s`.
    """
    s = s.lower()
    ch = ch.lower()
    return [i for i, ltr in enumerate(s) if ltr == ch]