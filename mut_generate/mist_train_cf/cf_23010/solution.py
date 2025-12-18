"""
QUESTION:
Implement a function `pack_string` that takes a string `s` of variable length between 8 and 20 characters and returns a list of unique characters from the string, preserving their original order, and padded with None values to a length of 8 if necessary. The function should have a time complexity of O(n), where n is the length of the string.
"""

def pack_string(s):
    seen = set()
    unique_chars = []
    
    for char in s:
        if char not in seen:
            seen.add(char)
            unique_chars.append(char)
            if len(unique_chars) == 8:
                break
                
    unique_chars += [None] * (8 - len(unique_chars))
    
    return unique_chars