"""
QUESTION:
Create a regular expression that matches words starting with 'a' and ending with 'e', with a minimum length of 4 characters and a maximum length of 8 characters. The function should take a string as input and return all matching words.
"""

import re

def entance(text):
    """
    This function takes a string as input and returns all words that start with 'a' and end with 'e', 
    with a minimum length of 4 characters and a maximum length of 8 characters.

    Args:
        text (str): The input string.

    Returns:
        list: A list of words that match the specified pattern.
    """

    # regular expression pattern to match the words
    pattern = r"\ba[a-z]{2,6}e\b"

    # find all matching words
    matches = re.findall(pattern, text)

    return matches