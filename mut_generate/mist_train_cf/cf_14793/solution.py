"""
QUESTION:
Separate a given alphanumeric string into left and right parts. The left part should contain only digits, and the right part should contain only lowercase letters. If the string contains no lowercase letters, the right part should be an empty string.
"""

def separate_string(s):
    left_part = ''
    right_part = ''
    for char in s:
        if char.isdigit():
            left_part += char
        elif char.islower():
            right_part += char
    return left_part, right_part