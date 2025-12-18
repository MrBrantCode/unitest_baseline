"""
QUESTION:
Write a function `find_first_unique_char` that takes a string as input and returns the 0-based index of the first non-repeating character in the string. If no such character exists, return -1. Note: Python uses 0-based indexing.
"""

def find_first_unique_char(string):
    # Dictionary to store character counts
    char_count = {}
    
    # Count characters
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    # Scan string for first unique character
    for index, char in enumerate(string):
        if char_count[char] == 1:
            return index
            
    # If no unique character present
    return -1