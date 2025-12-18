"""
QUESTION:
Write a function `validate_strings(s1, s2)` that takes two strings `s1` and `s2` as input and returns `True` if they pass the following validation conditions, and `False` otherwise:

- Both strings should be at least 12 characters long.
- `s1` should contain at least three special characters.
- `s2` should contain at least three uppercase letters.
- Both strings should not contain any consecutive repeating characters.
- The combined length of both strings should not exceed 25 characters.
- `s1` should contain at least two lowercase letters.
- `s2` should contain at least two numeric digits.
- Both strings should contain at least two whitespace characters.
- The first character of `s1` should be a letter (uppercase or lowercase) and not a special character.
- The last character of `s2` should be a letter (uppercase or lowercase) and not a special character or a numeric digit.
"""

import re

def validate_strings(s1, s2):
    # Condition 1: Both s1 and s2 should be at least 12 characters long.
    if len(s1) < 12 or len(s2) < 12:
        return False

    # Condition 2: s1 should contain at least three special characters.
    if len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', s1)) < 3:
        return False

    # Condition 3: s2 should contain at least three uppercase letters.
    if len(re.findall(r'[A-Z]', s2)) < 3:
        return False

    # Condition 4: Both s1 and s2 should not contain any consecutive repeating characters.
    if re.search(r'(.)\1', s1) or re.search(r'(.)\1', s2):
        return False

    # Condition 5: The combined length of s1 and s2 should not exceed 25 characters.
    if len(s1) + len(s2) > 25:
        return False

    # Condition 6: s1 should contain at least two lowercase letters.
    if len(re.findall(r'[a-z]', s1)) < 2:
        return False

    # Condition 7: s2 should contain at least two numeric digits.
    if len(re.findall(r'\d', s2)) < 2:
        return False

    # Condition 8: Both s1 and s2 should contain at least two whitespace characters.
    if len(re.findall(r'\s', s1)) < 2 or len(re.findall(r'\s', s2)) < 2:
        return False

    # Condition 9: The first character of s1 should be a letter and it should not be a special character.
    if not re.match(r'^[a-zA-Z]', s1):
        return False

    # Condition 10: The last character of s2 should be a letter and it should not be a special character or a numeric digit.
    if not re.match(r'^[a-zA-Z]$', s2[-1]):
        return False

    # All conditions pass
    return True