"""
QUESTION:
Design a function `convert_special_to_underscore` that takes a string as input and replaces all non-alphanumeric characters with underscores. The function should use the `re` (regular expression) module.
"""

import re

def convert_special_to_underscore(s):
    return re.sub('\W', '_', s)