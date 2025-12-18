"""
QUESTION:
Write a function `matches_pattern(pattern, string)` that checks if the given `string` matches the given `pattern`. The `pattern` can contain any combination of uppercase letters and special characters '.' or '*'. The `string` can also contain any combination of uppercase letters and special characters. The function should follow these rules: 
- Uppercase letters in the `pattern` should match the same uppercase letters in the `string`.
- '.' in the `pattern` can match any single uppercase letter in the `string`.
- '*' in the `pattern` can match any sequence of uppercase letters in the `string`.
- '*' can only be used once in the `pattern`.
- '*' cannot be the first character in the `pattern`.
- '.' cannot be the last character in the `pattern`.
- The `pattern` cannot contain any lowercase letters.
The function should return `True` if the `string` matches the `pattern`, and `False` otherwise.
"""

def matches_pattern(pattern, string):
    # Check if pattern or string is empty
    if not pattern or not string:
        return False

    # Check if pattern contains lowercase letters
    if any(char.islower() for char in pattern):
        return False

    # Check if '*' is used more than once in pattern
    if pattern.count('*') > 1:
        return False

    # Check if '*' is the first character in pattern
    if pattern.startswith('*'):
        return False

    # Check if '.' is the last character in pattern
    if pattern.endswith('.'):
        return False

    # Replace '.' and '*' with regular expressions
    pattern = pattern.replace('.', '[A-Z]')
    pattern = pattern.replace('*', '[A-Z]*')

    # Use regular expression to match pattern with string
    import re
    if re.fullmatch(pattern, string):
        return True
    else:
        return False