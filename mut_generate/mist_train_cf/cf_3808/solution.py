"""
QUESTION:
Create a function `is_palindrome` that determines if a given string is a palindrome of another, considering spaces, punctuation, and capitalization. The function should handle input strings of up to 1 million characters in length and optimize its performance and memory usage.
"""

def entrance(s1, s2):
    s1 = ''.join(filter(str.isalnum, s1)).lower()
    s2 = ''.join(filter(str.isalnum, s2)).lower()
    return s1 == s2[::-1]