"""
QUESTION:
Write a function `check_hello_world` that checks if a given string contains the word 'hello' at least 5 times and the word 'world' at least once, and does not contain any punctuation marks. The function should return True if the string meets the conditions, False otherwise. The check for 'hello' and 'world' should be case-insensitive.
"""

import re

def check_hello_world(s):
    """
    Checks if a given string contains the word 'hello' at least 5 times and the word 'world' at least once,
    and does not contain any punctuation marks. The check for 'hello' and 'world' is case-insensitive.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string meets the conditions, False otherwise.
    """
    # Remove punctuation marks from the string
    s = re.sub(r'[^\w\s]', '', s)
    
    # Count the number of occurrences of 'hello' and check if 'world' occurs at least once
    return s.lower().count('hello') >= 5 and 'world' in s.lower()