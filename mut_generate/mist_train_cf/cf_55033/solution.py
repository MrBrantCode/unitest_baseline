"""
QUESTION:
Design a function `clean_text` that takes a string `input_text` as input and returns a string containing only alphabetical, numerical, and white space characters. The function should remove all unconventional or special characters from the input text.
"""

import re

def clean_text(input_text):
    return re.sub(r'[^a-zA-Z0-9 ]', '', input_text)