"""
QUESTION:
Write a function `reverse_sentence` that takes a string of words as input and returns the string with the words in reverse order. The function should not reverse the order of characters within each word, but only the order of the words themselves.
"""

def reverse_sentence(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))