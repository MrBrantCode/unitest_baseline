"""
QUESTION:
Write a function named `count_words` that takes a string as input and returns the number of words that are at least 3 characters long and consist only of alphabetic characters (excluding hyphens and apostrophes as separate words). The function should ignore any leading or trailing spaces in the string and any punctuation marks such as periods, exclamation marks, question marks, or commas.
"""

import re

def count_words(string):
    string = string.strip()
    string = re.sub(r'[^\w\s-]', '', string)
    words = string.split()
    words = [word for word in words if len(word) >= 3 and word.isalpha()]
    return len(words)