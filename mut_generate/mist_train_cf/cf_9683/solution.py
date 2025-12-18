"""
QUESTION:
Create a function `is_substring(long_str, short_str)` that determines if `short_str` is a substring of `long_str` without using any built-in string searching functions or libraries. The function should handle cases where the input strings are empty or have special characters, and return `True` if `short_str` is a substring of `long_str` and `False` otherwise.
"""

def is_substring(long_str, short_str):
    if not long_str or not short_str:
        return False
    
    long_len = len(long_str)
    short_len = len(short_str)
    
    if long_len < short_len:
        return False
    
    for i in range(long_len - short_len + 1):
        if long_str[i:i+short_len] == short_str:
            return True
    
    return False