"""
QUESTION:
Create a function `extract_words` that takes a string as input and returns a list of words. Each word should be in uppercase and sorted in alphabetical order. The function should ignore any punctuation marks or special characters in the string. The input string must have a minimum length of 50 characters and contain at least one uppercase letter, one lowercase letter, one numerical digit, and one special character. If the input string is empty, the function should return an error message.
"""

import re

def extract_words(string):
    # Check if the string is empty
    if not string:
        return "Error: Input string is empty."
    
    # Remove punctuation marks and special characters
    cleaned_string = re.sub(r'[^\w\s]', '', string)
    
    # Check if the cleaned string meets the requirements
    if len(cleaned_string) < 50 or \
       not any(char.isdigit() for char in cleaned_string) or \
       not any(char.islower() for char in cleaned_string) or \
       not any(char.isupper() for char in cleaned_string) or \
       not any(char.isalnum() for char in cleaned_string):
        return "Error: Input string does not meet the requirements."
    
    # Extract words, convert to uppercase, and sort alphabetically
    words = sorted(word.upper() for word in cleaned_string.split())
    
    return words