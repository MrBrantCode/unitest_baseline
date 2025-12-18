"""
QUESTION:
Write a function `is_palindrome` that checks if a given sentence is a palindrome. The sentence can contain spaces, punctuation marks, special characters, digits, and symbols. The function should disregard any spaces, punctuation marks, special characters, and capitalization, and return True if the sentence is a palindrome, False otherwise. The sentence should have at least two words, and at least three of the words in the sentence should be palindromes themselves. The sentence should not have any repeated words or consecutive repeated characters in any of the words.
"""

import re

def is_palindrome(sentence):
    # Remove spaces, punctuation marks, and special characters
    sentence = re.sub('[^A-Za-z0-9]+', '', sentence)
    
    # Convert to lowercase
    sentence = sentence.lower()
    
    # Check if the resulting string is equal to its reverse
    return sentence == sentence[::-1]