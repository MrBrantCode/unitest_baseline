"""
QUESTION:
Create a function named `partition_special_characters` that takes a string `text` as input. The function should return a set of unique special characters present in the string. A special character is defined as any non-alphanumeric and non-space character. The function should be case-sensitive and should not include duplicate special characters in the output.
"""

import string

def partition_special_characters(text):
    # Initialize set for special characters
    special_chars = set()
    
    for char in text:
        # Check if each character is not an alphanumeric and not a space
        if not(char.isalnum()) and not(char.isspace()):
            special_chars.add(char)
            
    return special_chars