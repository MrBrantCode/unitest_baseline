"""
QUESTION:
Write a function named `count_words` that takes a string as input and returns the number of words in the string. The string may contain punctuation marks, numbers, and special characters, as well as multiple spaces or other whitespace characters separating words. Ignore any leading or trailing whitespace characters in the string.
"""

import re

def count_words(string):
    string = string.strip()
    words = re.findall(r'\w+', string)
    return len(words)