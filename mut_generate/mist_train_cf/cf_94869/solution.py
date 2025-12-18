"""
QUESTION:
Write a function `find_index(s)` that finds the index of the first character in a string `s` that is not a space and is followed by a punctuation mark. The function should return the index of the first occurrence that satisfies the conditions. If no such character is found, return -1.
"""

import string

def find_index(s):
    punctuation = set(string.punctuation)
    
    for i in range(len(s) - 1):
        if s[i] != ' ' and s[i] not in punctuation and s[i+1] in punctuation:
            return i
    
    return -1