"""
QUESTION:
Write a function called `remove_substrings` that takes a string `s` and a list of substrings as input, and returns the string with all occurrences of the given substrings removed. The function should be able to remove multiple substrings from the input string.
"""

def remove_substrings(s, substrings):
    """
    Removes all occurrences of the given substrings from the input string.

    Args:
        s (str): The input string.
        substrings (list): A list of substrings to be removed.

    Returns:
        str: The string with all occurrences of the given substrings removed.
    """
    for substring in substrings:
        s = s.replace(substring, "")
    return s