"""
QUESTION:
Implement a function `replace_phrase(string, phrase, new_phrase)` that takes three parameters: the input string, the phrase to be replaced, and the new phrase. The function should replace all occurrences of the specified phrase in the string with the new phrase, considering only complete words and ignoring case sensitivity.
"""

import re

def replace_phrase(string, phrase, new_phrase):
    pattern = r'\b{}\b'.format(re.escape(phrase))
    return re.sub(pattern, new_phrase, string, flags=re.IGNORECASE)