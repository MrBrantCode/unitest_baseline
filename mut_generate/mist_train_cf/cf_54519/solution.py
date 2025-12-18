"""
QUESTION:
Create a function called `duplicate_seq` that takes a string as input, removes all punctuation and numeric characters, converts all alphabetic characters to lowercase, and returns the resulting string duplicated.
"""

import re

def duplicate_seq(string):
    clean_string = re.sub('[^A-Za-z]', '', string)
    clean_string = clean_string.lower()
    return clean_string*2