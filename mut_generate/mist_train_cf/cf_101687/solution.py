"""
QUESTION:
Write a function called `invert_sentence` that takes a string `sentence` as input, and returns the sentence with the order of the words reversed. The function should not use any additional libraries and should only use built-in Python functions.
"""

def invert_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)