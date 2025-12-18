"""
QUESTION:
Replace "My website" with "John's website" in the given sentence, maintaining the original capitalization and punctuation, but only if "My website" is not preceded or followed by alphanumeric characters. The function should be named `replace_website`.
"""

import re

def replace_website(sentence):
    return re.sub(r'\bMy website\b', "John's website", sentence)