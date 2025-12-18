"""
QUESTION:
Create a function called `all_prefixes` that takes a string as input and returns a list of all prefixes from shortest to longest, excluding single character prefixes. The function should be able to handle strings of any length.
"""

def all_prefixes(s):
    """
    Returns a list of all prefixes from shortest to longest, excluding single character prefixes.

    Args:
    s (str): The input string.

    Returns:
    list: A list of prefixes.
    """
    return [s[:i] for i in range(2, len(s) + 1)]