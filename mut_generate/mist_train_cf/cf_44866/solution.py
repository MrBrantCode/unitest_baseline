"""
QUESTION:
Create a function `string_check(s, min_len, max_len)` that takes a string `s` and two integers `min_len` and `max_len` as input. The function should return the number of unique words in the string if it meets the following conditions: its length is between `min_len` and `max_len` (inclusive), and it does not contain any repeating character sequences of length 2 or more. If the string does not meet these conditions, the function should return `False`.
"""

import re

def string_check(s, min_len, max_len):
    # Check the length of the string
    if len(s) < min_len or len(s) > max_len:
        return False
    # Check for repeating sequences
    for i in range(2, len(s) // 2 + 1):
        pattern = r"(.{%d}).*\1" % i
        if re.search(pattern, s):
            return False
    # If the string passed the length and repeating sequences checks,
    # return the number of unique words
    return len(set(s.split()))