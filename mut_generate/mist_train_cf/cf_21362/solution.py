"""
QUESTION:
Create a function named `remove_special_characters` that takes a string as input, removes any non-alphanumeric characters and special characters within alphanumeric characters, and converts all characters to lowercase. The input string will only contain printable ASCII characters.
"""

import re

def remove_special_characters(string):
    # Remove non-alphanumeric characters and special characters within alphanumeric characters
    string = re.sub('[^a-zA-Z0-9]+', '', string)
    
    # Convert uppercase letters to lowercase
    string = string.lower()
    
    return string