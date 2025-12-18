"""
QUESTION:
Write a function named `find_longest_strings` that receives a list of strings as input and returns the two strings with the highest length that have at least one capital letter and one punctuation mark.
"""

import string

def find_longest_strings(strings):
    # Remove strings that don't have capital letters or punctuation marks
    valid_strings = [s for s in strings if any(c.isupper() for c in s) and any(c in string.punctuation for c in s)]
    
    # Sort valid strings by length and return the two longest ones
    longest_strings = sorted(valid_strings, key=len, reverse=True)[:2]
    
    return longest_strings