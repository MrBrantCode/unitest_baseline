"""
QUESTION:
Remove leading zeros from a string while handling special characters and emoticons that may appear before alphabets. Create a function named `remove_leading_zeros` that takes a string `s` as input and returns the modified string with leading zeros removed, regardless of special characters or emoticons in between. The function should only remove zeros that appear before alphabets in the string.
"""

import re

def remove_leading_zeros(s):
    return re.sub('0+(?=.*[a-zA-Z])', '', s)