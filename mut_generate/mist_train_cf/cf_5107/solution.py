"""
QUESTION:
Create a function `find_valid_words` that takes a string as input, and returns a list of words that meet the following conditions:

* Are longer than 10 characters
* Contain at least one uppercase letter
* Contain at least one lowercase letter
* Contain at least one digit
* Do not contain any special characters (such as punctuation marks or spaces)

The function should ignore any words that do not meet these conditions.
"""

import re

def find_valid_words(string):
    words = string.split()
    valid_words = []
    
    for word in words:
        # Check if word contains special characters
        if re.search('[^a-zA-Z0-9]', word):
            continue
        
        # Check if word is longer than 10 characters
        if len(word) <= 10:
            continue
        
        # Check if word contains at least one uppercase letter
        if not any(char.isupper() for char in word):
            continue
        
        # Check if word contains at least one lowercase letter
        if not any(char.islower() for char in word):
            continue
        
        # Check if word contains at least one digit
        if not any(char.isdigit() for char in word):
            continue
        
        # If all conditions are met, add word to valid_words list
        valid_words.append(word)
    
    return valid_words