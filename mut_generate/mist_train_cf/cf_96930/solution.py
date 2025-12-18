"""
QUESTION:
Write a function named "classify_string" that takes a string as a parameter and returns a string classification. The function should remove all spaces and punctuation marks from the input string. If the modified string reads the same forward and backward (case-insensitive), classify it as a "Palindrome". If the modified string contains only alphabets, classify it as a "Word". Otherwise, classify it as a "Phrase".
"""

import string

def classify_string(s):
    # Remove spaces and punctuation marks from the string
    modified_string = ''.join(c for c in s if c not in string.punctuation and c != ' ')

    # Check if the modified string is a palindrome
    if modified_string.lower() == modified_string.lower()[::-1]:
        return "Palindrome"
    
    # Check if the modified string contains only alphabets
    if modified_string.isalpha():
        return "Word"
    
    # Otherwise, classify it as a phrase
    return "Phrase"