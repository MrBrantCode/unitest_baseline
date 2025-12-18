"""
QUESTION:
Create a function `sanitize_string(s)` that takes a string `s` as input and returns a new string with all non-alphanumeric characters (except whitespace) removed. The function should iterate over each character in the string and include only alphanumeric characters and whitespace in the output.
"""

def sanitize_string(s):
    return ''.join(c for c in s if c.isalnum() or c.isspace())