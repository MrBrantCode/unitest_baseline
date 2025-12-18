"""
QUESTION:
Implement a function `is_palindrome(sentence)` that checks if a given sentence is a palindrome, ignoring non-alphanumeric characters and case sensitivity. The function should return `True` if the sentence is a palindrome and `False` otherwise.
"""

def is_palindrome(sentence):
    sentence = ''.join(filter(str.isalnum, sentence.lower()))
    return sentence == sentence[::-1]