"""
QUESTION:
Write a function named `reverse_sentence` that takes a string of words as input and returns a string with the order of the words reversed.
"""

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence