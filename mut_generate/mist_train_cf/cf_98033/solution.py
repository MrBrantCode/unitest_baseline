"""
QUESTION:
Write a Python function called `add_to_numbers` that takes a string `sentence` as input, adds 100 to all numbers found in the sentence using regular expressions, and returns the resulting string.
"""

import re
def add_to_numbers(sentence):
    """
    Adds 100 to all numbers found in the input sentence using regular expressions.

    Args:
    sentence (str): The input sentence containing numbers.

    Returns:
    str: The resulting string with 100 added to all numbers.
    """
    pattern = r'\d+'
    replacement = lambda match: str(int(match.group()) + 100)
    result = re.sub(pattern, replacement, sentence)
    return result