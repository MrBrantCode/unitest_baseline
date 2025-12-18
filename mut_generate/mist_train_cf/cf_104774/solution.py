"""
QUESTION:
Create a function called `reverse_string` that takes a string as input, removes any non-alphanumeric characters from the string, and returns the string in reverse order. The function should only consider alphabets and numbers as valid characters.
"""

import re

def entrance(string):
    # Remove special characters
    string = re.sub('[^A-Za-z0-9]+', '', string)
    
    # Reverse the string
    return string[::-1]