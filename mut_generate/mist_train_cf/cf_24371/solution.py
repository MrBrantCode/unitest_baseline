"""
QUESTION:
Write a function called `find_pattern_index` that takes two parameters: `string` and `pattern`. The function should return the starting index of the first occurrence of `pattern` in `string`. If `pattern` is not found in `string`, return -1. The function should be able to handle strings of any length and patterns of any length up to the length of the string.
"""

def find_pattern_index(string, pattern):
    for i in range(len(string) - len(pattern) + 1): 
        if string[i:i+len(pattern)] == pattern: 
            return i 
    return -1