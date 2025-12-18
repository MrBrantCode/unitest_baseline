"""
QUESTION:
Write a function named `split_string` that takes a string as input, splits it into words, and returns a list of words. The function should exclude any words containing numbers or special characters, convert all words to lowercase, and remove any duplicates from the list. The function should also handle strings with multiple spaces between words.
"""

import re

def split_string(s):
    # Split the string into words
    words = re.findall(r'\w+', s.lower())
    
    # Remove words with numbers or special characters
    words = [word for word in words if word.isalpha()]
    
    # Remove duplicate words
    words = list(set(words))
    
    return words