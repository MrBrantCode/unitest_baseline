"""
QUESTION:
Write a function `remove_punctuation` that removes all punctuation from a given string while preserving special characters such as emojis and non-English characters. The function should take a string as input and return the cleaned string.
"""

import re

def remove_punctuation(string):
    # Remove punctuation marks except emojis and non-English characters
    cleaned_string = re.sub(r'[^\w\s😊\u0080-\uFFFF]', '', string)
    return cleaned_string