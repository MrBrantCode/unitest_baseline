"""
QUESTION:
Write a function named `validate_word` that takes a string as input and returns True if the string matches the pattern "XX-XXX-XXX" where the first two characters are uppercase letters, the next three characters are lowercase letters, and the last three characters can be a mix of uppercase and lowercase letters, with no digits or special characters. The function should return False for any other input string.
"""

import re

def validate_word(word):
    pattern = "^[A-Z]{2}-[a-z]{3}-[A-Za-z]{3}$"
    match = re.match(pattern, word)
    if match:
        return True
    else:
        return False