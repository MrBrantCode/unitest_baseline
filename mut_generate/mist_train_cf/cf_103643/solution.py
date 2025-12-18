"""
QUESTION:
Create a function `compare_strings` that takes two strings as input and returns the index of the first character that is different between the two strings. If the strings are identical, return -1. If the strings are of unequal length and all characters up to the length of the shorter string are equal, return the length of the shorter string.
"""

def compare_strings(string1, string2):
    # Iterate over the characters in the strings
    for i in range(min(len(string1), len(string2))):
        if string1[i] != string2[i]:
            return i
    
    # If all characters up to this point are equal, but the lengths of the strings are different
    if len(string1) != len(string2):
        return min(len(string1), len(string2))
    
    # If the strings are identical
    return -1