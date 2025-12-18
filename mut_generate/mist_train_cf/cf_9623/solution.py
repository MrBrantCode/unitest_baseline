"""
QUESTION:
Write a function `to_uppercase(string)` that converts a given string to uppercase without using any built-in string or character conversion methods. The function should handle both uppercase and lowercase letters, as well as non-alphabet characters.
"""

def to_uppercase(string):
    uppercase_string = ""
    
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - (ord('a') - ord('A')))
        else:
            uppercase_char = char
        uppercase_string += uppercase_char
    
    return uppercase_string