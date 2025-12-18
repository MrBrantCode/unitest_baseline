"""
QUESTION:
Write a function `matches_pattern(pattern, string)` that checks if a given string matches a specified pattern. The pattern can contain any combination of uppercase letters and special characters '.' or '*'. The string can also contain any combination of uppercase letters and special characters. The function should return True if the string matches the pattern, and False otherwise.

The matching rules are as follows: 
- Uppercase letters in the pattern should match the same uppercase letters in the string.
- The '.' special character in the pattern can match any single uppercase letter in the string.
- The '*' special character in the pattern can match any sequence of uppercase letters in the string.

The function has the following restrictions:
- The '*' special character can only be used once in the pattern.
- The '*' special character cannot be the first character in the pattern.
- The '.' special character cannot be the last character in the pattern.
- The pattern cannot contain any lowercase letters.
"""

def matches_pattern(pattern, string):
    if not pattern or not string:
        return False

    if any(char.islower() for char in pattern):
        return False

    if pattern.count('*') > 1:
        return False

    if pattern.startswith('*'):
        return False

    if pattern.endswith('.'):
        return False

    pattern = pattern.replace('.', '[A-Z]')
    pattern = pattern.replace('*', '[A-Z]*')

    import re
    if re.fullmatch(pattern, string):
        return True
    else:
        return False