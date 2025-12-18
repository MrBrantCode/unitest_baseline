"""
QUESTION:
Write a function named `remove_whitespace` that takes a string as input. The function should remove any leading and trailing whitespaces from the string, replace multiple consecutive whitespace characters between words with a single space character, and return the resulting string.
"""

def remove_whitespace(string):
    # Remove leading and trailing whitespaces
    string = string.strip()
    
    # Remove whitespace characters in between words
    string = ' '.join(string.split())
    
    return string