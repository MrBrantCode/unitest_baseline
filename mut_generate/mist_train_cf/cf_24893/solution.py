"""
QUESTION:
Write a function `string_two_characters` that takes an input string and returns a new string made of the first two and last two characters of the input string.
"""

def string_two_characters(s): 
    n = len(s)
    return s[0:2] + s[n-2:n]