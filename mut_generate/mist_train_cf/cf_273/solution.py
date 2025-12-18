"""
QUESTION:
Write a function `modify_string` that takes a string as input. The function should remove all whitespace, punctuation, and digits from the string, convert all characters to uppercase, and then sort the resulting string in descending order. The function should return the modified string.
"""

import string

def modify_string(s):
    s = ''.join(c for c in s if c not in string.whitespace + string.punctuation and not c.isdigit())
    return ''.join(sorted(s.upper(), reverse=True))