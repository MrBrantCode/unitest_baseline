"""
QUESTION:
Write a function named `is_palindrome` that takes a sentence as input, removes all non-alphanumeric characters, ignores case sensitivity, and returns `True` if the sentence is a palindrome and `False` otherwise.
"""

def is_palindrome(sentence):
    # Remove all non-alphanumeric characters and convert to lowercase
    sentence = ''.join(ch.lower() for ch in sentence if ch.isalnum())
    
    # Check if the reversed sentence is equal to the original sentence
    return sentence == sentence[::-1]