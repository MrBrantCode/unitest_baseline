"""
QUESTION:
Write a function `concatenate_strings` that takes two strings as input, concatenates them without using built-in string concatenation methods or operators, removes any duplicate characters from the resulting string, and returns the result.
"""

def concatenate_strings(string1, string2):
    unique_chars = set()
    
    for char in string1:
        unique_chars.add(char)
    
    for char in string2:
        unique_chars.add(char)
    
    result = ""
    
    for char in sorted(unique_chars):
        result += char
    
    return result