"""
QUESTION:
Implement a function `is_palindrome(sentence)` that checks if a given sentence is a palindrome, considering only alphanumeric characters and ignoring case sensitivity, and ignoring non-alphanumeric characters such as punctuation marks and spaces. The function should return a boolean value indicating whether the sentence is a palindrome or not.
"""

def is_palindrome(sentence):
    # Remove all non-alphanumeric characters and convert to lowercase
    sentence = ''.join(ch.lower() for ch in sentence if ch.isalnum())
    
    # Check if the reversed sentence is equal to the original sentence
    return sentence == sentence[::-1]