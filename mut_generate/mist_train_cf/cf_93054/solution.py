"""
QUESTION:
Create a regular expression pattern to match alphanumeric characters that are immediately followed by exactly three digits, where the alphanumeric characters can be part of a larger string and the pattern should match the alphanumeric character and the three digits as a whole word. The pattern should not match any alphanumeric characters that are followed by less than or more than three digits.
"""

import re

def entrance(text):
    pattern = r"\b\w{1}\d{3}\b"
    matches = re.findall(pattern, text)
    return matches