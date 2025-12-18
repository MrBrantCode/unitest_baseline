"""
QUESTION:
Create a function called `find_pattern` that takes a string as input. The function should find all occurrences of a pattern in the string where 'x' is immediately followed by at least three 'w's, disregarding case sensitivity and ignoring special characters and numerical values. The function should return a list of the starting positions of all matches, including nested and recursive patterns, or a message indicating that the pattern was not found.
"""

import re

def find_pattern(string):
    # Convert the string to lowercase to handle case insensitivity
    string = string.lower()
    # Search for the pattern ( x followed by at least 3 w without considering case)
    matches = re.finditer('xw{3,}', string)
    match_positions = [match.start() for match in matches]
    if not match_positions:
        return "The pattern does not exist within the string"
    return match_positions