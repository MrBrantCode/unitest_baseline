"""
QUESTION:
Create a function `extract_words` that takes a string as input and returns a list of words. The input string must have a minimum length of 20 characters and contain at least one numerical digit. The function should remove all punctuation marks and special characters from the string, split it into a list of words, convert each word to uppercase, and sort the words alphabetically.
"""

import re

def extract_words(input_string):
    if len(input_string) < 20 or not any(char.isdigit() for char in input_string):
        return []
    
    cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
    words = cleaned_string.split()
    words = [word.upper() for word in words]
    words.sort()
    
    return words