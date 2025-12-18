"""
QUESTION:
Create a function `check_string(s)` that takes a string `s` as input and returns `True` if the string consists only of alphabet characters and ends with "py", and `False` otherwise. The function should exclude strings containing numbers or special characters.
"""

import re

def check_string(s):
    pattern = '^[a-zA-Z]*py$'
    if re.match(pattern, s):
        return True
    else:
        return False