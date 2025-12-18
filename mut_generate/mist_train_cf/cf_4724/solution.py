"""
QUESTION:
Determine if the given string matches the given regular expression pattern, where the pattern may contain nested groups. The function should capture and return the nested groups as separate matches. The input string must contain at least one uppercase letter, one lowercase letter, and one digit. The pattern should match strings that contain the word "sample" followed by a punctuation mark. The solution should have a time complexity of O(n), where n is the length of the string, and the string can have a maximum length of 10^6.

Write a function `match_pattern(string, pattern)` where `string` is the input string and `pattern` is the regular expression pattern.
"""

import re

def match_pattern(string, pattern):
    """
    This function determines if the given string matches the given regular expression pattern.
    The pattern may contain nested groups. The function captures and returns the nested groups as separate matches.
    
    Args:
        string (str): The input string.
        pattern (str): The regular expression pattern.
    
    Returns:
        list: A list of tuples, where each tuple contains the full match and the captured groups.
    """

    matches = re.finditer(pattern, string)

    result = []
    for match in matches:
        full_match = match.group(0)
        groups = match.groups()
        result.append((full_match, *groups))

    return result