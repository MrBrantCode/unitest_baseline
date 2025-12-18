"""
QUESTION:
Write a function `match_strings` that takes a list of strings as input, ignoring case sensitivity, and returns a new list containing only those strings that have at least one character from A-F (in any order) and at least one special character (!, @, #, $, etc.).
"""

def match_strings(lst):
    special_chars = "!@#$%^&*()[]{}:;<>,.?/~+=|\\`~"
    alphabets = "ABCDEFabcdef"
    
    result = []
    for string in lst:
        has_alpha = any(char in alphabets for char in string)
        has_special = any(char in special_chars for char in string)
        if has_alpha and has_special:
            result.append(string)
    return result