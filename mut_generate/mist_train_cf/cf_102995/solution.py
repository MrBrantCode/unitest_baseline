"""
QUESTION:
Write a function `clean_string` that takes a string as input and returns the string with all punctuation and numbers removed, and all uppercase letters converted to lowercase.
"""

def clean_string(s):
    s = ''.join(e for e in s if e.isalpha() or e.isspace())
    return s.lower()