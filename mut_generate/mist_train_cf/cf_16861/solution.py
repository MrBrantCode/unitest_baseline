"""
QUESTION:
Write a function `retrieve_third_char` that takes a string `s` as input. If `s` has more than 10 characters and consists only of lowercase alphabetic characters, return the third character of `s` (0-indexed).
"""

def retrieve_third_char(s):
    """
    Retrieves the third character of a string if it has more than 10 characters and consists only of lowercase alphabetic characters.

    Args:
        s (str): The input string.

    Returns:
        str: The third character of the string if conditions are met, otherwise None.
    """
    if len(s) > 10 and s.isalpha() and s.islower():
        return s[2]
    else:
        return None