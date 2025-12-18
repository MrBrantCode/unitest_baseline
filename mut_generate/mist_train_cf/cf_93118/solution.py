"""
QUESTION:
Write a function named `replace_words` that takes two parameters: the input string `s` and the words to be replaced, along with their corresponding replacement words, as a dictionary `d`. The function should replace the words in the string with their corresponding replacement words in a case-insensitive manner, regardless of punctuation or special characters. The function should return the modified string.
"""

import re

def replace_words(s, d):
    for key in d:
        pattern = r'\b' + re.escape(key) + r'(?=[\W]|$)'
        s = re.sub(pattern, d[key], s, flags=re.IGNORECASE)
    return s