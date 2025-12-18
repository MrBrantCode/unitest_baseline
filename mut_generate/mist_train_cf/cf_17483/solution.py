"""
QUESTION:
Write a function called `remove_whitespace` that takes a string as input and returns a new string. The function should remove any leading and trailing whitespace characters from the input string and replace any sequence of one or more whitespace characters between words with a single space character.
"""

def remove_whitespace(string):
    # Remove leading and trailing whitespaces
    string = string.strip()
    
    # Remove whitespace characters in between words
    string = ' '.join(string.split())
    
    return string