"""
QUESTION:
Create a function named `reverser` that takes a sentence as input, reverses each word within the sentence while maintaining the original order of the words, and returns the modified sentence.
"""

def entance(sentence):
    words = sentence.split(' ')
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence