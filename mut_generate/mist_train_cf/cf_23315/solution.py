"""
QUESTION:
Create a function `extract_words_starting_with_letter` that takes a string `input_str` and a letter `letter` as input. The function should return all words from `input_str` that start with `letter`, ignoring case.
"""

import re

def extract_words_starting_with_letter(input_str, letter):
    """
    Extracts words from input_str that start with the given letter, ignoring case.

    Args:
    input_str (str): The input string to extract words from.
    letter (str): The letter to look for at the start of words.

    Returns:
    list: A list of words that start with the given letter.
    """
    return re.findall(r'\b' + re.escape(letter) + r'\w*\b', input_str, re.IGNORECASE)