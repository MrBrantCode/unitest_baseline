"""
QUESTION:
Write a function named `find_red_apple` that returns True if the word "apple" is preceded by the word "red" and followed by a comma in a given sentence. The function should return False otherwise.
"""

import re

def find_red_apple(sentence):
    """
    This function checks if the word 'apple' is preceded by 'red' and followed by a comma in a given sentence.

    Args:
        sentence (str): The input sentence to be checked.

    Returns:
        bool: True if 'apple' is preceded by 'red' and followed by a comma, False otherwise.
    """
    pattern = r'\bred apple,'
    return bool(re.search(pattern, sentence))