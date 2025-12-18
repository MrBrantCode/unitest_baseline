"""
QUESTION:
Create a function `check_x_not_followed_by_y` that takes a string as input and returns True if the string contains the letter 'X' not immediately followed by 'Y', and False otherwise.
"""

import re

def check_x_not_followed_by_y(s):
    pattern = r"^(?!.*XY).*X.*$"
    return bool(re.search(pattern, s))