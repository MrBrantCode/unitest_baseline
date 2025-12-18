"""
QUESTION:
Create a function `is_palindrome(sentence)` that determines if a given sentence is a palindrome. The function should be case-insensitive and ignore non-alphanumeric characters. It should handle sentences with multiple words and punctuation marks.
"""

import re

def is_palindrome(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    
    # Remove non-alphanumeric characters using regular expression
    sentence = re.sub('[^a-zA-Z0-9]', '', sentence)
    
    # Check if the sentence is a palindrome
    return sentence == sentence[::-1]