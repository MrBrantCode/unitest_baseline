"""
QUESTION:
Create a function named `reverse_words` that takes a sentence as input and returns the sentence with the sequence of words reversed. The function should split the sentence into words and then join them back together in reverse order, separated by spaces.
"""

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words