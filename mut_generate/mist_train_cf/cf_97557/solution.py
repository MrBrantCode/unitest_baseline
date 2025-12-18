"""
QUESTION:
Invert the order of words in a sentence. Write a function `invert_sentence` that takes a sentence as input and returns the sentence with the order of words inverted. The function should split the sentence into words, reverse the order of the words, and then join them back together into a sentence.
"""

def invert_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)