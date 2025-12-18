"""
QUESTION:
Write a function named `match_pattern` that uses regular expressions to identify if the words "start", "here", and "end" appear in a given string in that order, with any characters in between them. The function should return the matched text if found, and "No match" otherwise.
"""

import re

def match_pattern(s):
    """
    This function uses regular expressions to identify if the words "start", "here", and "end" 
    appear in a given string in that order, with any characters in between them.

    Args:
        s (str): The input string to search for the pattern.

    Returns:
        str: The matched text if found, "No match" otherwise.
    """
    pattern = r'\bstart\b.*\bhere\b.*\bend\b'
    match = re.search(pattern, s)
    return match.group(0) if match else "No match"