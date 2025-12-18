"""
QUESTION:
Create a function `find_xy_words` that takes a string of text as input and returns a list of words containing the letters 'x' and 'y' in successive sequence within their structure. The function should only match complete words and ignore non-word characters.
"""

import re

def find_xy_words(text):
    xy_words = re.findall(r"\b\w*x\w*y\w*\b", text)
    return xy_words