"""
QUESTION:
Create a regular expression that can extract the username from the input string, where the username is preceded by a percentage sign and optionally followed by a colon, whitespace, and "tp". The function should return a list of usernames found in the input string. The input string may contain one or more instances of the username, with possible variations in whitespace. The function should use Python's `re` module and return a list of matches using `re.findall()`.
"""

import re

def extract_username(text_input):
    regex = r"%\s*(\w+):?\s*tp"
    return re.findall(regex, text_input)