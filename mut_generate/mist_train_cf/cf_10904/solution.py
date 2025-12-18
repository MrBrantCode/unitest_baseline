"""
QUESTION:
Write a function called `find_first_valid_char_index` that finds the index of the first character in a given string that is not a space and is not followed by a punctuation mark. The input string must contain at least one punctuation mark and at least one alphanumeric character.
"""

import string

def find_first_valid_char_index(s):
    for i in range(len(s) - 1):
        if s[i] != ' ' and s[i+1] not in string.punctuation:
            return i