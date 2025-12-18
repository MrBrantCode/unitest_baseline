"""
QUESTION:
Write a function `validate_string(s)` that checks if a given string `s` meets the following conditions:
- The length of the string is between 5 and 15 characters (inclusive).
- The string is alphanumeric (contains only letters and numbers).
- The string contains at least one uppercase letter.
- The string contains a repeated sequence of characters (a substring that appears more than once).

If the string meets all conditions, the function should return `True`. Otherwise, it should return a string describing the reason why the string was not validated.
"""

import re

def validate_string(s):
    min_length = 5
    max_length = 15
    if min_length <= len(s) <= max_length:
        if s.isalnum():            
            if any(char.isupper() for char in s):
                if re.search(r'(\w).*\1', s):                  # Uses regex to find any repeated substrings (word characters)
                    return True
                else:
                    return 'No repeated sequence found.'
            else:
                return 'No uppercase letter found.'
        else:
            return 'String is not alphanumeric.'
    else:
        return 'Length error: String is too short or too long.'