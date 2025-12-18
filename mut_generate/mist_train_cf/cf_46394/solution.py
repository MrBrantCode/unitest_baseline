"""
QUESTION:
Write a function `check_sentence(sentence)` that takes a string as input and returns `True` if the sentence contains all the alphabets (a-z) at least once, ignoring case sensitivity and special characters, and `False` otherwise.
"""

def check_sentence(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return set(sentence.lower()).issuperset(alphabet)