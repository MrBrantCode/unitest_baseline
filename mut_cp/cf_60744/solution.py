"""
ORIGINAL QUESTION:
Determine if a given string matches a regular expression pattern and identify all unique matches within the string. Implement a function `find_unique_matches` that takes two parameters: `input_string` and `pattern`. The function should return the unique matches and the number of unique matches.
"""

import re

def find_unique_matches(input_string, pattern):
    """
    Determine if a given string matches a regular expression pattern and identify all unique matches within the string.

    Args:
        input_string (str): The input string to search for matches.
        pattern (str): The regular expression pattern to match.

    Returns:
        tuple: A set of unique matches and the number of unique matches.
    """
    # Find matches with re.findall()
    matches = re.findall(pattern, input_string)

    # Convert matches to set to eliminate duplicates
    unique_matches = set(matches)

    return unique_matches, len(unique_matches)