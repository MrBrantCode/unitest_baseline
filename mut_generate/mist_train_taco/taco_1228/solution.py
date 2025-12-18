"""
QUESTION:
Given a string, remove any characters that are unique from the string.

Example: 

input: "abccdefee"

output: "cceee"
"""

from collections import Counter

def remove_unique_characters(input_string: str) -> str:
    """
    Removes any characters that are unique from the input string.

    Parameters:
    input_string (str): The input string from which unique characters need to be removed.

    Returns:
    str: A new string containing only the characters that are not unique in the input string.
    """
    char_count = Counter(input_string)
    return ''.join((c for c in input_string if char_count[c] > 1))