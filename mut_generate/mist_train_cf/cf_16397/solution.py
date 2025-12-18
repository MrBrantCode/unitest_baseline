"""
QUESTION:
Write a function `reverse_words` that takes a string as input and returns a modified string with the words in reversed order. The function should first remove any leading or trailing whitespace from the input string, then convert multiple spaces between words to a single space. The position of punctuation marks, special characters, and numbers within the string should remain unchanged.
"""

import re

def reverse_words(string):
    # Remove leading and trailing whitespace
    string = string.strip()
    
    # Convert multiple spaces into a single space
    string = re.sub('\s+', ' ', string)
    
    # Split the string into a list of words
    words = string.split(' ')
    
    # Reverse the order of the words
    words = words[::-1]
    
    # Join the words back into a string
    reversed_string = ' '.join(words)
    
    return reversed_string