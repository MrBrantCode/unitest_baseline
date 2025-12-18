"""
QUESTION:
Create a function `ends_with_py` that determines whether a given string ends with "py" (case insensitive). The function should return True if the string ends with "py" and False otherwise.
"""

import re

def ends_with_py(s):
    pattern = r"[pP][yY]$"
    return bool(re.search(pattern, s))