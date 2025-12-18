"""
QUESTION:
Write a function called `count_substring_frequency` that takes a string `text` and a substring as input and returns the frequency of the substring within the string.
"""

def count_substring_frequency(text, substring):
    """
    This function calculates the frequency of a given substring within a string.

    Args:
        text (str): The main string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The frequency of the substring within the string.
    """
    return text.count(substring)