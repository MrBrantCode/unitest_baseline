"""
QUESTION:
Write a function `is_palindrome(sentence)` that determines whether a given sentence is a palindrome, ignoring case sensitivity and excluding numbers and special characters, but considering punctuation and white spaces.
"""

def is_palindrome(sentence):
    # Removing numbers and special characters from the sentence
    sentence = ''.join(e for e in sentence if e.isalpha() or e.isspace() or not e.isalnum())

    # Ignoring case sensitivity
    sentence = sentence.lower()

    # Checking if the sentence is a palindrome
    return sentence == sentence[::-1]