"""
QUESTION:
Write a function `clean_and_reverse` that takes a string as input, converts it to lowercase, removes any non-alphanumeric characters (replacing them with spaces), and reverses the order of the words. The input string may contain alphanumeric characters and punctuation.
"""

import re

def clean_and_reverse(s):
    """
    Converts a string to lowercase, removes non-alphanumeric characters, 
    and reverses the order of the words.

    Parameters:
    s (str): The input string.

    Returns:
    str: The cleaned and reversed string.
    """
    s = s.lower()  # change to lowercase
    s = re.sub(r'\W+', ' ', s)  # remove special characters
    return ' '.join(s.split()[::-1])  # reverse order of words