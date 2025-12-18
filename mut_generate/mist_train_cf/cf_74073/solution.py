"""
QUESTION:
Create a function `substitute_numerical_values(s)` that takes a string `s` as input and returns a string with all numerical values replaced with the '#' symbol.
"""

import re

def substitute_numerical_values(s):
    return re.sub('\d', '#', s)