"""
QUESTION:
Write a function `reverse_and_convert` that takes a string as input, removes any non-alphabetic characters, reverses the order of the characters, and then swaps the case of the letters (i.e., converts all uppercase letters to lowercase and all lowercase letters to uppercase).
"""

import string

def reverse_and_convert(s):
    # Remove punctuation marks and special characters
    s = ''.join(char for char in s if char.isalpha())
    
    # Reverse the string
    s = s[::-1]
    
    # Convert uppercase to lowercase and vice versa
    s = s.swapcase()
    
    return s