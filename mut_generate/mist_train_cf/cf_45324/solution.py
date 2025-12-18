"""
QUESTION:
Create a function called `invert_string` that takes a string of words as input and returns a new string where the order of the words is reversed. The words themselves should not be reversed, only their order in the string.
"""

def invert_string(string):
    words = string.split(' ')  
    words = list(reversed(words))  
    string_inverted = ' '.join(words)  
    return string_inverted