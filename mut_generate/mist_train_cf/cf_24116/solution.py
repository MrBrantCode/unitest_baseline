"""
QUESTION:
Write a function called `reverse_words` that takes a sentence as input and returns the sentence with the order of words reversed.
"""

def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence