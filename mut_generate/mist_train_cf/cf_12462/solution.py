"""
QUESTION:
Write a function named `reverse_sentence` that takes a string as input, splits it into words, and returns the words in reverse order. The words should be separated by a space and the output should be a string.
"""

def reverse_sentence(sentence):
    return ' '.join(reversed(sentence.split()))