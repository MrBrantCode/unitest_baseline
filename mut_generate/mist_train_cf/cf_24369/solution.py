"""
QUESTION:
Write a function that extracts substrings that match the pattern "AAA_BBB_CCC" where 'A', 'B', and 'C' are placeholders for any alphabetic character and the substring should contain exactly three groups of three alphabetic characters separated by underscores.
"""

import re

def entrance(s):
    pattern = r'^([A-Za-z]{3})_([A-Za-z]{3})_([A-Za-z]{3})$'
    match = re.match(pattern, s)
    return match.groups() if match else None