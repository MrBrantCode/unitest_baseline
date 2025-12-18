"""
QUESTION:
Write a function `find_valid_words` that takes a string as input and returns a list of words that meet the following conditions: 
- The word is longer than 10 characters.
- The word contains at least one uppercase letter.
- The word contains at least one lowercase letter.
- The word contains at least one digit.
- The word does not contain any special characters (such as punctuation marks or spaces).
Ignore any words that do not meet these conditions.
"""

import re

def find_valid_words(string):
    words = string.split()
    valid_words = []
    
    for word in words:
        if re.search('[^a-zA-Z0-9]', word):
            continue
        
        if len(word) <= 10:
            continue
        
        if not any(char.isupper() for char in word):
            continue
        
        if not any(char.islower() for char in word):
            continue
        
        if not any(char.isdigit() for char in word):
            continue
        
        valid_words.append(word)
    
    return valid_words