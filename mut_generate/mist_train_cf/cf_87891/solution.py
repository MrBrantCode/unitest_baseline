"""
QUESTION:
Write a function `check_pattern(pattern, string)` that checks if a given string matches a specified pattern. The pattern can contain uppercase letters, special characters '.', '*', and '+', and numerical digits, while the string can contain any combination of uppercase letters, special characters, and numerical digits. The function should return True if the string matches the pattern, and False otherwise. 

The pattern matching rules are as follows:
- Uppercase letters in the pattern match the same uppercase letters in the string.
- '.' matches any single uppercase letter, special character, or numerical digit in the string.
- '*' matches any sequence of uppercase letters, special characters, or numerical digits in the string.
- '+' matches one or more occurrences of uppercase letters, special characters, or numerical digits in the string.

Additional restrictions on the pattern include:
- '*' can only be used once in the pattern.
- '*' cannot be the first character in the pattern.
- '.' cannot be the last character in the pattern.
- The pattern cannot contain lowercase letters.
- The pattern cannot start with a numerical digit.
"""

import re

def check_pattern(pattern, string):
    if pattern.count('*') > 1 or pattern.startswith('*') or pattern.endswith('.') or re.search('[a-z]', pattern) or pattern[0].isdigit():
        return False

    pattern = pattern.replace('.', '[A-Za-z0-9]')
    pattern = pattern.replace('*', '[A-Za-z0-9]*')
    pattern = pattern.replace('+', '[A-Za-z0-9]+')

    return re.fullmatch(pattern, string) is not None