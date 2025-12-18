"""
QUESTION:
Create a function named `is_palindrome` that takes a sentence as input and returns a boolean indicating whether the sentence is a palindrome. The function should be case-insensitive, ignore non-alphanumeric characters, and consider spaces and punctuation marks as part of the palindrome check. The input sentence can contain any characters, including letters, numbers, spaces, and punctuation marks.
"""

import re

def is_palindrome(sentence):
    # Convert the sentence to lowercase and remove non-alphanumeric characters
    sentence = re.sub(r'[^a-zA-Z0-9]', '', sentence.lower())
    
    # Check if the modified sentence is equal to its reverse
    return sentence == sentence[::-1]