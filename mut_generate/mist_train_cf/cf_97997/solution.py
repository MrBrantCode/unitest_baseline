"""
QUESTION:
Write a function called `invert_sentence` that takes a sentence as input and returns the sentence with the order of words inverted. The function should split the sentence into words, reverse their order, and join them back together into a sentence.
"""

def invert_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)