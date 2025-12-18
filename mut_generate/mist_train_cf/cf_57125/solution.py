"""
QUESTION:
Write a function `count_unique_words` that takes a string `text` as input. The function should count the unique words in the string, ignoring case sensitivity, considering numerals as separate words, and excluding one-letter words. The string can be of unlimited length and may contain words and numerals separated by various delimiters.
"""

import re

def count_unique_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return len(set(word for word in words if len(word) > 1))