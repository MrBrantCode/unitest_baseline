"""
QUESTION:
Write a function `reverse_words(sentence)` that takes a sentence as input, reverses the order of the words, and reverses each word individually. The function should return a string with the modified sentence. Assume that words are separated by a single space.
"""

def entrance(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    reversed_words = [word[::-1] for word in reversed_sentence.split()]
    return ' '.join(reversed_words)