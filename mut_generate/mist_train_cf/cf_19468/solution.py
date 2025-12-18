"""
QUESTION:
Write a function `check_pattern_match` that determines if a given string matches a regular expression pattern containing nested groups. The string must contain at least one uppercase letter, one lowercase letter, and one digit. The pattern should match strings that contain the word "sample" followed by a punctuation mark. Return a list of captured groups if the string matches the pattern, otherwise return `None`.

The input parameters for the function are:
- `s`: the input string
- `pattern`: the regular expression pattern, default value is `((.*) sample (.*)[^\w\s])`
"""

import re

def check_pattern_match(s, pattern=r"((.*) sample (.*)[^\w\s])"):
    """
    This function checks if a given string matches a regular expression pattern containing nested groups.
    
    Parameters:
    s (str): The input string
    pattern (str): The regular expression pattern (default is r"((.*) sample (.*)[^\w\s])")
    
    Returns:
    list: A list of captured groups if the string matches the pattern, otherwise None
    """
    
    # Check if the string contains at least one uppercase letter, one lowercase letter, and one digit
    if not (any(c.isupper() for c in s) and any(c.islower() for c in s) and any(c.isdigit() for c in s)):
        return None
    
    # Use re.match to match the pattern at the beginning of the string
    match = re.match(pattern, s)
    
    # If the string matches the pattern, return the captured groups
    if match:
        return list(match.groups())
    else:
        return None