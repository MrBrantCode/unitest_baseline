"""
QUESTION:
Write a function called `remove_odd_index_chars` that takes a string `s` as input and returns a modified string with characters at odd index positions removed, while ignoring any punctuation marks. The function should consider the index positions from the start of the string and 0 as an even index.
"""

import string

def remove_odd_index_chars(s):
    punctuations = string.punctuation
    modified_string = ""
    
    for i, char in enumerate(s):
        if char in punctuations:
            continue
        if i % 2 == 0:
            modified_string += char
    
    return modified_string