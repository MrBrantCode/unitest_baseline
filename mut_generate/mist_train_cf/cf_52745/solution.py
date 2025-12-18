"""
QUESTION:
Create a function named `capitalize_first_letter` that takes a string `s` as input. The function should capitalize the first letter of each word in the string while preserving the case of the remaining letters. The function should handle punctuation marks attached to words and support special characters from multiple languages, including those with diacritics like umlauts and tildes.
"""

import re

def capitalize_first_letter(s):
    return re.sub(r'\b(\w)', lambda m: m.group().upper(), s)