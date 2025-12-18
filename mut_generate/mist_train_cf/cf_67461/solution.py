"""
QUESTION:
Write a function `check_palindrome(sentence)` that checks if a given sentence is a palindrome, ignoring punctuation, whitespace, and case. The function should return `True` if the sentence is a palindrome and `False` otherwise.
"""

import re

def check_palindrome(sentence):
    sentence = sentence.lower()
    sentence = re.sub('[^a-z]', '', sentence)
    return sentence == sentence[::-1]