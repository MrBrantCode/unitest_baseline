"""
QUESTION:
Create a function `word_count(s)` that takes a string `s` as input and returns a dictionary with the count of each word in the string. The function should exclude special characters and punctuation marks from the count, be case-insensitive, and handle exceptions for null or empty input strings. The function should also be efficient enough to handle large strings.
"""

import collections
import string

def word_count(s):
    try:
        if s:  
            words = s.translate(str.maketrans('', '', string.punctuation)).lower().split()    
            return dict(collections.Counter(words))
        else:  
            return "Input string is empty."
    except Exception as e: 
        return str(e)