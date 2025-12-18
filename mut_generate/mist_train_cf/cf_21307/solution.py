"""
QUESTION:
Write a function named `is_palindrome` that determines if a given sentence is a palindrome, ignoring punctuation, white spaces, and case sensitivity. The function should return a boolean value indicating whether the sentence is a palindrome or not.
"""

def is_palindrome(sentence):
    sentence = ''.join(e for e in sentence if e.isalnum()).lower()
    return sentence == sentence[::-1]