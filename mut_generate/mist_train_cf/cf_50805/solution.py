"""
QUESTION:
Write a function `append_string(s)` that takes a string `s` as input. If `s` contains any numerical characters, return `s` as is. Otherwise, remove all punctuation from `s` and append the cleaned string to itself.
"""

import string

def append_string(s):
    # check if string contains a digit
    if any(char.isdigit() for char in s):
        return s

    # remove punctuation using translation table
    translator = str.maketrans('', '', string.punctuation)
    s_without_punctuation = s.translate(translator)

    return s_without_punctuation + s_without_punctuation