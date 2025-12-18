"""
QUESTION:
Write a function `text_to_asterisks` that takes a string `s` as input and performs a two-way conversion between punctuation marks and asterisks. The function should replace punctuation marks with asterisks if there are no asterisks in the string, and replace asterisks with periods and punctuation marks with asterisks if there are some asterisks. The function should handle edge cases such as null or empty strings, strings entirely made up of punctuation marks or asterisks, and nested conversions. The function should be optimized for efficiency in terms of time and space complexity, and should be able to manage strings of any length.
"""

import string

def text_to_asterisks(s):
    if not s:
        return s
    asterisks = s.count('*')
    if asterisks == 0: 
        return ''.join(['*' if c in string.punctuation else c for c in s])
    elif asterisks == len(s): 
        return '.' * len(s)
    else: 
        return ''.join(['*' if c in string.punctuation else '.' if c == '*' else c for c in s])