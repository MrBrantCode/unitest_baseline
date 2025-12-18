"""
QUESTION:
Write a function named `find_phrase_variation` that uses regular expression to identify any variations of the phrase "an apple a day keeps the doctor away" in a given string, including cases where other words are inserted between the original words. The function should return a boolean value indicating whether a match is found.
"""

import re

def find_phrase_variation(s):
    """
    Uses regular expression to identify any variations of the phrase 
    "an apple a day keeps the doctor away" in a given string.

    Args:
        s (str): The input string to search for the phrase.

    Returns:
        bool: True if a match is found, False otherwise.
    """
    pattern = re.compile(r"(an)(.*)(apple)(.*)(a)(.*)(day)(.*)(keeps)(.*)(the)(.*)(doctor)(.*)(away)")
    return bool(pattern.search(s))