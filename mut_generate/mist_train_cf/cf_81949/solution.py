"""
QUESTION:
Write a function `cleanse_string(text)` that takes a string of text as input, removes all non-alphanumeric characters (replacing them with spaces), compresses consecutive spaces into a single space, and preserves the original case of the alphanumeric characters, including multi-byte (UTF-8) characters.
"""

import re
import unicodedata

def cleanse_string(text):
    text = unicodedata.normalize('NFKD', text)
    cleaned_text = re.sub(r'\W+', ' ', text)
    return re.sub(r'\s+', ' ', cleaned_text).strip()