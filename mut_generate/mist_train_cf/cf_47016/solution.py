"""
QUESTION:
Create a function called `purify` that takes a string as input and returns the string with all non-alphanumeric characters (except whitespace) removed. The function should use regular expressions to achieve this.
"""

import re

def purify(text):
    return re.sub('[^a-zA-Z0-9\s]', '', text)