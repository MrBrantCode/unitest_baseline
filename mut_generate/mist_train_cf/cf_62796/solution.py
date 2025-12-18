"""
QUESTION:
Create a regex pattern that matches strings with the following rules: 
- Exactly one dash
- One or more digits immediately after the dash
- One or more letters immediately after the digits.
"""

def entrance(s):
    """
    Returns True if the string matches the pattern and False otherwise.
    The pattern requires exactly one dash, followed by one or more digits, 
    and then one or more letters.
    """
    import re
    # Match exactly one dash, followed by one or more digits, and then one or more letters
    pattern = r'-\d+[a-zA-Z]+'
    return bool(re.fullmatch(pattern, s))