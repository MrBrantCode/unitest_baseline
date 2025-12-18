"""
QUESTION:
Write a function `reverse_sentence` that takes a string of words as input and returns the words in reverse order. The function should not reverse the characters within each word, only the order of the words themselves.
"""

def reverse_sentence(sentence):
    return ' '.join(reversed(sentence.split()))