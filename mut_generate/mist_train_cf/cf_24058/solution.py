"""
QUESTION:
Write a regular expression pattern using Python that matches a string containing the words "start", "end", and "here" in any order. The function name is not specified.
"""

import re

def entrance(s):
    """
    This function checks if a given string contains the words 'start', 'end', and 'here' in any order.

    Parameters:
    s (str): The input string to be checked.

    Returns:
    bool: True if the string contains the words 'start', 'end', and 'here' in any order, False otherwise.
    """
    pattern = re.compile(r'.*(start|end|here).*', re.IGNORECASE)
    return bool(pattern.match(s)) and bool(re.search('start', s, re.IGNORECASE)) and bool(re.search('end', s, re.IGNORECASE)) and bool(re.search('here', s, re.IGNORECASE))