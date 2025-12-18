"""
QUESTION:
Construct a regular expression pattern to match the string "hello people" with the following conditions:

* The string can be in any case (e.g., "Hello People", "HELLO PEOPLE", "hELLO pEoPlE", etc.)
* There can be one or more spaces between the words "hello" and "people"
* The pattern should match the entire string, not just a part of it.

The function should return a match if the input string meets these conditions, and no match otherwise.
"""

import re

def entrance(input_string):
    """
    Matches the input string with "hello people" (case-insensitive) 
    with one or more spaces between the words.

    Args:
    input_string (str): The input string to be matched.

    Returns:
    bool: True if the input string matches the pattern, False otherwise.
    """
    pattern = r"^[hH][eE][lL]{2}[oO]\s+[pP][eE][oO][pP][lL][eE]$"
    match = re.match(pattern, input_string)
    return bool(match)