"""
QUESTION:
Create a function `sanitize_input` that removes single quotes and double quotes from a given string. The function should take a string as input and return the sanitized string.
"""

def sanitize_input(s):
    return s.replace("'", "").replace('"', '')