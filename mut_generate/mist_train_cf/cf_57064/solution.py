"""
QUESTION:
Write a function `find_distinctive_char` that finds the index of the first unique character in a given string. The function should return the index of the first character that appears only once in the string, or -1 if no such character exists. The index is 0-based.
"""

def find_distinctive_char(string):
    char_count = {}
    
    # Count the occurrences of each character
    for c in string:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    
    # Check for the first character that only occurs once
    for i in range(len(string)):
        if char_count[string[i]] == 1:
            return i
    
    # No unique characters
    return -1