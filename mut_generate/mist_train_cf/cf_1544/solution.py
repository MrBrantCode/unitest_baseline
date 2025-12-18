"""
QUESTION:
Create a function `extract_words` that takes a string as input and returns an array of words. The input string should have a minimum length of 50 characters and contain at least one uppercase letter, one lowercase letter, one numerical digit, and one special character. The function should ignore any punctuation marks or special characters in the string, convert each word to uppercase, and sort the words in alphabetical order. If the input string is empty, return "Error: Input string is empty." If the input string does not meet the requirements, return "Error: Input string does not meet the requirements."
"""

import re

def extract_words(string):
    if not string:
        return "Error: Input string is empty."
    
    cleaned_string = re.sub(r'[^\w\s]', '', string)
    
    if len(cleaned_string) < 50 or \
       not any(char.isdigit() for char in cleaned_string) or \
       not any(char.islower() for char in cleaned_string) or \
       not any(char.isupper() for char in cleaned_string) or \
       not any(char.isalnum() for char in cleaned_string):
        return "Error: Input string does not meet the requirements."
    
    words = sorted(word.upper() for word in cleaned_string.split())
    
    return words