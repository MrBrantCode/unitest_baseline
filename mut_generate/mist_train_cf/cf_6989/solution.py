"""
QUESTION:
Create a function `count_unique_characters` that takes a string as input and returns a dictionary containing the count of each unique character found, excluding any whitespace characters. The function should be optimized for efficiency.
"""

def count_unique_characters(s):
    """
    Returns a dictionary containing the count of each unique character found in the input string, excluding any whitespace characters.

    Args:
        s (str): The input string.

    Returns:
        dict: A dictionary containing the count of each unique character.
    """
    unique_chars = {}
    for char in s:
        if not char.isspace():
            unique_chars[char] = unique_chars.get(char, 0) + 1
    return unique_chars