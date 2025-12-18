"""
QUESTION:
Write a function `is_palindrome(sentence)` that determines if a given sentence is a palindrome, ignoring case sensitivity, and excluding any numbers and special characters, but taking into account punctuation and white spaces.
"""

def is_palindrome(sentence):
    # Removing numbers and special characters from the sentence
    sentence = ''.join(e for e in sentence if e.isalpha())
    
    # Ignoring case sensitivity
    sentence = sentence.lower()
    
    # Checking if the sentence is a palindrome
    return sentence == sentence[::-1]