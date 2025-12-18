"""
QUESTION:
Write a function `find_zyy` that takes a string `s` as input and returns the index of the first occurrence of 'z' followed by two or more 'y's in a case-insensitive manner. If no match is found, return -1.
"""

import re

def find_zyy(s):
    match = re.search(r'z[yY]{2,}', s, re.IGNORECASE)
    if match:
        return match.start()
    else:
        return -1