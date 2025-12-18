"""
QUESTION:
Write a function called `filter_alphanumeric` that takes a string `s` as input and returns a new string containing only the alphanumeric characters (a-z, A-Z, and 0-9) from `s`.
"""

def filter_alphanumeric(s):
    return ''.join(c for c in s if c.isalnum())