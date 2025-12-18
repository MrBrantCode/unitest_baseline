"""
QUESTION:
Write a function `get_common_suffix(phrases)` that determines the longest mutual ending sequence present across a given collection of alphanumeric phrases. The function should return the common suffix as a string. The phrases can contain letters, numbers, or special characters, and the algorithm should treat them all the same.
"""

import os

def get_common_suffix(phrases):
    # Reverse the phrases
    reversed_phrases = [phrase[::-1] for phrase in phrases]

    # Get the commom prefix of the reversed phrases
    reversed_common_suffix = os.path.commonprefix(reversed_phrases)

    # return reversed common suffix to get the actual common suffix
    return reversed_common_suffix[::-1]