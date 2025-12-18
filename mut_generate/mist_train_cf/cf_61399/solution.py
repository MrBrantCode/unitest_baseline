"""
QUESTION:
Write a function `replace_special_chars` that takes a string as input and returns the string after replacing all special characters with an empty string. The function should consider all punctuation characters as special characters.
"""

import re
import string

def replace_special_chars(str1):
    #list of special characters
    special_chars = string.punctuation
    pattern = "[" + special_chars + "]"

    #replace special characters with empty string
    str1 = re.sub(pattern, "", str1)
    return str1