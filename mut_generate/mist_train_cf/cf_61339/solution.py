"""
QUESTION:
Design a function `to_camel_case` that converts a given textual string into camelCase representation. The function should be case-insensitive, handle and remove non-alphabetical characters, treat successive non-alphabetical characters as a single word boundary, and efficiently handle edge cases such as empty strings and strings with only spaces or special characters.
"""

def to_camel_case(s):
    s = ''.join(c if c.isalpha() else ' ' for c in s)
    return ''.join(word.title() for word in s.split())