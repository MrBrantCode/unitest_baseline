"""
QUESTION:
Implement the function `is_happy(s)` that checks if a given string `s` is "happy". A string is considered "happy" if it meets the following conditions: its length is at least 3, every group of 3 consecutive characters are non-repetitive, and every unique character appears at least twice.
"""

def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    unique_chars = set(s)
    for char in unique_chars:
        if s.count(char) < 2:
            return False
    return True