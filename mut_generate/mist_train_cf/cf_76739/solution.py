"""
QUESTION:
Design a function called `is_palindrome` that takes a sentence as input, returns `True` if the sentence is a palindrome (ignoring case, spaces, punctuation, and special characters), and `False` otherwise. The function should handle palindromes that are phrases or sentences, not just individual words.
"""

import re

def is_palindrome(sentence):
    sentence = re.sub(r'\W+', '', sentence.lower())   # Remove non-alphanumeric characters and convert to lowercase
    return sentence == sentence[::-1]