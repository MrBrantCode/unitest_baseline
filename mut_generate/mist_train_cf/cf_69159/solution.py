"""
QUESTION:
Write a function named `compress_string` that takes a string `s` as input and returns the compressed string. The function should replace substrings of length 3 or more with the same character, with a combination of the duplicate character and the number of consecutive occurrences. For example, "aaa" should be replaced with "a3". If there are multiple valid substrings, replace the left-most one.
"""

import re

def compress_string(s):
    # regex to match 3 or more of the same characters in a row
    pattern = re.compile(r'(.)\1{2,}')
    
    # function to replace matches with the character and its count
    repl = lambda m: m.group(1) + str(len(m.group(0)))
    
    # replace matches in the string
    compressed = re.sub(pattern, repl, s)
    
    return compressed