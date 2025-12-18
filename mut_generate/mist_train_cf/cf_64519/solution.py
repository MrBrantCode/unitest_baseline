"""
QUESTION:
Create a function called `reformat_string` that takes a string `s` as input and returns a new string with the following conditions: all spaces are removed, all characters are converted to lowercase, and the characters are sorted in alphabetical order.
"""

def reformat_string(s):
    # Remove spaces
    s = s.replace(' ', '') 

    # Convert to lower case
    s = s.lower()

    # Sort string by alphabetical order
    s = ''.join(sorted(s))

    return s