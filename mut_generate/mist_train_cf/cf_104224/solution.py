"""
QUESTION:
Write a function `is_palindrome(sentence)` that determines if a given sentence is a palindrome. The function should consider only alphanumeric characters, ignoring case sensitivity, non-alphanumeric characters, and spaces. The input sentence may contain punctuation and special characters.
"""

def is_palindrome(sentence):
    # Remove non-alphanumeric characters and convert to lowercase
    clean_sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    
    # Check if the cleaned sentence is equal to its reverse
    return clean_sentence == clean_sentence[::-1]