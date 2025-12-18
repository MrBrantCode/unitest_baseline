"""
QUESTION:
Create a function `find_uppercase_words(s)` that takes a string `s` as input, parses it into words while ignoring non-alphabetic characters, and returns a list of words that are entirely in uppercase.
"""

import re

def find_uppercase_words(s):
    word_list = re.findall(r'\b\w+\b', s)  
    uppercase_words = []
    for word in word_list:                  
        if word.isupper():                  
            uppercase_words.append(word)
    return uppercase_words