"""
QUESTION:
Create a function `first_non_repeating_character` that takes a string as input and returns the first non-repeating character in the string, excluding any whitespace characters. If no non-repeating character is found, the function should return None.
"""

def first_non_repeating_character(string):
    string = string.replace(" ", "")
    char_counts = {}
    
    for char in string:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    
    for char in string:
        if char_counts[char] == 1:
            return char
    
    return None