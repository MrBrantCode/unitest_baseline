"""
QUESTION:
Write a function named `check_pattern` that takes two parameters: `pattern` and `string`. The `pattern` can contain any combination of uppercase letters, special characters '.', '*', and '+', and numerical digits, with the following restrictions:
- The '*' special character can only be used once in the pattern.
- The '*' special character cannot be the first character in the pattern.
- The '.' special character cannot be the last character in the pattern.
- The pattern cannot contain any lowercase letters.
- The pattern cannot start with a numerical digit.

The function should return True if the `string` matches the `pattern` according to the following rules:
- Uppercase letters in the pattern should match the same uppercase letters in the string.
- The '.' special character in the pattern can match any single uppercase letter, special character, or numerical digit in the string.
- The '*' special character in the pattern can match any sequence of uppercase letters, special characters, or numerical digits in the string.
- The '+' special character in the pattern can match one or more occurrences of uppercase letters, special characters, or numerical digits in the string.

The function should return False otherwise.
"""

import re

def check_pattern(pattern, string):
    # Additional rules
    if pattern.count('*') > 1 or pattern.startswith('*') or pattern.endswith('.') or re.search('[a-z]', pattern) or pattern[0].isdigit():
        return False

    # Replace special characters with regex patterns
    pattern = pattern.replace('.', '[A-Z0-9]')
    pattern = pattern.replace('*', '[A-Z0-9]*')
    pattern = pattern.replace('+', '[A-Z0-9]+')

    # Check if the string matches the pattern
    return re.fullmatch(pattern, string) is not None