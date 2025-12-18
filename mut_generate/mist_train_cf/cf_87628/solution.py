"""
QUESTION:
Create a function `count_unique_words` that takes a string as input and returns the count of unique words in the string. The function should ignore any leading or trailing spaces in the string and handle punctuation marks and special characters by treating them as word separators.
"""

import re

def count_unique_words(string):
    string = re.sub(r'[^\w\s]', '', string)
    string = string.strip()
    words = string.split()
    unique_words = set(words)
    return len(unique_words)