"""
QUESTION:
Create a function called `process_text` that takes a string as input and returns the string with all non-alphanumeric characters removed.
"""

import re

def process_text(s):
    return re.sub(r'\W+', '', s)