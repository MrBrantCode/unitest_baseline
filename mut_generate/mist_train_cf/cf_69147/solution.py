"""
QUESTION:
Create a regex pattern named 'pattern' that identifies hexadecimal values that exclusively begin with the character 'B'. The pattern should match word boundaries and be case-insensitive to hexadecimal digits.
"""

import re

def entrance(s):
    pattern = r'\bB[0-9A-Fa-f]+\b'
    return re.findall(pattern, s)