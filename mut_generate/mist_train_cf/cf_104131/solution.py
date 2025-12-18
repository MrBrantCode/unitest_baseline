"""
QUESTION:
Write a function `remove_leading_zeros(s)` that takes a string `s` as input and returns the string with leading zeros removed, but only if they are followed by a non-zero digit or another zero. The function should handle empty strings and return the original string if no leading zeros need to be removed.
"""

def remove_leading_zeros(s):
    if len(s) == 0:
        return s
    
    i = 0
    while i < len(s) and s[i] == '0':
        i += 1
    
    if i > 0 and i < len(s) and s[i].isdigit() and s[i] != '0':
        s = s[i:]
    
    while s.startswith('00'):
        s = s[1:]
    
    return s