"""
QUESTION:
Write a function named "remove_consecutive_reverse" that takes a string as input, removes all consecutive characters, and returns the non-consecutive characters in reverse order. The function should handle strings with both uppercase and lowercase letters in a case-sensitive manner.
"""

def remove_consecutive_reverse(s):
    if len(s) <= 1:
        return s
    
    if s[0] == s[1]:
        return remove_consecutive_reverse(s[1:])
    
    return remove_consecutive_reverse(s[1:]) + s[0]