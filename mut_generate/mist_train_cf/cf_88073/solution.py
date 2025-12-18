"""
QUESTION:
Create a function named `is_palindrome(sentence)` that determines whether a given sentence is a palindrome, ignoring case, and non-alphanumeric characters. The function should consider spaces and punctuation marks as part of the palindrome check, and it should handle palindromes with more than one word and with punctuation marks within words.
"""

import re

def is_palindrome(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    
    # Remove non-alphanumeric characters using regular expression
    sentence = re.sub('[^a-zA-Z0-9]', '', sentence)
    
    # Check if the sentence is a palindrome
    return sentence == sentence[::-1]