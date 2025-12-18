"""
QUESTION:
Write a function named `find_name` that takes a string `s` as input and returns a list of full names (first name and surname) found in the string. The full name should be in the format of a first name and a surname separated by a space, with each starting with a capital letter followed by lowercase letters.
"""

import re

def find_name(s):
    pattern = r"[A-Z][a-z]*\s[A-Z][a-z]*"
    matches = re.findall(pattern, s)
    return matches