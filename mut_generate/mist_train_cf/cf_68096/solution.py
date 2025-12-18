"""
QUESTION:
Write a function `validate_strings(s1, s2)` that checks the validity of two input strings `s1` and `s2` based on the following requirements: 
- Both strings should be longer than 5 characters.
- Neither string should contain only digits.
- `s1` should not be entirely in lowercase and should contain at least one uppercase character.
- `s2` should be entirely in lowercase and digits.
- Both strings should end with digits.
- Both strings should contain at least two special characters.
- The last two digits of both strings should be the same.

The function should return `True` if both strings meet all the requirements and `False` otherwise.
"""

import re

def validate_strings(s1, s2):
    # Check the string length
    if len(s1) <= 5 or len(s2) <= 5:
        return False

    # Check that strings do not contain only digits
    if s1.isdigit() or s2.isdigit():
        return False

    # Check that s1 is not entirely in lower case
    if s1.islower():
        return False

    # check that s1 contains uppercase
    if not any(character.isupper() for character in s1):
        return False

    # check that s2 is entirely in lower case and digits
    if not s2.islower() or not any(character.isdigit() for character in s2):
        return False

    # Check that s1 and s2 end in digits
    if not s1[-1].isdigit() or not s2[-1].isdigit():
        return False

    # Check that they contain at least two special characters
    special_chars_s1 = len(re.findall(r'[^\w]', s1))
    special_chars_s2 = len(re.findall(r'[^\w]', s2))
    if special_chars_s1 < 2 or special_chars_s2 < 2:
        return False

    # Check that both strings end in the same 2 digits
    if s1[-2:] != s2[-2:]:
        return False

    return True